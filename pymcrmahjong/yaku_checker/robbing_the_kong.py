from common import YakuEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku


class RobbingTheKong(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.ROBBING_THE_KONG)

    def is_satisfied(self, division: Division, agari_info: AgariInfo) -> bool:
        return agari_info.is_robbing_a_quad
