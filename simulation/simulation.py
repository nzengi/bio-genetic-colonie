from colonies.colony import Colony

def run_simulation():
    colony = Colony("Alpha", population_size=100)
    generations = 50
    
    for generation in range(generations):
        print(f"Generation {generation + 1}")
        colony.adapt()
        # Gelişmeleri gözlemle veya kayıt altına al

if __name__ == "__main__":
    run_simulation()
