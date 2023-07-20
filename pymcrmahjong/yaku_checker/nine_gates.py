import numpy as np

from common import YakuEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku


class NineGates(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.NINE_GATES)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        if division.is_opened:
            return False

        tile_count = division.tile_count
        base_shape = np.array([3, 1, 1, 1, 1, 1, 1, 1, 3])
        base_shape[division.agari_tile.number - 1] += 1

        return (
            tile_count[0:9] == base_shape
            or tile_count[9:18] == base_shape
            or tile_count[18:27] == base_shape
        )
