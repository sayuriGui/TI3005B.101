import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def Product_Clean(Odoo_Final):
    for j in range (len(Odoo_Final)):
        t = Odoo_Final['Líneas de factura/Producto'][j]
        if ( '- FUEGO AZTECA' in t):
            t.replace('- FUEGO AZTECA', '')
        for i in range(len(t)):
            if ( "["  in t) or ( "]"  in t):
                t.replace(t[i], '')
        if (t is not float ):
            Odoo_Final['Líneas de factura/Producto'][j] = t
    return Odoo_Final