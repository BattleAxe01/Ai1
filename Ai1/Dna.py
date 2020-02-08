class Dna:
    s = ""
    fitness = -1

    def __init__(self, s):
        self.s = s

    def __repr__(self) -> str:
        return self.s

