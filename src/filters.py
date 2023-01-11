import abc
from typing import Any


class IFilter:

    @abc.abstractmethod
    def filter(self, value, *args, **kwargs) -> Any:
        pass
