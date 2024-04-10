import matplotlib.pyplot as plt
from load_csv import load


def main():
    dataFrame = load("../life_expectancy_years.csv")

	# Get values from dataFrame where country is 'France'
    franceData = dataFrame.loc[dataFrame.country == 'France']

    # Retrieve all columns values that is the years except de first one
    # which refers to 'country'
    tableYears = franceData.columns[1:]
    # Retrieve the datas of each columns of the dataset
    # .values[0][1:] means taking all elements of the first table except
    # the first one which is 'France'
    tableDatas = franceData.values[0][1:]

    plt.plot(tableYears, tableDatas)
    plt.title("France Life expectancy Projections")

    plt.xlabel("Year")
    # Give copy of years table to xticks function by slicing with step 40
    plt.xticks(tableYears[::40])

    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()
