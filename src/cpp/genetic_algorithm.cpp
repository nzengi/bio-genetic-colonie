#include <vector>
#include <algorithm>
#include <random>

struct Robot {
    std::vector<int> genes;
    double fitness;

    Robot(int gene_length) : genes(gene_length), fitness(0.0) {
        std::generate(genes.begin(), genes.end(), []() { return rand() % 2; });
    }

    void evaluate_fitness() {
        int task_performance = std::accumulate(genes.begin(), genes.end(), 0);
        double collaboration = static_cast<double>(task_performance) / genes.size();
        int energy_efficiency = genes.size() - task_performance;

        fitness = (0.5 * task_performance) + (0.3 * collaboration) - (0.2 * energy_efficiency);
    }
};

class GeneticAlgorithm {
public:
    GeneticAlgorithm(int population_size, int gene_length, int generations, double mutation_rate)
        : population_size(population_size), gene_length(gene_length), generations(generations), mutation_rate(mutation_rate) {
        initialize_population();
    }

    void run() {
        for (int generation = 0; generation < generations; ++generation) {
            evaluate_population();
            std::vector<Robot> selected_population = selection();
            new_generation(selected_population);
        }
    }

    Robot get_best_robot() {
        return *std::max_element(population.begin(), population.end(), [](const Robot &a, const Robot &b) {
            return a.fitness < b.fitness;
        });
    }

private:
    int population_size;
    int gene_length;
    int generations;
    double mutation_rate;
    std::vector<Robot> population;

    void initialize_population() {
        population.clear();
        for (int i = 0; i < population_size; ++i) {
            population.emplace_back(gene_length);
        }
    }

    void evaluate_population() {
        for (auto &robot : population) {
            robot.evaluate_fitness();
        }
    }

    std::vector<Robot> selection() {
        std::sort(population.begin(), population.end(), [](const Robot &a, const Robot &b) {
            return a.fitness > b.fitness;
        });
        return std::vector<Robot>(population.begin(), population.begin() + population_size / 2);
    }

    void crossover(const Robot &parent1, const Robot &parent2, Robot &child) {
        int crossover_point = rand() % (gene_length - 1);
        std::copy(parent1.genes.begin(), parent1.genes.begin() + crossover_point, child.genes.begin());
        std::copy(parent2.genes.begin() + crossover_point, parent2.genes.end(), child.genes.begin() + crossover_point);
    }

    void mutate(Robot &robot) {
        for (int &gene : robot.genes) {
            if (static_cast<double>(rand()) / RAND_MAX < mutation_rate) {
                gene = 1 - gene;
            }
        }
    }

    void new_generation(const std::vector<Robot> &selected_population) {
        population.clear();
        while (population.size() < population_size) {
            const Robot &parent1 = selected_population[rand() % selected_population.size()];
            const Robot &parent2 = selected_population[rand() % selected_population.size()];
            Robot child(gene_length);
            crossover(parent1, parent2, child);
