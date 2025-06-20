class Subsystem2:
    """
    Some facades can work with multiple subsystems at the same time.
    This subsystem provides different operations than Subsystem1.
    """

    def operation1(self) -> str:
        """Initial operation of subsystem 2"""
        return "Subsystem2: Get ready!"

    def operation_z(self) -> str:
        """Main operation of subsystem 2"""
        return "Subsystem2: Fire!"
