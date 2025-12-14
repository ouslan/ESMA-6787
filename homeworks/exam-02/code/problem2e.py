from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
import pandas as pd


def main() -> None:
    df = pd.read_csv("marketing.txt", sep=r"\s+")
    model = ols("WorkIndex ~ C(Fee) + C(Schedule)", data=df).fit()

    anova_results = anova_lm(model)
    print(anova_results)

    conf_int = model.conf_int(alpha=0.05)
    print("Confidence Intervals for the factors:")
    print(conf_int)


if __name__ == "__main__":
    main()
