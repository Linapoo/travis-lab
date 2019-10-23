class Sequence:

    WEIGHTS = {'A': 131.2, 'C': 289.2, 'G': 329.2, 'T': 304.2}

    def __init__(self, sequence=""):
        self._nucleotides = sequence.upper()
    
    @property
    def nucleotides(self):
        return self._nucleotides

    def get_weight(self):
        return Sequence.WEIGHTS[self.nucleotides]

if __name__ == "__main__":
    sequence = Sequence("a")
    print(sequence.get_weight())