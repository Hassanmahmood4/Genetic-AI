import random
import math
import statistics
import sys

LOWER = -1.0
UPPER  =  2.0

def fitness_fn(x: float) -> float:

    return x * math.sin(10 * math.pi * x) + 1.0


def make_individual() -> float:

    return random.uniform(LOWER, UPPER)

def mutate(ind: float, mutation_rate: float, mutation_scale: float) -> float:

    if random.random() < mutation_rate:
        ind += random.gauss(0, mutation_scale)

    return max(LOWER, min(UPPER, ind))

def crossover(parent1: float, parent2: float, alpha: float = 0.5):

    c1 = alpha * parent1 + (1 - alpha) * parent2
    c2 = alpha * parent2 + (1 - alpha) * parent1

    c1 = max(LOWER, min(UPPER, c1))
    c2 = max(LOWER, min(UPPER, c2))
    return c1, c2

def tournament_select(pop, pop_fitness, k=3):

    best = None
    best_idx = None
    for _ in range(k):
        i = random.randrange(len(pop))
        if best is None or pop_fitness[i] > best:
            best = pop_fitness[i]
            best_idx = i
    return pop[best_idx]


def run_ga(
    pop_size=50,
    generations=100,
    crossover_rate=0.8,
    mutation_rate=0.2,
    mutation_scale=0.1,
    elitism_count=1,
    tournament_k=3,
    alpha=0.5,
    seed=None
):
    if seed is not None:
        random.seed(seed)


    population = [make_individual() for _ in range(pop_size)]
    history_best = []
    history_mean = []

    for gen in range(generations):
        pop_fitness = [fitness_fn(ind) for ind in population]


        best_idx = max(range(len(population)), key=lambda i: pop_fitness[i])
        best_val = pop_fitness[best_idx]
        mean_val = statistics.mean(pop_fitness)
        history_best.append(best_val)
        history_mean.append(mean_val)

        if gen % max(1, generations // 10) == 0 or gen == generations - 1:
            print(f"Gen {gen:3d} : best = {best_val:.6f} (x={population[best_idx]:.6f}), mean = {mean_val:.6f}")


        new_pop = []
        if elitism_count > 0:

            sorted_idxs = sorted(range(len(population)), key=lambda i: pop_fitness[i], reverse=True)
            for i in sorted_idxs[:elitism_count]:
                new_pop.append(population[i])


        while len(new_pop) < pop_size:

            parent1 = tournament_select(population, pop_fitness, k=tournament_k)
            parent2 = tournament_select(population, pop_fitness, k=tournament_k)


            if random.random() < crossover_rate:
                child1, child2 = crossover(parent1, parent2, alpha=alpha)
            else:
                child1, child2 = parent1, parent2


            child1 = mutate(child1, mutation_rate, mutation_scale)
            if len(new_pop) < pop_size:
                new_pop.append(child1)
            if len(new_pop) < pop_size:
                child2 = mutate(child2, mutation_rate, mutation_scale)
                new_pop.append(child2)

        population = new_pop


    pop_fitness = [fitness_fn(ind) for ind in population]
    best_idx = max(range(len(population)), key=lambda i: pop_fitness[i])
    return {
        "best_x": population[best_idx],
        "best_fitness": pop_fitness[best_idx],
        "history_best": history_best,
        "history_mean": history_mean
    }


if __name__ == "__main__":

    result = run_ga(
        pop_size=80,
        generations=120,
        crossover_rate=0.9,
        mutation_rate=0.2,
        mutation_scale=0.08,
        elitism_count=2,
        tournament_k=3,
        alpha=0.6,
        seed=42
    )

    print("\nFinal best solution:")
    print(f"x = {result['best_x']:.6f}, fitness = {result['best_fitness']:.6f}")


    try:
        import matplotlib.pyplot as plt
        plt.plot(result["history_best"], label="best")
        plt.plot(result["history_mean"], label="mean")
        plt.xlabel("Generation")
        plt.ylabel("Fitness")
        plt.legend()
        plt.title("GA progress")
        plt.grid(True)
        plt.show()
    except Exception:
        pass