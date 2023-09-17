# Main.py using polars and matplotlib to set data and see some plot

import polars as pl
import matplotlib.pyplot as plt

stat_df = pl.read_csv("Statistics_Test.csv")


# Mean, Median, Standard Deviation
def people():
    age = stat_df["AGE"]
    age_mean = age.mean()
    age_median = age.median()
    age_std = age.std()
    print(f"Mean = {age_mean}, Median = {age_median}, Standard Deviation = {age_std}")
    return


# Count columns for test
def count_col():
    num_col = len(stat_df.columns)
    return num_col


# Count rows for test
def count_row():
    num_row = len(stat_df)
    return num_row


# Make a plot to Histogram of Age column
def create_hist():
    plt.hist(stat_df["AGE"], bins=10, color="blue", edgecolor="white")
    plt.xlabel("AGE")
    plt.ylabel("Frequency")
    plt.title("Age Histogram")
    plt.savefig("age_hist.png")
    plt.show()
    return


people()
create_hist()
