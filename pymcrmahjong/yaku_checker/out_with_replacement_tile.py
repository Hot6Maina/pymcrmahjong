from common import YakuEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku


class OutWithReplacementTile(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.OUT_WITH_REPLACEMENT_TILE)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        return int(agari_info.is_replacement_tile)
