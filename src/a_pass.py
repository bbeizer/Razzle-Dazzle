class APass:
    def __init__(self, initial, final):
        self.initial = initial
        self.final = final

    def __eq__(self, other):
        return self.initial == other.initial and self.final == other.final

    def to_dict(self):
        return {
            "initial": self.initial.to_dict(),
            "final": self.final.to_dict()
        }
