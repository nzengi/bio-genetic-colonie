from algorithms.genetic_algorithm import GeneticAlgorithm

class Colony:
    def __init__(self, name, population_size):
        self.name = name
        self.genetic_algorithm = GeneticAlgorithm(population_size, mutation_rate=0.01, crossover_rate=0.7)

    def adapt(self):
        # Koloni adaptasyon süreci
        self.genetic_algorithm.evolve()
