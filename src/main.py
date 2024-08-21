from genetic_algorithm import GeneticAlgorithm
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

# List of accounts (simulate Ethereum addresses)
accounts = ["0xAccount1", "0xAccount2", "0xAccount3", "0xAccount4", "0xAccount5"]  # Replace with real accounts

# Run the genetic algorithm
genetic_algorithm = GeneticAlgorithm(POPULATION_SIZE, GENE_LENGTH, GENERATIONS, MUTATION_RATE, blockchain_interface, accounts)
best_robot = genetic_algorithm.run()

# Log the result
log_generation(logger, GENERATIONS, best_robot.fitness)
print(f"Best Robot Genes: {best_robot.genes}, Fitness: {best_robot.fitness}")
