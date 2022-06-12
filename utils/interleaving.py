import copy

def interleave(data1, data2):
    
    original_data2 = copy.deepcopy(data2)
    
    while(len(data2) < len(data1)):
        data2 += original_data2
    
    lvl1 = [''] * len(data1) * 2 
    lvl1[::2] = data1[:len(data1)]
    lvl1[1::2] = data2[:len(data1)]
    
    return lvl1

def decrypt_interleave(interleaved_data):
    
    data1 = interleaved_data[::2]
    data2 = interleaved_data[1::2]
    
    return data1, data2