# Main.py using polars and matplotlib to set data and see some plot

import polars as pl
import matplotlib.pyplot as plt

auto_df = pl.read_csv("Auto.csv", ignore_errors=True)
print(auto_df)


# Calculate mean, median, standard deviation of each columns
def calculate_stat():
    auto_desc = auto_df.describe()
    print(auto_desc)


calculate_stat()


# Make a boxplot of columns in Auto.csv
def build_boxplot():
    plt.hist(stat_df["AGE"], bins=10, color="blue", edgecolor="white")
    plt.xlabel("AGE")
    plt.ylabel("Frequency")
    plt.title("Age Histogram")
    plt.savefig("age_hist.png")
    plt.show()
    return


people()
create_hist()
