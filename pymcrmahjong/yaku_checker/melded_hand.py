from common import YakuEnum, DivisionPartTypeEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku


class Melded_Hand(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.MELDED_HAND)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        for part in division.parts:
            if part != DivisionPartTypeEnum.HEAD:
                if part.is_concealed:
                    return int(False)
        return int(not AgariInfo.is_tsumo_agari)