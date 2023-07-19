from common import YakuEnum, DivisionPartTypeEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku


class ConcealedKong(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.CONCEALED_KONG)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        return sum(
            1
            for part in division.parts
            if part.is_concealed
            and (
                part.type is DivisionPartTypeEnum.QUAD
            )
        )
