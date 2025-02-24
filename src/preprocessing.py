import pandas as pd

def mapping (data : list, columns : list, start = 0 : int, is_default = True : bool, default_value = -1 : int) :
    '''
    
    '''
    
    size = len(data)

    _map = {}
    
    for i in range (size) :
        _mape[columns[i]] = i + start

    if is_default :
        _map[columns[columns[size - 1]]] = default_value

    return data.map(_map)

