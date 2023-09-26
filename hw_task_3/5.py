from random import random, randint


class Apple:
    maturation_stages = ['bloom', 'green', 'red']

    def __init__(self, apple_id: int, maturation_stage=0):
        self.apple_id = apple_id
        self.maturation_stage = maturation_stage

    def grow(self):
        self.maturation_stage += 1

    def info(self):
        if self.maturation_stage >= 2:
            # print(self.maturation_stages[-1])
            return True
        else:
            # print(self.maturation_stages[self.maturation_stage])
            return False


class Tree:

    __p = 0.5  # probability of growing new apples
    __max_new_apples = 5  # how many apples can grow randomly on tree

    def __init__(self, *args, age=1):
        self.age = age
        if self.age <= 1:
            self.apples, self.__apple_id_list = [], []
            print('The tree is too young to have apples. Created tree without apples.')
        else:
            self.apples = [*args]
            self.__apple_id_list = [apple.apple_id for apple in self.apples]

    def __add_apple(self, apple: Apple):
        self.apples.append(apple)

    def grow(self):
        self.age += 1

        if self.age == 10:
            self.apples.clear()

        if self.age > 1:
            i = 0
            while i < len(self.apples):
                self.apples[i].grow()
                if self.apples[i].maturation_stage > 4:
                    self.apples.remove(self.apples[i])
                else:
                    i += 1

        if self.age in range(2, 5):
            if random() < self.__p:
                for i in range(randint(1, self.__max_new_apples)-1):
                    if self.__apple_id_list:
                        new_apple_id = max(self.__apple_id_list) + 1
                    else:
                        new_apple_id = 0
                    self.__add_apple(Apple(new_apple_id))
                    self.__apple_id_list.append(new_apple_id)

    def info(self):
        if self.apples:
            for ap in self.apples:
                if not ap.info():
                    return False
                else:
                    continue
            return True
        else:
            print("There are no apples yet! Return back later.")

    def full_info(self):
        tree_info = [(k, v) for k, v in zip([apple.apple_id for apple in self.apples],
                                            [apple.maturation_stage for apple in self.apples])]
        return tree_info

    def harvest(self):
        if self.apples:
            count = 0
            i = 0
            while i < len(self.apples):
                if self.apples[i].maturation_stage >= 2:
                    self.__apple_id_list.remove(self.apples[i].apple_id)
                    self.apples.remove(self.apples[i])
                    count += 1
                else:
                    i += 1
            if count == 0:
                print("There are no matured apples yet! Return back later.")
            else:
                print(f"You've collected {count} apples")
        else:
            print("There are no apples yet! Return back later.")

    def __len__(self):
        return len(self.apples)


class Gardener:
    def __init__(self, name: str, *args):
        self.name = name
        self.trees = [*args]

    def care_plants(self):
        for tree in self.trees:
            tree.grow()

    def harvest(self):
        if self.trees:
            for tree in self.trees:
                tree.harvest()
        else:
            print("There are no trees in the garden!")

    def garden_stats(self):
        trees_age = {}
        apples_stats = {'bloom': 0, 'green': 0, 'red': 0}
        apples_count = 0
        i = 1
        for tree in self.trees:
            apples_count += len(tree)
            trees_age[f'Tree {i}'] = tree.age
            i += 1
            for apple in tree.apples:
                if apple.maturation_stage == 0:
                    apples_stats['bloom'] += 1
                elif apple.maturation_stage == 1:
                    apples_stats['green'] += 1
                else:
                    apples_stats['red'] += 1
        print(f'Number of trees: {len(trees_age)}')
        print(f'Trees age: {trees_age}')
        print(f'Number of apples: {apples_count}')
        print(f'Apples stages: {apples_stats}')


tree_1 = Tree(*[Apple(i) for i in range(6)], age=2)
gard = Gardener('Ivan', tree_1)

print(tree_1.full_info())
gard.care_plants()
print(tree_1.full_info())
print('------------------')

print(tree_1.full_info())
gard.care_plants()
print(tree_1.full_info())
print('------------------')

print(tree_1.full_info())
gard.care_plants()
print(tree_1.full_info())
print('------------------')

print(tree_1.full_info())
gard.care_plants()
print(tree_1.full_info())
print('------------------')

print(tree_1.full_info())
gard.care_plants()
print(tree_1.full_info())
print('------------------')

gard.garden_stats()
