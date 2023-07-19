from abc import ABC, abstractmethod

from common import YakuEnum
from agari_info import AgariInfo
from division import Division


class YakuMixin:
    def __init__(self, yaku: YakuEnum):
        self.yaku = yaku


class BaseYaku(ABC, YakuMixin):
    @abstractmethod
    def is_satisfied(self, division: Division, agari_info: AgariInfo) -> bool:
        pass