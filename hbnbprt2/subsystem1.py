class Subsystem1:
    """
    The Subsystem can accept requests either from the facade or client directly.
    In any case, to the Subsystem, the Facade is yet another client, and it's
    not a part of the Subsystem.
    """

    def operation1(self) -> str:
        """Initial operation of subsystem 1"""
        return "Subsystem1: Ready!"

    def operation_n(self) -> str:
        """Main operation of subsystem 1"""
        return "Subsystem1: Go!"
