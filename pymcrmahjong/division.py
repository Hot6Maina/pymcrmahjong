from pydantic import BaseModel

from common import CallTypeEnum, DivisionPartTypeEnum, TileTypeEnum
from call import Call
from count import TileCount
from tile import Tile, Tiles


class DivisionPart(BaseModel):
    type: DivisionPartTypeEnum
    tile_type: TileTypeEnum
    counts: TileCount
    is_concealed: bool

    @staticmethod
    def create_head(tile: Tile, is_concealed: bool):
        return DivisionPart(
            type=DivisionPartTypeEnum.HEAD,
            tile_type=tile.type,
            counts=TileCount.create_from_tiles([tile] * 2),
            is_concealed=is_concealed,
        )

    @staticmethod
    def create_triple(tile: Tile, is_concealed: bool):
        return DivisionPart(
            type=DivisionPartTypeEnum.TRIPLE,
            tile_type=tile.type,
            counts=TileCount.create_from_tiles([tile] * 3),
            is_concealed=is_concealed,
        )

    @staticmethod
    def create_straight(tile: Tile, is_concealed: bool):
        return DivisionPart(
            type=DivisionPartTypeEnum.SEQUENCE,
            tile_type=tile.type,
            counts=TileCount.create_from_tiles([tile, Tile(tile + 1), Tile(tile + 2)]),
            is_concealed=is_concealed,
        )

    @staticmethod
    def create_knitted(tile: Tile, is_concealed: bool):
        return DivisionPart(
            type=DivisionPartTypeEnum.KNITTED,
            tile_type=tile.type,
            counts=TileCount.create_from_tiles([tile, Tile(tile + 3), Tile(tile + 6)]),
            is_concealed=is_concealed,
        )

    @staticmethod
    def create_thirteen_orphans(head_tile: Tile, is_concealed: bool):
        return DivisionPart(
            type=DivisionPartTypeEnum.THIRTEEN_ORPHANS,
            tile_type=TileTypeEnum.ETC,
            counts=TileCount.create_from_tiles(
                Tiles.TERMINALS_AND_HONORS + [head_tile]
            ),
            is_concealed=is_concealed,
        )

    @staticmethod
    def create_from_call(call: Call):
        part_type = 0
        if call.type == CallTypeEnum.CHII:
            part_type = DivisionPartTypeEnum.SEQUENCE
        elif call.type == CallTypeEnum.PON:
            part_type = DivisionPartTypeEnum.TRIPLE
        else:
            part_type = DivisionPartTypeEnum.QUAD

        return DivisionPart(
            type=part_type,
            tile_type=call.tiles[0].type,
            counts=TileCount.create_from_tiles(call.tiles),
            is_concealed=call.type is CallTypeEnum.CONCEALED_KAN,
        )


class Division(BaseModel):
    parts: list[DivisionPart]
    agari_tile: Tile
    is_opened: bool

    @property
    def tile_count(self) -> TileCount:
        return sum((part.counts for part in self.parts), start=TileCount())

    @property
    def num_concealed_triplets(self) -> int:
        return sum(
            1
            for part in self.parts
            if part.is_concealed
            and (
                    part.type is DivisionPartTypeEnum.TRIPLE
                    or part.type is DivisionPartTypeEnum.QUAD
            )
        )

    @property
    def num_quads(self) -> int:
        return sum(1 for part in self.parts if part.type is DivisionPartTypeEnum.QUAD)
