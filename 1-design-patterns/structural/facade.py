from __future__ import annotations


class NewFacade:
    def __init__(self, subsystem_1: Subsystem_1, subsystem_2: Subsystem_2) -> None:

        self._subsystem_1 = subsystem_1 or Subsystem_1()
        self._subsystem_2 = subsystem_2 or Subsystem_2()

    def operation(self) -> str:

        results = []
        results.append("Facade initializes subsystems:")
        results.append('-----------------------------------------')
        results.append("Ordering subsystems to perform the action:")
        results.append(self._subsystem_1.operation_1())
        results.append(self._subsystem_2.operation_1())
        results.append(self._subsystem_1.operation_x())
        results.append(self._subsystem_2.operation_x())
        return "\n".join(results)


class Subsystem_1:
    @staticmethod
    def operation_1() -> str:
        return "Start operation '1' in Subsystem 1"

    @staticmethod
    def operation_x() -> str:
        return "Start operation 'X' in Subsystem 1"


class Subsystem_2:
    @staticmethod
    def operation_1() -> str:
        return "Start operation '1' in Subsystem 2"

    @staticmethod
    def operation_x() -> str:
        return "Start operation 'X' in Subsystem 2"


def client_code(facade: NewFacade) -> None:
    print(facade.operation())


if __name__ == "__main__":
    subsystem_1 = Subsystem_1()
    subsystem_2 = Subsystem_2()
    facade = NewFacade(subsystem_1, subsystem_2)
    client_code(facade)
