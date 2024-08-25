import random

class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, crossover_rate):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.population = self.initialize_population()

    def initialize_population(self):
        # Başlangıç popülasyonunu rastgele oluştur
        return [self.random_individual() for _ in range(self.population_size)]

    def random_individual(self):
        # Rastgele bir birey oluştur (örneğin bir dizi bit)
        return [random.randint(0, 1) for _ in range(10)]

    def fitness(self, individual):
        # Bireyin uygunluğunu değerlendir
        return sum(individual)  # Örnek uygunluk fonksiyonu

    def selection(self):
        # Popülasyondan seçim yap
        return random.choices(self.population, k=2, weights=[self.fitness(ind) for ind in self.population])

    def crossover(self, parent1, parent2):
        # İki ebeveyn arasında çaprazlama yap
        if random.random() < self.crossover_rate:
            point = random.randint(1, len(parent1) - 1)
            return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
        return parent1, parent2

    def mutate(self, individual):
        # Mutasyon işlemi
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                individual[i] = 1 - individual[i]
        return individual

    def evolve(self):
        # Yeni bir nesil oluştur
        new_population = []
        for _ in range(self.population_size // 2):
            parent1, parent2 = self.selection()
            child1, child2 = self.crossover(parent1, parent2)
            new_population.append(self.mutate(child1))
            new_population.append(self.mutate(child2))
        self.population = new_population
