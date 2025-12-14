import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main() -> None:
    df = pd.read_csv("marketing.txt", sep=r"\s+")
    plt.figure(figsize=(8, 6))

    sns.lineplot(
        data=df, x="Fee", y="WorkIndex", hue="Schedule", marker="o", palette="tab10"
    )
    plt.title("Interaction Plot of Fee Schedule and Scope of Work on WorkIndex")
    plt.xlabel("Fee Schedule")
    plt.ylabel("WorkIndex (Quality of Work)")
    plt.legend(title="Schedule", loc="upper left")
    plt.show()


if __name__ == "__main__":
    main()
