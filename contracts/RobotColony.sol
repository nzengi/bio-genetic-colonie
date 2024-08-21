import random
import numpy as np

# Define the Robot class which represents an individual in the population
class Robot:
    def __init__(self, genes):
        self.genes = genes  # A list of binary genes
        self.fitness = 0  # Fitness score initialized to 0
    
    # Function to evaluate the fitness of the robot
    def evaluate_fitness(self):
        task_performance = sum(self.genes)
        collaboration = sum(self.genes) / len(self.genes)
        energy_efficiency = len(self.genes) - sum(self.genes)
        
        # Custom fitness function: Adjust these weights as per project needs
        self.fitness = (0.5 * task_performance) + (0.3 * collaboration) - (0.2 * energy_efficiency)
        return self.fitness

# Function to initialize a population of robots
def initialize_population(population_size, gene_length):
    population = []
    for _ in range(population_size):
        genes = [random.randint(0, 1) for _ in range(gene_length)]
        robot = Robot(genes)
        population.append(robot)
    return population

# Selection function to choose the best robots for reproduction
def selection(population):
    population.sort(key=lambda x: x.fitness, reverse=True)
    return population[:len(population) // 2]

# Crossover function to combine genes from two parent robots
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1.genes) - 2)
    child_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
    return Robot(child_genes)

# Mutation function to introduce variability in the population
def mutate(robot, mutation_rate):
    for i in range(len(robot.genes)):
        if random.random() < mutation_rate:
            robot.genes[i] = 1 - robot.genes[i]  # Flip the gene (0 to 1 or 1 to 0)

# Main genetic algorithm function
def genetic_algorithm(population_size, gene_length, generations, mutation_rate):
    # Step 1: Initialize population
    population = initialize_population(population_size, gene_length)
    
    # Evolve the population over generations
    for generation in range(generations):
        # Step 2: Evaluate fitness for each robot
        for robot in population:
            robot.evaluate_fitness()
        
        # Step 3: Select the best-performing robots
        selected_population = selection(population)
        
        # Step 4: Create a new generation via crossover and mutation
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(selected_population, 2)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_population.append(child)
        
        population = new_population  # Replace old population with new population
        
        # Optional: Print the best fitness of the current generation for monitoring progress
        best_robot = max(population, key=lambda x: x.fitness)
        print(f"Generation {generation + 1}: Best Fitness = {best_robot.fitness}")
    
    # Return the best robot from the final population
    return max(population, key=lambda x: x.fitness)

# Parameters
POPULATION_SIZE = 100
GENE_LENGTH = 10
GENERATIONS = 50
MUTATION_RATE = 0.05

# Run the genetic algorithm
best_robot = genetic_algorithm(POPULATION_SIZE, GENE_LENGTH, GENERATIONS, MUTATION_RATE)
print(f"Best Robot Genes: {best_robot.genes}, Fitness: {best_robot.fitness}")
