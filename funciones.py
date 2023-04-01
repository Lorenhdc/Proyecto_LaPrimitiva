import pandas as pd

def crear_dic_primitiva():
    # Creamos un diccionario vacío con los números de la primitiva
    dic_primitiva = dict()
    for i in range(49):
        dic_primitiva[i+1] = 0
    return dic_primitiva

def crear_listado_dic(dataframe, porcentual):
    # Creamos diccionarios vacíos para completar
    dic_primitiva_porcentajes = crear_dic_primitiva()
    dic_primitiva = crear_dic_primitiva()

    lista_dictionarios = []

    sorteos = 0
    
    # Recorremos el dataframe y coleccionamos el número de veces que ocurre cada valor
    for i in range(len(dataframe)):
        sorteos += 1
        primer_numero = dataframe.iloc[i,0]
        segundo_numero = dataframe.iloc[i,1]
        tercer_numero = dataframe.iloc[i,2]
        cuarto_numero = dataframe.iloc[i,3]
        quinto_numero = dataframe.iloc[i,4]
        sexto_numero = dataframe.iloc[i,5]
        dic_primitiva[primer_numero] = dic_primitiva[primer_numero] + 1
        dic_primitiva[segundo_numero] = dic_primitiva[segundo_numero] + 1
        dic_primitiva[tercer_numero] = dic_primitiva[tercer_numero] + 1
        dic_primitiva[cuarto_numero] = dic_primitiva[cuarto_numero] + 1
        dic_primitiva[quinto_numero] = dic_primitiva[quinto_numero] + 1
        dic_primitiva[sexto_numero] = dic_primitiva[sexto_numero] + 1
        # Diferenciamos entre diccionario absoluto o porcentual
        if porcentual == 'Si':
            for numero in range(49):
                numero = numero+1
                dic_primitiva_porcentajes[numero] = round((dic_primitiva[numero]/sorteos)*100,4)
            lista_dictionarios.append(dic_primitiva_porcentajes.copy())
        else:
            lista_dictionarios.append(dic_primitiva.copy())

    
    return lista_dictionarios


def dataframe_final(listado, indice_df):
    # Creamos el diccionario_ultimate y modificamos ciertos campos a los cuales vamos a hacer uso
    dic_meses = {'01':'Jan', '02':'Feb', '03':'Mar', '04':'Apr', '05':'May', '06':'Jun', '07':'Jul', '08':'Aug', '09':'Sep', '10':'Oct', '11':'Nov', '12':'Dec'}
    df = pd.DataFrame(listado, index=indice_df)
    df['Fecha'] = pd.to_datetime(df.index, format = '%Y-%m-%d')
    df['Weekday'] = df['Fecha'].dt.weekday
    df['mes'] = df.index.astype(str).str[5:7]
    df.replace({'mes':dic_meses}, inplace=True)
    df['anio'] = df.index.astype(str).str[:4]
    df['Titulo']= df['mes'] + ' ' + df['anio']
    del df['Fecha'], df['mes'], df['anio']
    return df


def creacion_graficos(listados, df):
    import matplotlib.pyplot as plt; plt.rcdefaults()
    import numpy as np
    import matplotlib.pyplot as plt
    import numpy as np
    plt.rcParams["figure.figsize"] = (15,10)

    numero = 0

    for i in range(len(listados)):
        # Cuando la columna weekday == 3 (martes)
        if df.iloc[i,-2]==3:
            numero = numero + 1
            # Cada 4 martes (un mes), imprimimos la imagen a esa fecha  y lo guardamos en la carpeta que creamos 'graphs'. 
            if numero%4 == 0 or numero == 1: 
                data = listados[i]
                objects = data.keys()
                y_pos = np.arange(len(objects))
                performance_bar = data.values()
                performance_line = [12.24 for i in range(49)]
                rects1 = plt.bar(y_pos, performance_bar, align='center', alpha=0.95, label = 'Events (%)')
                line2 = plt.plot(y_pos, performance_line , linestyle='-', alpha=1, color='r', label='Expected events (%)')
                mes = df.iloc[i,-1]
                plt.xlim([-1, 50])
                plt.ylim([0, 0.5])
                plt.yticks([10, 20, 30, 40, 50], fontsize = 12)
                plt.xticks(y_pos, objects, fontsize=10)
                plt.title(mes,fontsize=18)
                plt.ylabel('%', fontsize=12)
                plt.legend(loc=1, prop={'size': 14})
                plt.savefig(f'graphs/{i}picture.png')
                #plt.show()
                plt.clf()