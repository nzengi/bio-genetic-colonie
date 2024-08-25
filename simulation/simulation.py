from colonies.colony import Colony
from interaction import ColonyInteraction
from reporting import generate_report, analyze_performance

def run_simulation():
    colony1 = Colony("Alpha", population_size=100)
    colony2 = Colony("Beta", population_size=100)
    interaction = ColonyInteraction(colony1, colony2)
    
    generations = 50
    performance_data = []
    
    for generation in range(generations):
        print(f"Generation {generation + 1}")
        colony1.adapt()
        colony2.adapt()
        interaction.exchange_information()
        
        best_fitness_colony1 = max([colony1.genetic_algorithm.fitness(ind) for ind in colony1.genetic_algorithm.population])
        best_fitness_colony2 = max([colony2.genetic_algorithm.fitness(ind) for ind in colony2.genetic_algorithm.population])
        performance_data.append((generation, best_fitness_colony1, best_fitness_colony2, colony1.strategy.name))
    
    # Performans verilerini kaydet
    generate_report(performance_data)
    
    # Performans verilerini analiz et
    analyze_performance(performance_data)
