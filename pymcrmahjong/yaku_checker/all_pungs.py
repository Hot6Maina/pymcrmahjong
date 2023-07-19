from common import DivisionPartTypeEnum, YakuEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku


class AllPungs(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.ALL_PUNGS)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        num_triplets = sum(
            1
            for part in division.parts
            if part.type is DivisionPartTypeEnum.TRIPLE
            or part.type is DivisionPartTypeEnum.QUAD
        )
        return int(num_triplets == 4)
