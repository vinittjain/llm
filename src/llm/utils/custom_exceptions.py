import dataclasses


__all__ = ["ModelCheckpointNotFoundHandler", "InvalidTokenHandler"]


@dataclasses.dataclass
class ModelCheckpointNotFoundHandler(Exception):
    error: str

    def __post_init__(self):
        raise Exception(f"{self.error}")


@dataclasses.dataclass
class InvalidTokenHandler(Exception):
    error: str

    def __post_init__(self):
        raise Exception(f"{self.error}")
