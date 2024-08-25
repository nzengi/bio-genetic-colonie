from colonies.colony import Colony
from interaction import ColonyInteraction

def run_simulation():
    colony1 = Colony("Alpha", population_size=100)
    colony2 = Colony("Beta", population_size=100)
    interaction = ColonyInteraction(colony1, colony2)
    
    generations = 50
    
    for generation in range(generations):
        print(f"Generation {generation + 1}")
        colony1.adapt()
        colony2.adapt()
        interaction.exchange_information()
        # Gelişmeleri gözlemle veya kayıt altına al

if __name__ == "__main__":
    run_simulation()
