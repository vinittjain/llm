import dataclasses
from abc import ABCMeta, abstractmethod


__all__ = ["BaseConfig", "Llama"]


class BaseConfig(metaclass=ABCMeta):

    @abstractmethod
    def _init_config(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_config_type(self) -> str:
        raise NotImplementedError


@dataclasses.dataclass
class Llama(BaseConfig):

    def _init_config(self) -> None:
        pass

    def get_config_type(self) -> str:
        return "llama"
