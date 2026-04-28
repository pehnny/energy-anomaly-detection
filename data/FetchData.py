from ucimlrepo import fetch_ucirepo
from pandas import DataFrame
  
def fetchData(subset : int = 0, offset : int = 0) -> DataFrame :
    individual_household_electric = fetch_ucirepo(id=235)

    print(individual_household_electric.variables)

    dataset = individual_household_electric.data.features

    if subset == 0 :
        return dataset

    if offset == 0 :
        return dataset.head(subset)
    
    return dataset[offset:subset]
