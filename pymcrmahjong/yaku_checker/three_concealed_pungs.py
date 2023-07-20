from common import YakuEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku


class ThreeConcealedPungs(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.THREE_CONCEALED_PUNGS)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        return int(division.num_concealed_triplets == 3)
