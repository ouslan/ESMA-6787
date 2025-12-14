from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
import pandas as pd


def main() -> None:
    df = pd.read_csv("marketing.txt", sep=r"\s+")
    model = ols("WorkIndex ~ C(Fee) * C(Schedule) * C(Supervisory)", data=df).fit()
    anova_results = anova_lm(model)
    print(anova_results)


if __name__ == "__main__":
    main()
