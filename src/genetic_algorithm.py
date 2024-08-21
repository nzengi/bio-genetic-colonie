from population import initialize_population, selection, crossover, mutate

class GeneticAlgorithm:
    def __init__(self, population_size, gene_length, generations, mutation_rate, blockchain_interface, accounts):
        self.population_size = population_size
        self.gene_length = gene_length
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.blockchain_interface = blockchain_interface
        self.accounts = accounts

    def run(self):
        """Run the genetic algorithm for the specified number of generations."""
        population = initialize_population(self.population_size, self.gene_length, self.blockchain_interface, self.accounts)
        
        for generation in range(self.generations):
            # Evaluate fitness for each robot
            for robot in population:
                robot.evaluate_fitness()
            
            # Select the best-performing robots
            selected_population = selection(population)
            
            # Create a new generation via crossover and mutation
            new_population = []
            while len(new_population) < self.population_size:
                parent1, parent2 = random.sample(selected_population, 2)
                child = crossover(parent1, parent2)
                mutate(child, self.mutation_rate)
                new_population.append(child)
            
            population = new_population  # Replace old population with new population
            
            # Optional: Print the best fitness of the current generation for monitoring progress
            best_robot = max(population, key=lambda x: x.fitness)
            print(f"Generation {generation + 1}: Best Fitness = {best_robot.fitness}")
            best_robot.update_task_performance_on_blockchain(self.blockchain_interface)
        
        # Return the best robot from the final population
        return max(population, key=lambda x: x.fitness)
