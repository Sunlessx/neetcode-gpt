import numpy as np
import math
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        sigmoid_z = []
        for x in z:
            sigmoid_z.append(round(1/(1+math.exp(-x)), 5))
        print(sigmoid_z)
        return sigmoid_z

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        relu_z = []
        for x in z:
            relu_z.append(round(max(0.0, x),5))
        print(relu_z)
        return relu_z
