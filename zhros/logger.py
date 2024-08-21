import logging

def setup_logger():
    """Set up the logger for tracking progress."""
    logger = logging.getLogger("genetic_algorithm")
    logger.setLevel(logging.INFO)
    
    handler = logging.FileHandler("genetic_algorithm.log")
    handler.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger

def log_generation(logger, generation, best_fitness):
    """Log the progress of each generation."""
    logger.info(f"Generation {generation}: Best Fitness = {best_fitness}")
