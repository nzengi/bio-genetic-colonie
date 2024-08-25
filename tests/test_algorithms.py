import unittest
from algorithms.genetic_algorithm import GeneticAlgorithm

class TestGeneticAlgorithm(unittest.TestCase):
    def test_evolution(self):
        ga = GeneticAlgorithm(10, mutation_rate=0.01, crossover_rate=0.7)
        initial_population = ga.population[:]
        ga.evolve()
        self.assertNotEqual(ga.population, initial_population)

if __name__ == '__main__':
    unittest.main()
