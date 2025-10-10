class animal:
    def __init__(self, al, ll, en, t, f):
        self.armLength = float(al)
        self.legLength = float(ll)
        self.eyeNumber = int(en)
        self.hasTail = bool(t)
        self.hasFur = bool(f)

    def printData(self):
        print(f"Arm Length: {self.armLength} cm.")
        print(f"Leg Length: {self.legLength} cm.")
        print(f"Number of Eyes: {self.eyeNumber} eyes.")
        if(self.hasTail):
            print("Has a tail.")
        else:
            print("Does not have a tail.")
        if(self.hasFur):
            print("Has fur.")
        else:
            print("Does not have fur.")

def main():
    dog = animal(20.0, 20.0, 2, 1, 1)

    dog.printData()

if __name__=="__main__":
	main()