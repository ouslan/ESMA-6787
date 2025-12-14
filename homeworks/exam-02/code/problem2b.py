import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def main() -> None:
    df = pd.read_csv("marketing.txt", sep=r"\s+")
    plt.figure(figsize=(8, 6))

    sns.lineplot(data=df, x="Fee", y="WorkIndex", hue="Supervisory")
    plt.title("Interaction Plot of Fee Schedule and Supervisory on WorkIndex")
    plt.xlabel("Fee Schedule")
    plt.ylabel("WorkIndex (Quality of Work)")
    plt.legend(title="Supervisory", loc="upper left")
    plt.show()


if __name__ == "__main__":
    main()
