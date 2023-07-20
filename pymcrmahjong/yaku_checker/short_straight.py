from itertools import combinations

from common import DivisionPartTypeEnum, YakuEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku


class ShortStraight(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.SHORT_STRAIGHT)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        count = 0
        for part1, part2 in combinations(division.parts, 2):
            if not (
                part1.type is part2.type is DivisionPartTypeEnum.SEQUENCE
            ):
                continue
            if (
                part1.tile_type != part2.tile_type
            ):
                continue
            first_number_list = sorted(
                [part1.counts.get_tile_number[0],
                 part2.counts.get_tile_number[0]]
            )
            if (
                    first_number_list[0] + 3 == first_number_list[1]
            ):
                count += 1
        return count
