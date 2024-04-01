import numpy as np

input_vector = np.array([1.0, 0.5])
weights = np.array([2.01, 2.57])
bias = 1.5
target = 1.0

def sigmoid(x):
        return 1/(1+np.exp(-x));
def make_prediction(input_vector, weights, bias):
        layer_1 = np.dot(input_vector, weights) + bias;
        layer_2 = sigmoid(layer_1)
        return round(layer_2, 5)
def sigmoid_deriv(x):
        return sigmoid(x) * (1-sigmoid(x))

prediction = make_prediction(input_vector, weights, bias)
mse = (prediction - target)**2
print(f"Prediction: {prediction} error: {mse}")

for i in range(10000):
        derror_dprediction = 2 * (prediction - target)
        layer_1 = np.dot(input_vector, weights) + bias
        dprediction_dlayer1 = sigmoid_deriv(layer_1)
        dlayer1_dbias = 1.0
        dlayer1_dweights = 1.0
        derror_dbias = derror_dprediction * dprediction_dlayer1 * dlayer1_dbias
        derror_dweights = derror_dprediction * dprediction_dlayer1 * dlayer1_dweights
        bias -= derror_dbias
        weights -= derror_dweights
        prediction = make_prediction(input_vector, weights, bias)
        mse = (prediction - target)**2
        print(f"Prediction: {prediction} error: {mse}")
print(f"Weights: {weights} Bias: {bias}")
print("Done")