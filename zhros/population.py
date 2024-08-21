import random
from robot import Robot

def initialize_population(population_size, gene_length, blockchain_interface, accounts):
    """Initialize the population of robots and authorize them on the blockchain."""
    population = []
    for _ in range(population_size):
        genes = [random.randint(0, 1) for _ in range(gene_length)]
        address = random.choice(accounts)  # Simulate Ethereum addresses for robots
        robot = Robot(genes, address)
        robot.authorize_on_blockchain(blockchain_interface)  # Authorize robot on the blockchain
        population.append(robot)
    return population

def selection(population):
    """Select the best-performing robots for reproduction."""
    population.sort(key=lambda x: x.fitness, reverse=True)
    return population[:len(population) // 2]

def crossover(parent1, parent2):
    """Create a new robot by combining genes from two parent robots."""
    crossover_point = random.randint(1, len(parent1.genes) - 2)
    child_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
    return Robot(child_genes, parent1.address)  # Reuse address or assign a new one if needed

def mutate(robot, mutation_rate):
    """Introduce variability in the robot population by mutating genes."""
    for i in range(len(robot.genes)):
        if random.random() < mutation_rate:
            robot.genes[i] = 1 - robot.genes[i]  # Flip the gene (0 to 1 or 1 to 0)
