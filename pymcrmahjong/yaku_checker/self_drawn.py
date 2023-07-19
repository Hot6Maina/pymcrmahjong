from common import YakuEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku


class SelfDrawn(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.SELF_DRAWN)

    def is_satisfied(self, division: Division, agari_info: AgariInfo) -> bool:
        return agari_info.is_tsumo_agari and division.is_opened
