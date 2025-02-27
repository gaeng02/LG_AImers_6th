import pandas as pd

if (__name__ == "__main__") : 

    filepath = "" # setting
    df = pd.read_csv (filepath)

    print(df.columns)

    for col in df.columns :
        print(col)
        print(df[col].unique())
        print()

    
    # drop
    drop_columns = [] # setting 
    df = df.drop()


    # Nan.
    nan_columns = [] # setting
    for col in nan_columns : 
        df[col].fillna(-1, inplace = True)

    
    # mapping
    column = ""     # setting
    mapping = {     # setting
        "data1" : 0,
        "data2" : 1
        }
    df[column] = df[column].map(mapping)
