import pandas as pnd
import matplotlib.pyplot as plt

from load_csv import load


def main():
    dfFrance = load("../life_expectancy_years.csv")

    print(dfFrance)
    # df = dfFrance.loc[dfFrance.country == 'France'].T
    # print(df.axes)
    # # plt.show()


if __name__ == "__main__":
    main()
