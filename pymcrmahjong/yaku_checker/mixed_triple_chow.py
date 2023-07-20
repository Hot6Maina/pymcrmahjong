from itertools import combinations

from common import DivisionPartTypeEnum, YakuEnum, TileTypeEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku


class MixedTripleChow(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.MIXED_TRIPLE_CHOW)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        for part1, part2, part3 in combinations(division.parts, 3):
            if not (
                part1.type is part2.type is part3.type is DivisionPartTypeEnum.SEQUENCE
            ):
                continue
            if (
                part1.tile_type == part2.tile_type or
                part2.tile_type == part3.tile_type or
                part1.tile_type == part1.tile_type
            ):
                continue
            if (
                part1.counts.get_tile_number[0] ==
                part2.counts.get_tile_number[0] ==
                part3.counts.get_tile_number[0]
            ):
                return int(True)
        return int(False)
