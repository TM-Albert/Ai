from mathhelper import sigmoid

def feedforward(x, weights, bias):
    w_sum = [0, 0]

    for i in range(len(x)):
        for j in range(len(weights)):
            w_sum[i] = x[i] * weights[j]

        w_sum[i] += bias

    for i in range(len(w_sum)):
        w_sum[i] = sigmoid(w_sum[i])

    [0,0]
    [0.4051257858555448, -0.5843519159246258, 0.703376365781059, -0.8848898688558118]
    return w_sum
