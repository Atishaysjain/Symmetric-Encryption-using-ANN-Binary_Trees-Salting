import os
import copy
import tensorflow as tf
import numpy as np
import argparse as ap

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # This will not print tensorflow warnings


from utils import ann_decryption  
from utils import ann_encryption  
from utils import binary_tree 
from utils import interleaving

parser = ap.ArgumentParser()

parser.add_argument("-input", "--input_data", type = str, help = "String to be encrypted and decrypted", default = "Hey! I love Machine Learning")

parser.add_argument("-s", "--salt", type = str, help = "salt used for encryption", default = "123456789")

parser.add_argument("-u", "--user_id", type = int, help = "User Id of the user, unique for each user", default = 1)

arguments = parser.parse_args()



def encrypt(input_data, salt, n, user_id): # n represents the number of nodes in the layer of the ANN
    
    # Interleaving salt and input data
    lvl1 = interleaving.interleave(input_data, salt)
    
    # Binary Tree encryption
    inorder, preorder = binary_tree.encrypt_binary_tree(lvl1)

    inorder_lvl2, preorder_lvl2 = copy.deepcopy(inorder), copy.deepcopy(preorder)
    
    # ANN encryption
    # Converts the input string from binary encryption to a numeric format
    inorder_ann = ann_encryption.get_ann_input(data_lvl2 = inorder_lvl2)
    preorder_ann = ann_encryption.get_ann_input(data_lvl2 = preorder_lvl2)

    # slices the numeric array into arrays such that they could be passed into the ANN, i.e into sub arrays with length equal to the number of nodes in the first layer of the ANN.
    inorder_ann_sliced = ann_encryption.slice_input(inorder_ann, n)
    preorder_ann_sliced = ann_encryption.slice_input(preorder_ann, n)

    # saves the path of the weights of the ANN for a given user with a unique user_id
    # model_path = os.path.join(os.getcwd(), 'weights', f"standard_encryption_weights_{user_id}.h5")
    # is_exists = os.path.exists(model_path)
    # if not is_exists:
    model_path = ann_encryption.create_model_initial(n, user_id)

    # Extracting weights
    model = tf.keras.models.load_model(model_path)

    # Returns the output after passing the encrypted string from binary encryption to the ANN
    lvl3_inorder = ann_encryption.get_predictions(model, inorder_ann_sliced, n)
    lvl3_preorder = ann_encryption.get_predictions(model, preorder_ann_sliced, n)

    encrypted_value = np.concatenate((lvl3_inorder, lvl3_preorder))

    return encrypted_value



def decrypt(encrypted_value, n, user_id): # n represents the number of nodes in the layer of the ANN
    
    # Getting encrypted inorder and encrypter preorder
    mid_index = int(len(encrypted_value)/2)
    lvl3_inorder, lvl3_preorder = encrypted_value[:mid_index], encrypted_value[mid_index:]

    # Getting the model weights for a given user
    model_path = os.path.join(os.getcwd(), 'weights', f"standard_encryption_weights_{user_id}.h5")

    # Returns the input sliced numeric array passed to the ANN as input
    inorder_ann_input = ann_decryption.decrypt_ann(model_path, n, lvl3 = lvl3_inorder)
    preorder_ann_input = ann_decryption.decrypt_ann(model_path, n, lvl3 = lvl3_preorder)

    # Gets the output from the binary encryption
    inorder_lvl2_decrypted = ann_decryption.get_lvl2(inorder_ann_input)
    preorder_lvl2_decrypted = ann_decryption.get_lvl2(preorder_ann_input)
    

    # Binary Tree decryption
    lvl1 = binary_tree.decrypt_binary_tree(inorder_lvl2_decrypted, preorder_lvl2_decrypted)
    
    # Getting salt and input data from the interleaved Binary Tree decrypted value
    input_array, salt = interleaving.decrypt_interleave(interleaved_data = lvl1)
    
    decrypted_value = ''
    for s in input_array:
        decrypted_value += s
    
    return decrypted_value



if __name__ == '__main__':

    input_data = arguments.input_data
    salt = arguments.salt
    user_id = arguments.user_id

    n_nodes = 16 # Number of nodes in a layer of the Artificial Neural Network

    # Encryption Code
    inorder = []
    preorder = []
    encrypted_value = encrypt(input_data, salt, n = n_nodes, user_id = user_id)
    print(f"The encrypted value is:\n {encrypted_value}")


    # Decryption Code
    decrypted_value = decrypt(encrypted_value, n = n_nodes, user_id = user_id)
    print(f"The decrypted value is: {decrypted_value}")

    if(input_data == decrypted_value):
        print("SUCCESS!!")


    