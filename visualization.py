import matplotlib.pyplot as plt
import pandas as pd

def plot_performance(performance_data):
    df = pd.DataFrame(performance_data, columns=["Generation", "Colony Alpha Best Fitness", "Colony Beta Best Fitness", "Strategy"])

    plt.figure(figsize=(12, 6))
    
    # Fitness grafikleri
    plt.plot(df["Generation"], df["Colony Alpha Best Fitness"], label="Colony Alpha Best Fitness", color='blue')
    plt.plot(df["Generation"], df["Colony Beta Best Fitness"], label="Colony Beta Best Fitness", color='red')
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness")
    plt.title("Colony Performance Over Generations")
    plt.legend()

    # Strateji değişim grafiği
    strategy_changes = df[df["Strategy"].shift() != df["Strategy"]]
    for index, row in strategy_changes.iterrows():
        plt.axvline(x=row["Generation"], color='green', linestyle='--', label=f'Strategy Change: {row["Strategy"]}')

    plt.show()
