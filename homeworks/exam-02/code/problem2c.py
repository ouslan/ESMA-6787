import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm


def main() -> None:
    df = pd.read_csv("marketing.txt", sep=r"\s+")
    model = smf.ols("WorkIndex ~ C(Fee) * C(Schedule)", data=df).fit()
    anova_results = anova_lm(model)
    print(anova_results)


if __name__ == "__main__":
    main()
