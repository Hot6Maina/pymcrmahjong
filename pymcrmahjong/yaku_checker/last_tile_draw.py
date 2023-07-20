from common import YakuEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku


class LastTileDraw(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.LAST_TILE_DRAW)

    def is_satisfied(self, division: Division, agari_info: AgariInfo) -> bool:
        return agari_info.is_last_draw
