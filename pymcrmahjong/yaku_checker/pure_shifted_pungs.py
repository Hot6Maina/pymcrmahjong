from itertools import combinations

from common import DivisionPartTypeEnum, YakuEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku


class PureShiftPungs(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.PURE_SHIFTED_PUNGS)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        for part1, part2, part3 in combinations(division.parts, 3):
            if not (
                part1.type in (DivisionPartTypeEnum.TRIPLE, DivisionPartTypeEnum.QUAD) and
                part2.type in (DivisionPartTypeEnum.TRIPLE, DivisionPartTypeEnum.QUAD) and
                part3.type in (DivisionPartTypeEnum.TRIPLE, DivisionPartTypeEnum.QUAD)
            ):
                continue
            if not (
                part1.tile_type == part2.tile_type and
                part2.tile_type == part3.tile_type and
                part1.tile_type == part1.tile_type
            ):
                continue
            first_number_list = sorted(
                [part1.counts.get_tile_number[0],
                 part2.counts.get_tile_number[0],
                 part3.counts.get_tile_number[0]]
            )
            if (
                first_number_list[0] + 1 == first_number_list[1] and
                first_number_list[1] + 1 == first_number_list[2]
            ):
                return int(True)
        return int(False)
