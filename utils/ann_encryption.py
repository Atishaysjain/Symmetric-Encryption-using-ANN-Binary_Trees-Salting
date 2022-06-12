import numpy as np
import os
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential 
from tensorflow.keras import layers
from tensorflow.keras import initializers

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # This will not print tensorflow warnings

# Converts the input string from binary encryption to a numeric format
def get_ann_input(data_lvl2):
    
    data_ann = []

    for i in data_lvl2:

        if '*' in i:
            l = i.split('*')
            num = ord(l[0])
            num += 256*(len(l)-1)
            data_ann.append(num)

        else:
            data_ann.append(ord(i))
            
    return data_ann



# slices the numeric array into arrays such that they could be passed into the ANN, i.e into sub arrays with length equal to the number of nodes in the first layer of the ANN.
def slice_input(input_array, n):
    
    sliced_array = []
    
    if(len(input_array) > n):

        for i in range(0, int(len(input_array)/n)):
            
            sliced_array.append(input_array[n*i:n*(i+1)])
        
        i = int(len(input_array)/n)
        sliced_array.append(input_array[n*i:])
        
        while(len(sliced_array[-1]) < n):
            sliced_array[-1].append(-1)

    else:

        sliced_array.append(input_array)

        while(len(sliced_array[-1]) < n):
            sliced_array[0].append(-1)

        
    return sliced_array



# saves the path of the weights of the ANN for a given user with a unique user_id
def create_model_initial(n, user_id): # n represents the number of nodes in a layer of the ANN

    # print(user_id)
    layer = layers.Dense(
        units=64,
        kernel_initializer=initializers.RandomNormal(stddev=0.01),
        bias_initializer=initializers.Zeros()
    )  
    model = Sequential([
        layers.Dense(units = n, input_shape = (n,), kernel_initializer=initializers.RandomNormal(mean=0.4, stddev=1.0, seed=user_id*3)),
        layers.Dense(units = n, kernel_initializer=initializers.RandomNormal(mean=0.4, stddev=1.0, seed=user_id*3+1)), 
        layers.Dense(units = n, kernel_initializer=initializers.RandomNormal(mean=0.4, stddev=1.0, seed=user_id*3+2))
    ])
    
    model_path = os.path.join(os.getcwd(), 'weights', f"standard_encryption_weights_{user_id}.h5")
    # print(model_path)
    model.save(model_path)
    
    return model_path


# Returns the output after passing the encrypted string from binary encryption to the ANN
def get_predictions(model, sliced_array, n):
    
    lvl3 = []
    sliced_array = np.array(sliced_array)
    
    for array in sliced_array:
        
        predictions = model.predict(np.array(array).reshape(1,n))
        lvl3.append(predictions)
        
    return lvl3



