🧬 Genetic Algorithm for Function Optimization (Python)

This project implements a Genetic Algorithm (GA) in Python to optimize a one-dimensional,
multi-modal mathematical function:

f(x) = x \cdot \sin(10\pi x) + 1

The algorithm searches for the value of x in the range [-1, 2] that maximizes the fitness
function using evolutionary concepts such as selection, crossover, mutation, and elitism.

🚀 Features
	•	Continuous optimization (real-valued individuals)
	•	Tournament selection
	•	Arithmetic crossover
	•	Gaussian mutation with boundary constraints
	•	Elitism to preserve best solutions
	•	Tracks best and mean fitness over generations
	•	Optional visualization of convergence using Matplotlib


📁 Project Structure

.
├── Genetic AI.py          # Genetic Algorithm implementation
└── README.md        # Project documentation


🧪 Fitness Function

The function being optimized is:

f(x) = x * sin(10πx) + 1

This function is non-linear and multi-modal, making it a good test case for evolutionary
algorithms.

⚙️ Requirements
	•	Python 3.8+
	•	(Optional) Matplotlib for plotting

Install dependencies:

pip install matplotlib

▶️ How to Run

Clone the repository:

git clone https://github.com/Hassanmahmood4/Genetic-AI.git
cd Genetic-AI

Run the program:

python Genetic AI.py


📈 Output

During execution, the program prints progress like:

Gen   0 : best = 1.534210 (x=0.912345), mean = 1.102312
Gen  12 : best = 1.875432 (x=1.234567), mean = 1.503211
...
Final best solution:
x = 1.850213, fitness = 1.872345

If matplotlib is installed, a plot will be shown displaying:
	•	Best fitness per generation
	•	Mean fitness per generation

This helps visualize convergence behavior of the GA.


🧠 Genetic Algorithm Parameters

You can tweak the algorithm from the run_ga() function:

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

Parameter	Description
pop_size	Number of individuals in population
generations	Number of generations to evolve
crossover_rate	Probability of crossover
mutation_rate	Probability of mutation
mutation_scale	Strength of Gaussian mutation
elitism_count	Number of best individuals preserved
tournament_k	Tournament size for selection
alpha	Weight for arithmetic crossover
seed	Random seed for reproducibility


🛠️ Customization Ideas
	•	Extend to multi-dimensional optimization
	•	Add different selection strategies (roulette wheel, rank selection)
	•	Try different fitness functions
	•	Log results to file for experiments
	•	Compare GA with gradient-based methods


📚 Learning Goals

This project is useful for:
	•	Understanding Genetic Algorithms
	•	Learning evolutionary optimization
	•	Experimenting with hyperparameters
	•	Visualizing convergence behavior
  
