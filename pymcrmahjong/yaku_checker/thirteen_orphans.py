from common import YakuEnum, DivisionPartTypeEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku


class ThirteenOrphans(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.THIRTEEN_ORPHANS)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        for part in division.parts:
            if part.type == DivisionPartTypeEnum.THIRTEEN_ORPHANS:
                return int(True)
        return int(False)
