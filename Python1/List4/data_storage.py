import numpy as np
num_inputs = 5
input_states = np.zeros(num_inputs, dtype=np.int8)  
input_states[0] = 1
input_states[1] = 1
input_states[2] = 0
input_states[3] = 1
input_states[4] = 0
print("Current input states:", input_states)
