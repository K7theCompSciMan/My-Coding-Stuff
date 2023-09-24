import numpy as np
class NeuralNetwork:
        def __init__(self, learning_rate):
                self.weights = np.array([np.random.randn(), np.random.random()])
                self.bias = np.random.randn()
                self.learning_rate = learning_rate
        
        def sigmoid(self, x):
                return 1/(1+np.exp(-x))
        
        def sigmoid_deriv(self, x):
                return self.sigmoid(x) * (1-self.sigmoid(x))
        
        def predict(self, input_vector):
                layer_1 = np.dot(input_vector, self.weights) + self.bias
                layer_2 = self.sigmoid(layer_1)
                return layer_2
        
        def compute_gradients(self, input_vector, target):
                layer_1 = np.dot(input_vector, self.weights) + self.bias
                layer_2 = self.sigmoid(layer_1)
                prediction = layer_2

                derror_dprediction = 2 * (prediction - target)
                dprediction_dlayer1 = self.sigmoid_deriv(layer_1)

                dlayer1_dbias = 1.0
                dlayer1_dweights = (0* self.weights) + (1 * input_vector)

                derror_dbias = derror_dprediction * dprediction_dlayer1 * dlayer1_dbias
                derror_dweights = derror_dprediction * dprediction_dlayer1 * dlayer1_dweights
                return derror_dbias, derror_dweights
        
        def update_values(self, derror_dbias, derror_dweights):
                self.bias -= derror_dbias * self.learning_rate
                self.weights -= derror_dweights * self.learning_rate

        def train(self, input_vectors, targets, iterations):
                cumulative_errors = []
                for i in range(iterations):
                        random_data_index = np.random.randint(len(input_vectors))

                        input_vector = input_vectors[random_data_index]
                        target = targets[random_data_index]
                        derror_dbias, derror_dweights = self.compute_gradients(input_vector, target)

                        self.update_values(derror_dbias, derror_dweights)
                        
                        if i % 100 == 0:
                                cumulative_error = 0

                                for j in range(len(input_vectors)):
                                        data_point = input_vectors[j]
                                        target = targets[j]

                                        prediction = self.predict(data_point)
                                        error = (prediction-target)**2
                                        cumulative_error += error
                                cumulative_errors.append(cumulative_error)

                return cumulative_errors