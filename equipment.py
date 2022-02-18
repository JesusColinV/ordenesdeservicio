from db import *
import pandas as pd
import os

class OrdenDeServicio():
    def __init__(self):
        self.path='./'
        self.FileName='Equipo2022'
        self.FullTable = 'OrdenesDeServicio'

    def create(self):
        '''
        we confirm that the table has not been created
        '''
        if self.FileName in os.listdir(self.path):
            df = pd.read_excel(self.FileName)
        else:
            df = pd.DataFrame({i:[] for i in equipment})
        return df
        
Orden = OrdenDeServicio()
Orden.create()