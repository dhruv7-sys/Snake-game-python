#concept_of_class_inheritence

class animals:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("exhale","inhale")

class fish(animals):
    def __init__(self):
        super(fish, self).__init__()

    def breathe(self):
        super(fish, self).breathe()
        print("doing this underwater")


    def swim(self):
        print(" Dory is moving in water")

dory = fish()
dory.swim()
dory.breathe()
print(dory.num_eyes)