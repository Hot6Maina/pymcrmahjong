from common import DivisionPartTypeEnum, YakuEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku


class PrevalentWind(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.PREVALENT_WIND)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        return any(
            (
                part.type is DivisionPartTypeEnum.TRIPLE
                or part.type is DivisionPartTypeEnum.QUAD
            )
            and part.counts.is_containing_only([agari_info.round_wind])
            for part in division.parts
        )
