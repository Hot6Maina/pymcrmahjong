from common import YakuEnum, DivisionPartTypeEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku
from tile import Tiles


class SevenShiftedPairs(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.SEVEN_SHIFTED_PAIRS)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        count = 0
        for part in division.parts:
            if part.type == DivisionPartTypeEnum.HEAD:
                count += 1
        if count != 7:
            return int(False)
        good_flag = False
        tile_count = division.tile_count
        if tile_count.is_containing_only(Tiles.MANS) \
            or tile_count.is_containing_only(Tiles.PINS) \
                or tile_count.is_containing_only(Tiles.SOUS):
            number_list = []
            for part in division.parts:
                number_list.append(part.counts.get_tile_number[0])
            number_list = sorted(set(number_list))
            if len(number_list) == 7 and number_list[-1] - number_list[0] == 6:
                good_flag = True
        return int(good_flag)
