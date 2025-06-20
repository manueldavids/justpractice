from facade import Facade
from subsystem1 import Subsystem1
from subsystem2 import Subsystem2

def client_code(facade: Facade) -> None:
    """
    The client code works with complex subsystems through a simple iterface
    provided by the Facade. When a facade manages the lifecycle of the
    subsystem, the client might not even know about the existence of the
    subsystem. This approach lets you keep the complexity under control.
    """
    print(facade.operation(), end="")

if __name__ == "__main__":
    # The client code may have some of tthe subsystem's objects already created.
    # In this case, it might be worthwhile to initialize the Facade with these
    # objects instead of letting the Facade create new instances>
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)

