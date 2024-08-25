from algorithms.genetic_algorithm import GeneticAlgorithm
from strategies import AggressiveStrategy, DefensiveStrategy

class Colony:
    def __init__(self, name, population_size):
        self.name = name
        self.genetic_algorithm = GeneticAlgorithm(population_size, mutation_rate=0.01, crossover_rate=0.7)
        self.strategy = self.select_strategy()

    def select_strategy(self):
        # Koloni başlangıç stratejisini seçer
        if self.name == "Alpha":
            return AggressiveStrategy("Aggressive")
        else:
            return DefensiveStrategy("Defensive")

    def evaluate_performance(self):
        # Performansa göre strateji değiştirme
        average_fitness = sum([self.genetic_algorithm.fitness(ind) for ind in self.genetic_algorithm.population]) / len(self.genetic_algorithm.population)
        
        # Performans düşükse strateji değiştir
        if average_fitness < 5:  # Örnek bir eşik değeri
            self.strategy = DefensiveStrategy("Defensive")
        else:
            self.strategy = AggressiveStrategy("Aggressive")

    def adapt(self):
        # Stratejiyi uygula ve adaptasyon sürecini başlat
        self.strategy.execute(self)
        self.genetic_algorithm.evolve()
        self.evaluate_performance()
