class Animal:

    noise = "rrrr"

    def makeNoise(self):
        print(f"{self.noise}")

    def setNoise(self, newNoise):
        self.noise = newNoise



class Wolf(Animal):
    noise = "grrr"


class BabyWolf(Animal):
    noise = "prr"