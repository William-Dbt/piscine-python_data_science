import matplotlib.pyplot as plt
from load_csv import load


def popStringToFloat(popStr: str) -> float:
    """This function will take the args from the dataset expressed as 'X M'
    Where X is a number and M is the letter for Million

    Args:
        popStr (str): Arg to convert

    Returns:
        float: float of the convertion
    """
    return float(popStr.replace('M', '')) * 1e6


def main():
    """Display country information of France and Belgium
    from population_total.csv file
    """
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
    plt.plot(tableYears, belgiumDatas, label="Belgium", color="skyblue")
    plt.plot(tableYears, franceDatas, label="France", color="green")

    plt.xlabel("Year")
    plt.xticks(range(1800, 2050, 40))
    plt.xlim(1800, 2050)

    plt.ylabel("Population")
    # Define values to take care of and how values have to be printed
    yTicks = [20.0 * 1e6, 40.0 * 1e6, 60.0 * 1e6]
    plt.yticks(yTicks,
               ["{:,.0f}M".format(popNumber / 1e6) for popNumber in yTicks])

    plt.legend(loc="lower right")
    plt.show()


if __name__ == "__main__":
    main()
