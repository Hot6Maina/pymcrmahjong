from common import DivisionPartTypeEnum, YakuEnum
from agari_info import AgariInfo
from division import Division
from tile import Tiles
from base_yaku import BaseYaku


class LittleThreeDragons(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.LITTLE_THREE_DRAGONS)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        is_dragon_head = any(
            part.type is DivisionPartTypeEnum.HEAD
            and part.counts.is_containing_only(Tiles.DRAGONS)
            for part in division.parts
        )
        num_dragon_triplets = sum(
            1
            for part in division.parts
            if part.counts.is_containing_only(Tiles.DRAGONS)
            and (
                part.type is DivisionPartTypeEnum.TRIPLE
                or part.type is DivisionPartTypeEnum.QUAD
            )
        )
        return is_dragon_head and num_dragon_triplets == 2
