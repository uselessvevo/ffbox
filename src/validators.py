import abc


class IValidator:

    @abc.abstractmethod
    def validate(self) -> None:
        pass
