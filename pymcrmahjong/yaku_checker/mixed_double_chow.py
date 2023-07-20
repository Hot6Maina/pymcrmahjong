from itertools import combinations

from common import DivisionPartTypeEnum, YakuEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku


class MixedDoubleChow(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.MIXED_DOUBLE_CHOW)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        count = 0
        for part1, part2 in combinations(division.parts, 2):
            if not (
                part1.type is part2.type is DivisionPartTypeEnum.SEQUENCE
            ):
                continue
            if (
                part1.tile_type == part2.tile_type
            ):
                continue
            if (
                part1.counts.get_tile_number[0] ==
                part2.counts.get_tile_number[0]
            ):
                count += 1
        return count
