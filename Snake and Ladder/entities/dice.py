class dice:
    def __init__(self, faces):
        self.faces = faces

    def roll(self):
        import random
        number = random.randrange(1, self.faces+1)
        return number
