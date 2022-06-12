import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential 
from tensorflow.keras import layers
from tensorflow.keras import initializers

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # This will not print tensorflow warnings

def get_input_ann(model_path, lvl3, n):
    
    model = tf.keras.models.load_model(model_path)
    
    n_layers = len(model.layers)
    
    dependent_var = lvl3
    for i in range(1, n_layers+1):
        
        dependent_var = np.linalg.solve(model.layers[-i].get_weights()[0].T, dependent_var.reshape(n, 1))
        
    return dependent_var


# Returns the input sliced numeric array passed to the ANN as input
def decrypt_ann(model_path, n, lvl3):
    
    input_ann = []
    
    for prediction in lvl3:
        
        inp = get_input_ann(model_path, prediction, n)
        for i in range(0, len(inp)):
            if(inp[i][0]<0):
                inp[i][0] = -1
            else:
                inp[i][0] = int(inp[i][0]+0.5) 
        input_ann.append(inp)
        
    return input_ann


# Gets the output from the binary encryption
def get_lvl2(data_array):
    
    lvl2_decrypted = []
    
    for array in data_array:
                
        for i in array:
            
#             print(i)
            i = int(i)
            if(i == -1):
                break
            
            elif(i>256):
                n_star = int(i/256)
                stars = '*' * n_star
                char = chr(i%256)
                lvl2_decrypted.append(f'{char}{stars}')
            
            else:
                lvl2_decrypted.append(chr(i))
            
    lvl2_decrypted = np.array(lvl2_decrypted).reshape(-1)
    
    return lvl2_decrypted