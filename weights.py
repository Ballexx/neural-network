import random

def generate_weight(generate_length):
    weights = []
    for i in range(generate_length):
        weight = random.randrange(-1000, 1000) / 1000
        weights.append(weight)

    return weights

weights = []

for i in range(5):
    weights.append(generate_weight(300))


with open("data.json", "a") as outfile:
    outfile.write(f"layer_weights: {str(weights)}")