import dataclasses
from abc import ABCMeta, abstractmethod


__all__ = ["BaseInference", "LlamaInference"]


class BaseInference(metaclass=ABCMeta):

    @abstractmethod
    def _init_config(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_config_type(self) -> str:
        raise NotImplementedError


@dataclasses.dataclass
class LlamaInference(BaseConfig):

    def _init_config(self) -> None:
        pass

    def get_config_type(self) -> str:
        return "llama_inference"
