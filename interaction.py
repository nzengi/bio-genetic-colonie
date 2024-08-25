class ColonyInteraction:
    def __init__(self, colony1, colony2):
        self.colony1 = colony1
        self.colony2 = colony2

    def exchange_information(self):
        # Koloniler arasındaki bilgi alışverişini genişlet
        best_individual_colony1 = max(self.colony1.genetic_algorithm.population, key=self.colony1.genetic_algorithm.fitness)
        best_individual_colony2 = max(self.colony2.genetic_algorithm.population, key=self.colony2.genetic_algorithm.fitness)

        # Stratejik bilgi paylaşımı (örneğin, hayatta kalma stratejileri)
        strategy_colony1 = sum(best_individual_colony1) / len(best_individual_colony1)
        strategy_colony2 = sum(best_individual_colony2) / len(best_individual_colony2)

        if strategy_colony1 > strategy_colony2:
            self.colony2.genetic_algorithm.population.append(best_individual_colony1)
        else:
            self.colony1.genetic_algorithm.population.append(best_individual_colony2)
