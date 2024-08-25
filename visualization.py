import matplotlib.pyplot as plt

def plot_performance(performance_data):
    generations = [data[0] for data in performance_data]
    colony1_fitness = [data[1] for data in performance_data]
    colony2_fitness = [data[2] for data in performance_data]
    
    plt.plot(generations, colony1_fitness, label="Colony Alpha Best Fitness")
    plt.plot(generations, colony2_fitness, label="Colony Beta Best Fitness")
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness")
    plt.title("Colony Performance Over Generations")
    plt.legend()
    plt.show()
