import matplotlib.pyplot as plt
from load_csv import load


def main():
    """This program shows the projection of life expectency in relation to the
    gross national product of the year 1900 for each country
    """
    dfIncomes = \
        load("../income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    dfLifeExpectency = load("../life_expectancy_years.csv")

    # Get the values of year 1900 for each files
    incomes = dfIncomes['1900'].tolist()
    lifeExpectency = dfLifeExpectency['1900'].tolist()

    plt.title("1900")
    # Create the graph with incomes and lifExpectency of year 1900 in dots
    plt.plot(incomes, lifeExpectency, 'o')

    plt.xlabel("Gross domestic product")
    # Change scale of x axis to show values as logarithmic scale
    # This help to visualize the graph wich is  very large or have small values
    plt.xscale('log')
    # Give scale values and name to x axis
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])

    plt.ylabel("Life expectency")
    plt.show()


if __name__ == "__main__":
    main()
