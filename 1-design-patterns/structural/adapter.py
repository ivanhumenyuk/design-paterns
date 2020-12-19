class Target:
    def request(self) -> str:
        return "Target: The default target's behavior."


class ToAdapt:
    def specific_request(self) -> int:
        return 123489845546456


class Adapter(Target, ToAdapt):
    def request(self) -> str:
        return f"Adapter: (mutate) --{str(self.specific_request())}--"


def client_code(target: Target) -> None:
    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = ToAdapt()
    print("Client: ToAdapt class give int value. "
          "I want to receive only string values!")
    print(f"ToAdapt: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)
