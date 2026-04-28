from data import CleanData, FetchData, Save

def main() :
    data = Save.loadData()

    if data is None :
        data = FetchData.fetchData(100_000)

    data = CleanData.cleanData(data)

    Save.saveData(data, True)
    return

if __name__ == "__main__" :
    main()
