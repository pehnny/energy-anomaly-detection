from pandas import DataFrame, read_parquet
from pathlib import Path
from typing import Optional

path_to_save = Path(__file__).parent.joinpath('household_electric_consumption.parquet')

def saveData(data : DataFrame, overwrite : bool = False) -> bool :
    if not overwrite and path_to_save.is_file() :
        return False

    data.to_parquet(path_to_save)

    return True

def loadData() -> Optional[DataFrame] :
    if not path_to_save.is_file() :
        return
    
    return read_parquet(path_to_save)
