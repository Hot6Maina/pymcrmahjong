from __future__ import annotations

from typing import Iterable, Sequence

import numpy as np
from pydantic import BaseModel

from hand import Hand
from tile import Tile, Tiles


class TileCount(BaseModel):
    counts: np.ndarray = np.zeros(len(Tiles.DEFAULTS), dtype=np.int64)
    tile_num: list

    @property
    def num_tiles(self) -> int:
        return sum(self.counts)

    @property
    def get_tile_number(self) -> list:
        if not self.tile_num:
            for i in range(27):
                self.tile_num.append(i%9+1)
            if not self.tile_num:
                self.tile_num.append(0)
            self.tile_num.sort()
        return self.tile_num

    @staticmethod
    def create_from_tiles(tiles: Iterable[Tile]):
        return TileCount(
            counts=np.bincount([tile for tile in tiles], minlength=len(Tiles.DEFAULTS))
        )

    def __eq__(self, other):
        if not isinstance(other, TileCount):
            return NotImplemented
        return np.equal(self.counts, other.counts).all()

    def __add__(self, other: TileCount):
        return TileCount(counts=self.counts + other.counts)

    def __getitem__(self, idx):
        return self.counts[idx]

    def __setitem__(self, idx, value):
        self.counts[idx] = value

    def find_earliest_nonzero_index(self, index: int = 0):
        while index < len(self.counts) and self.counts[index] == 0:
            index += 1
        return index

    def is_containing_only(self, indices: Sequence[int]) -> bool:
        return self.counts[indices].sum() == self.counts.sum()

    def count_tile(self, indices: Sequence[int]) -> int:
        return self.counts[indices].sum()

    class Config:
        arbitrary_types_allowed = True


class HandCount(BaseModel):
    concealed_count: TileCount
    call_counts: list[TileCount]

    @staticmethod
    def create_from_hand(hand: Hand):
        concealed_count = TileCount.create_from_tiles(hand.iter_concealed_tiles)
        call_counts = [TileCount.create_from_tiles(call.tiles) for call in hand.calls]
        return HandCount(concealed_count=concealed_count, call_counts=call_counts)

    @property
    def total_count(self) -> TileCount:
        return sum(self.call_counts, start=self.concealed_count)

    def __getitem__(self, item):
        return self.concealed_count[item] + sum(
            call_count[item] for call_count in self.call_counts
        )
