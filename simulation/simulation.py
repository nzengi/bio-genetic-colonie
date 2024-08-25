from colonies.colony import Colony
from interaction import ColonyInteraction

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
        
        # Koloniler arasındaki bilgi alışverişinden önceki en iyi fitness değerlerini alın
        best_fitness_colony1_before = max([colony1.genetic_algorithm.fitness(ind) for ind in colony1.genetic_algorithm.population])
        best_fitness_colony2_before = max([colony2.genetic_algorithm.fitness(ind) for ind in colony2.genetic_algorithm.population])
        
        # Bilgi alışverişi yap
        interaction.exchange_information()
        
        # Koloniler arasındaki bilgi alışverişinden sonraki en iyi fitness değerlerini alın
        best_fitness_colony1_after = max([colony1.genetic_algorithm.fitness(ind) for ind in colony1.genetic_algorithm.population])
        best_fitness_colony2_after = max([colony2.genetic_algorithm.fitness(ind) for ind in colony2.genetic_algorithm.population])
        
        # Performans verilerini kaydet
        performance_data.append((generation, best_fitness_colony1_after, best_fitness_colony2_after))
    
    # Performans verilerini analiz et veya görselleştir
    for data in performance_data:
        print(f"Generation {data[0]}: Colony Alpha Best Fitness: {data[1]}, Colony Beta Best Fitness: {data[2]}")

if __name__ == "__main__":
    run_simulation()
