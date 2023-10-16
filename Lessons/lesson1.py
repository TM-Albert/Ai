import random
from feedforward import feedforward
from mathhelper import sigmoid, derivsigmoid

l_rate = 0.2
epochs = 10000

input_data_set = [[0 ,0], [0, 1], [1, 0], [1, 1]]
output_data_set = [0,0,0,1]

def fit(data, y, learn_rate, epochs):

    weights = [[random.uniform(-1, 1) for _ in range(2)], [random.uniform(-1, 1) for _ in range(2)]]
    biases = [[random.uniform(-1, 1)], [random.uniform(-1, 1)]]

    for epoch in range(epochs):
        for i in range(len(input_data_set)):

            x = input_data_set[i]
            target = output_data_set[i]

            [0,0]
            [0.4051257858555448, -0.5843519159246258, 0.703376365781059, -0.8848898688558118]

            calculated_output = feedforward(x, weights, biases)

            


