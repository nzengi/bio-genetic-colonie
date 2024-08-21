import genetic_algorithm_cpp as ga_cpp
from blockchain_interface import BlockchainInterface
from logger import setup_logger, log_generation

# Setup parameters
POPULATION_SIZE = 100
GENE_LENGTH = 10
GENERATIONS = 50
MUTATION_RATE = 0.05
PROVIDER_URL = "http://127.0.0.1:7545"  # Ganache or Ethereum node URL
CONTRACT_ADDRESS = "0xYourContractAddressHere"
ADMIN_ACCOUNT = "0xYourAdminAccountHere"

# Load the contract ABI from a file
with open('RobotColony.json') as f:
    contract_data = json.load(f)

# Setup the blockchain interface
blockchain_interface = BlockchainInterface(PROVIDER_URL, CONTRACT_ADDRESS, contract_data['abi'], ADMIN_ACCOUNT)

# Setup the logger
logger = setup_logger()

# Initialize the C++ genetic algorithm
genetic_algorithm = ga_cpp.GeneticAlgorithm(POPULATION_SIZE, GENE_LENGTH, GENERATIONS, MUTATION_RATE)
genetic_algorithm.run()

# Get the best robot
best_robot = genetic_algorithm.get_best_robot()

# Log the result
log_generation(logger, GENERATIONS, best_robot.fitness)
print(f"Best Robot Genes: {best_robot.genes}, Fitness: {best_robot.fitness}")

# Update blockchain with best robot's performance
blockchain_interface.verify_task(best_robot.address, int(best_robot.fitness))
