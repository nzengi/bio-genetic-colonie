class AdaptationStrategy:
    def __init__(self, name):
        self.name = name

    def execute(self, colony):
        # Stratejiye göre koloninin adaptasyonunu sağlar
        raise NotImplementedError("Strateji yürütme yöntemi uygulanmalı")
    
class AggressiveStrategy(AdaptationStrategy):
    def execute(self, colony):
        # Daha agresif bir adaptasyon stratejisi uygular
        colony.genetic_algorithm.mutation_rate += 0.01
        colony.genetic_algorithm.crossover_rate -= 0.01

class DefensiveStrategy(AdaptationStrategy):
    def execute(self, colony):
        # Daha savunmacı bir strateji uygular
        colony.genetic_algorithm.mutation_rate -= 0.01
        colony.genetic_algorithm.crossover_rate += 0.01
