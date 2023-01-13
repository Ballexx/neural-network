import json
import numpy as np

class NeuralNetwork:
    def __init__(self):
        self.node_count = 300
        self.output_count = 5
        self.input_bias = []
        self.layer_bias = []

    def generate_bias(self, bias_amount, bias):
        for _ in range(bias_amount):
            bias.append(0)

        return bias

    def feedforward(self, node_count, parent_node_count, values, weights, biases):

        node_val = 0
        node_final_value = []

        for parent_node in range(parent_node_count):
            for child_node in range(node_count):
                wx = values[child_node] * weights[parent_node][child_node]
                node_val += wx

            node_final_value.append(node_val - biases[parent_node])
            node_val = 0

        return node_final_value

    def sigmoid(self, items):
        sigmoid_list = []

        for i in range(len(items)):
            sigmoid_list.append(1 / (1 + np.exp(-items[i])))

        return sigmoid_list

    def calculate(self, input_vals):

        input_nodes = len(input_vals)

        input_bias = self.generate_bias(input_nodes, self.input_bias)
        layer_bias = self.generate_bias(self.node_count, self.layer_bias)

        with open("data.json") as file:
            data = json.loads(file.read())
            input_weights = data[0]["input_weights"]
            layer_weights = data[1]["layer_weights"]

        hidden_layer_values = self.feedforward(625, 300, input_vals, input_weights, input_bias)
        output_values = self.feedforward(300, self.output_count, hidden_layer_values, layer_weights, layer_bias)

        print(self.sigmoid(output_values))
