from abc import ABC
from dataclasses import dataclass

from src.common.converters.base import BaseConverter


@dataclass
class BaseService(ABC):
    converter: BaseConverter
