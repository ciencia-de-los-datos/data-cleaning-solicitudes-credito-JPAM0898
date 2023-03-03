"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada correctamente. Tenga en cuenta datos faltantes y duplicados.
"""
import pandas as pd

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col=0)
    
    # Everything to lowercase 
    df['sexo'] = df['sexo'].str.lower()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower()
    df['idea_negocio'] = df['idea_negocio'].str.lower()
    df['barrio'] = df['barrio'].str.lower()
    df['línea_credito'] = df['línea_credito'].str.lower()
     
    # Whitespaces, hyphen and underscore checks
    df['idea_negocio'] = df['idea_negocio'].replace({'-':' ','_':' '}).str.strip()
    df['barrio'] = df['barrio'].replace({'-':' ','_':' '}).str.strip()
    df['línea_credito'] = df['línea_credito'].replace({'-':' ','_':' '}).str.strip()
    
    # Date checks   
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'],dayfirst=True)
    
    # Money checks
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',','').str.replace('$','').str.strip().astype(float)
    
    df.drop_duplicates(inplace=True)
    df.dropna(axis='index',inplace=True)
    df.reset_index(inplace=True,drop=True)

    return df
