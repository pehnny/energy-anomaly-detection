from data import CleanData, FetchData, Save
from data.HouseholdElectricDataFrame import Columns
from analysis import Operation
from matplotlib import pyplot as plt

def main() :
    # Get Data
    data = Save.loadData()

    if data is None :
        data = FetchData.fetchData(100_000)

    data = CleanData.cleanData(data)
    print(data.head())

    # Analyse a subset for active power
    subset = data.loc["2007-03-01":"2007-03-15"]
    subset[Columns.GLOBAL_ACTIVE_POWER].plot(figsize=(12,5))
    plt.show(block=True)
    plt.close()

    # Analyse active power variation
    subset_diff = Operation.derivative(subset[Columns.GLOBAL_ACTIVE_POWER])
    subset_diff.plot(figsize=(12,5))
    plt.show(block=True)
    plt.close()

    # Distinguish regimes
    holiday = subset_diff.loc[:"2007-03-03"]
    normal = subset_diff.loc["2007-03-04":]
    regimes = [holiday, normal]

    # Look for anomalies
    for regime in regimes :
        treshold = regime.abs().quantile(0.995)
        anomalies = regime[regime.abs() > treshold]
        anomalies.plot(figsize=(12,5), style =".")
        plt.show(block=True)
        plt.close()

    Save.saveData(data)
    return

if __name__ == "__main__" :
    main()
