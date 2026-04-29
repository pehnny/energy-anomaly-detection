from pandas import DataFrame, to_datetime, to_numeric
from data.HouseholdElectricDataFrame import Columns

def _insertDatetime(data : DataFrame) -> DataFrame :
    'Ajoute la colonne datetime à partir des colonnes date et time.'
    'Envoie le dataset si la colonne datetime existe déjà.'
    'Défini la colonne Datetime comme index du dataset.'
    if data.index.name == "Datetime" :
        return data
    
    data["Datetime"] = to_datetime(data["Date"] + " " + data["Time"], format=r"%d/%m/%Y %H:%M:%S")
    data = data.set_index("Datetime").sort_index()
    return data

def _dropDate(data : DataFrame) -> DataFrame :
    'Retire la colonne Date.'
    if "Date" in data :
        data = data.drop(columns="Date")
    return data

def _dropTime(data : DataFrame) -> DataFrame :
    'Retire la colonne Date.'
    if "Time" in data :
        data = data.drop(columns="Time")
    return data

def _convertDateTime(data : DataFrame) -> DataFrame :
    'Converti les colonnes Date et Time en une seule colonne Datetime au format Timestamp.'
    'Défini la colonne Datetime comme index du dataset.'
    data = _insertDatetime(data)
    data = _dropDate(data)
    data = _dropTime(data)
    return data

def _convertDtypeToFloat(data : DataFrame) -> DataFrame :
    'Converti les données en type numpy f64. Les données manquantes sont converties en NaN.'
    'Retourne le dataset si les types sont déjà correct.'
    isFloat64 = True
    for dtype in data.dtypes :
        if dtype != "float64" :
            isFloat64 = False
    
    if isFloat64 :
        return data

    for col in data.columns :
        data[col] = to_numeric(data[col], errors="coerce")
    return data

def cleanData(data : DataFrame) -> DataFrame :
    'Nettoie les données.'
    data = _convertDateTime(data)
    data = _convertDtypeToFloat(data)
    return data
