import numpy as np

input_vector = np.array([1.72, 1.23])
weight_1 = np.array([1.26, 0])
weight_2 = np.array([2.17, 0.32])
bias = np.array([0.0])

def sigmoid(x): 
    return 1 / (1 + np.exp(-x))
    
def make_prediction(input_vector, weights, bias):
    layer_1 = np.dot(input_vector, weights)+bias
    layer_2 = sigmoid(layer_1)
    return layer_2
    
prediction1 = make_prediction(input_vector, weight_1, bias)
prediction2 = make_prediction(input_vector, weight_2, bias)


target = 0

mse = np.square(prediction1 - target)

mse = root(x^2)

x = (prediction1 - target)^2

sin(x^2)

u = sin(u)
du/dy = cos(u)

z = x^2 
dz/du = 2x

2x cos(x^2)

y = x^2

print(f"The prediction result for weight1: {prediction1}")
print(f"The prediction result for weight2: {prediction2}")
print(f"Mean Squared Error: {mse}")