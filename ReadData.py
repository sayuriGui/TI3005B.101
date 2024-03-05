import pandas as pd
import numpy as np

def read_from_excel(ruta):

    """
        Input :
        files: A python list with the numbers of the files that will be read
        Output :
        result_data: A list of signal.Estimulo objects
    """
    filename =  ('c:/Users/sofia/OneDrive/Documents/FuegoAzteca/data/{}'.format(ruta))
    data = pd.read_excel(filename)

    return data