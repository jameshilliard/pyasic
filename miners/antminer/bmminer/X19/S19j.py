from miners.bmminer import BMMiner


class BMMinerS19j(BMMiner):
    def __init__(self, ip: str) -> None:
        super().__init__(ip)
        self.api_type = "BMMiner"
        self.model = "S19j"
        self.nominal_chips = 114

    def __repr__(self) -> str:
        return f"BMMinerS19j: {str(self.ip)}"
