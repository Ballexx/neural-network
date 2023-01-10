import random

class neuralnetwork:

    def generate_weight(self, input):
        weight_list = []
        for i in range(len(input)):
            weight = random.randrange(-1000, 1000)/1000
            weight_list.append(weight)

        return weight_list

    def calculate(self, input):
        weights = self.generate_weight(input)

        for i in range(len(input)):
            for j in range(len(weights)):
                pass


