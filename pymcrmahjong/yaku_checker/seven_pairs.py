from common import YakuEnum, DivisionPartTypeEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku


class SevenPairs(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.SEVEN_PAIRS)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        count = 0
        for part in division.parts:
            if part.type == DivisionPartTypeEnum.HEAD:
                count += 1
        return int(count == 7)
