import random
from feedforward import feedforward
from mathhelper import sigmoid, derivsigmoid

l_rate = 0.2
epochs = 10000

input_data_set = [[0 ,0], [0, 1], [1, 0], [1, 1]]
output_data_set = [0,0,0,1]

def fit(data, output_data_set, learn_rate, epochs):

    weights = [[random.uniform(-1, 1) for _ in range(2)], [random.uniform(-1, 1) for _ in range(2)], [random.uniform(-1, 1) for _ in range(2)]]
    biases = [[random.uniform(-1, 1)], [random.uniform(-1, 1)], [random.uniform(-1, 1)]]

    for epoch in range(epochs):
        for i in range(len(data)):

            x = data[i]
            target = output_data_set[i]

            [0,0]
            [[0.4051257858555448, -0.5843519159246258], [0.703376365781059, -0.8848898688558118]]

            first_layer_output = feedforward(x, weights, biases)

            [0.8378112032793879, 0.3378112032793879]

            neuron1 = first_layer_output[0]
            neuron2 = first_layer_output[1]

            output = feedforward(first_layer_output, second_layer_weights, biases[2])
