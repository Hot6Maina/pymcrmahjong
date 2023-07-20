from common import DivisionPartTypeEnum, YakuEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku
from tile import Tiles


class DoublePung(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.DOUBLE_PUNG)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        count = [0] * 10
        for part in division.parts:
            if part.counts.is_containing_only(Tiles.NUMBERS) and (part.type == DivisionPartTypeEnum.TRIPLE or part.type == DivisionPartTypeEnum.QUAD):
                count[part.counts.get_tile_number[0]] += 1
        return count.count(2)
