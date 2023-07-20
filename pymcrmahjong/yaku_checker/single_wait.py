from common import YakuEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku
from common import WaitEnum


class SingleWait(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.SINGLE_WAIT)

    def is_satisfied(self, division: Division, agari_info: AgariInfo) -> bool:
        return agari_info.wait_type == WaitEnum.SINGLE_WAIT
