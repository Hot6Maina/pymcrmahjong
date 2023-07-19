from common import DivisionPartTypeEnum, YakuEnum
from agari_info import AgariInfo
from division import Division
from tile import Tiles
from base_yaku import BaseYaku


class LittleFourWinds(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.LITTLE_FOUR_WINDS)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        is_wind_head = any(
            part.type is DivisionPartTypeEnum.HEAD
            and part.counts.is_containing_only(Tiles.WINDS)
            for part in division.parts
        )
        num_wind_triplets = sum(
            1
            for part in division.parts
            if part.counts.is_containing_only(Tiles.WINDS)
            and (
                part.type is DivisionPartTypeEnum.TRIPLE
                or part.type is DivisionPartTypeEnum.QUAD
            )
        )
        return is_wind_head and num_wind_triplets == 3
