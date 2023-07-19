from common import YakuEnum, DivisionPartTypeEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku


class TwoConcealedKong(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.TWO_CONCEALED_KONGS)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        return int(sum(
            1
            for part in division.parts
            if part.is_concealed
            and (
                part.type is DivisionPartTypeEnum.QUAD
            )
        ) == 2)
