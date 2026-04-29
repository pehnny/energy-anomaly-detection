from pandas import Series

def derivative(data : Series) -> Series :
    return data.diff()
