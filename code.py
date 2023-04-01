from funciones import crear_listado_dic, dataframe_final, creacion_graficos
import pandas as pd
import os

class graphs_execution():

    def primitiva_code():

        print('Your code is being executed (downloading...)')

        try:
            outdir = './graphs'

            if not os.path.exists(outdir):
                os.mkdir(outdir)

            df_primitiva = pd.read_csv('Dataset_primitiva.csv', index_col = 'FECHA')

            listado_diccionarios = crear_listado_dic(df_primitiva, porcentual='Si')

            df_final = dataframe_final(listado_diccionarios, df_primitiva.index)

            creacion_graficos(listado_diccionarios, df_final)

            print("Executed succesfully, go and check it!")

        except:
            'Something went wrong, check your code!'
