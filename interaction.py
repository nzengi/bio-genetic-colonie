class ColonyInteraction:
    def __init__(self, colony1, colony2):
        self.colony1 = colony1
        self.colony2 = colony2

    def exchange_information(self):
        # Koloniler arasında bilgi alışverişi
        # Örneğin, en iyi bireyler arasında veri paylaşımı
        best_individual_colony1 = max(self.colony1.genetic_algorithm.population, key=self.colony1.genetic_algorithm.fitness)
        best_individual_colony2 = max(self.colony2.genetic_algorithm.population, key=self.colony2.genetic_algorithm.fitness)
        self.colony1.genetic_algorithm.population.append(best_individual_colony2)
        self.colony2.genetic_algorithm.population.append(best_individual_colony1)
