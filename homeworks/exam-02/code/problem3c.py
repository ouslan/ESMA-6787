import pandas as pd
import statsmodels.formula.api as smf


def main():
    data = {
        "Programmer": [1, 2, 3, 4, 5, 6],
        "Stat_New": [3.1, 3.8, 3.0, 3.4, 3.3, 3.6],
        "Stat_Earlier": [7.5, 8.1, 7.6, 7.8, 6.9, 7.8],
        "Eng_New": [2.5, 2.8, 2.0, 2.7, 2.5, 2.4],
        "Eng_Earlier": [5.1, 5.3, 4.9, 5.5, 5.4, 4.8],
    }

    df = pd.DataFrame(data)
    long_df = pd.melt(
        df,
        id_vars="Programmer",
        value_vars=["Stat_New", "Stat_Earlier", "Eng_New", "Eng_Earlier"],
        var_name="Condition",
        value_name="Time",
    )
    long_df["Problem"] = long_df["Condition"].apply(
        lambda x: "Stat" if "Stat" in x else "Eng"
    )
    long_df["Model"] = long_df["Condition"].apply(
        lambda x: "New" if "New" in x.split("_")[1] else "Earlier"
    )
    model = smf.mixedlm(
        "Time ~ C(Model) * C(Problem)", long_df, groups=long_df["Programmer"]
    ).fit()

    print(model.summary())


if __name__ == "__main__":
    main()
