class Apple:
    maturation_stages = ['bloom', 'green', 'red']
    
    def __init__(self, apple_id: int, maturation_stage=0):
        self.apple_id = apple_id
        self.maturation_stage = maturation_stage
    
    def grow(self):
        if self.maturation_stage < 2:
            self.maturation_stage += 1
    
    def info(self):
        if self.maturation_stage == 2:
            return True
        else:
            return False


class Tree:
    def __init__(self, *args):
        self.apples = [*args]
    
    def grow(self):
        for ap in self.apples:
            ap.grow()
    
    def info(self):
        if self.apples:
            for ap in self.apples:
                if not ap.info():
                    return False
                else:
                    continue
            return True
        else:
            print('There are no apples yet.')
    
    def harvest(self):
        self.apples.clear()


class Gardener:
    def __init__(self, name: str, *args):
        self.name = name
        self.trees = [*args]
    
    def care_plants(self):
        for tree in self.trees:
            tree.grow()
    
    def harvest(self):
        info = True
        for tree in self.trees:
            if not tree.info:
                info = False
                break
            else:
                continue
        if info:
            for tree in self.trees:
                tree.harvest()
        else:
            print("Not all apples are ready")
            

tree = Tree(*[Apple(i) for i in range(5)])
gard = Gardener('Ivan', tree)

while not tree.info():
    print(tree.info())
    gard.care_plants()
    
print(tree.info())
gard.harvest()
tree.info()
