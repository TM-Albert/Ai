def feedforward(x, weights, bias):
    w_sum = [[], []]

    for i in range(len(x)):
        for j in range(len(weights)):
            w_sum[i] = x[i] * weights[j]

        w_sum[i] += bias

    [0,0]
    [0.4051257858555448, -0.5843519159246258, 0.703376365781059, -0.8848898688558118]
    return w_sum
    