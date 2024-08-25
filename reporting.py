import pandas as pd

def generate_report(performance_data, filename="performance_report.csv"):
    # Performans verilerini bir CSV dosyasına kaydet
    df = pd.DataFrame(performance_data, columns=["Generation", "Colony Alpha Best Fitness", "Colony Beta Best Fitness", "Strategy"])
    df.to_csv(filename, index=False)

def analyze_performance(performance_data):
    # Verileri analiz et ve özet rapor oluştur
    df = pd.DataFrame(performance_data, columns=["Generation", "Colony Alpha Best Fitness", "Colony Beta Best Fitness", "Strategy"])
    
    # Koloni performansını karşılaştır
    alpha_avg_fitness = df["Colony Alpha Best Fitness"].mean()
    beta_avg_fitness = df["Colony Beta Best Fitness"].mean()
    
    # En iyi strateji hangisi?
    strategy_counts = df["Strategy"].value_counts()
    
    print("---- Performance Analysis ----")
    print(f"Average Best Fitness of Colony Alpha: {alpha_avg_fitness}")
    print(f"Average Best Fitness of Colony Beta: {beta_avg_fitness}")
    print("Strategy Distribution:")
    print(strategy_counts)

    return df
