class Sequence:
    def __init__(self, sequence=""):
        print("init")

    def get_weight(self):
        print("get_weight")

if __name__ == "__main__":
    sequence = Sequence("A")
    print(sequence.get_weight())