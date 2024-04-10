import matplotlib.pyplot as plt
from load_csv import load


def popStringToFloat(popStr: str):
    return float(popStr.replace('M', '')) * 1e6


def main():
    dataFrame = load("../population_total.csv")

    franceData = dataFrame.loc[dataFrame.country == 'France']
    belgiumData = dataFrame.loc[dataFrame.country == 'Belgium']

    tableYears = franceData.columns[1:].astype(int)

    franceDatas = franceData.values[0][1:]
    belgiumDatas = belgiumData.values[0][1:]

    # Convert all datas from string to float
    franceDatas = [popStringToFloat(pop) for pop in franceDatas]
    belgiumDatas = [popStringToFloat(pop) for pop in belgiumDatas]

    plt.title("Population Projections")
    plt.plot(tableYears, franceDatas, label="France", color="green")
    plt.plot(tableYears, belgiumDatas, label="Belgium", color="skyblue")

    plt.xlabel("Year")
    plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
    plt.xlim(1800, 2040)

    plt.ylabel("Population")
    # plt.yticks([20, 40, 60])
    # TODO: Work on y label

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
