# Discrete NSGA-2

![Type of optimizer algorithm: discrete inputs](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Type of objective function: multi-objective](https://img.shields.io/badge/Output-multi--objective-red)


## About

The non-dominated sorting genetic algorithm (NSGA) is a common baseline for multi-objective optimization (see {cite:p}`Deb:NSGA-2:2002`).

In this discrete-input version, we use a mating procedure based on randomly mutating parents as many times as specified upon creation. Our implementation is a wrapper around `pymoo`'s version of NSGA-2 {cite:p}`pymoo`. 

## How to run

Here is a minimal example on a two copies of the toy problem `aloha`:

```python
import numpy as np

from poli.objective_repository import AlohaProblemFactory
from poli.core.multi_objective_black_box import MultiObjectiveBlackBox

from poli_baselines.solvers import DiscreteNSGAII

# Hyperparameters
population_size = 15
batch_size = 10
max_iterations = 100
num_mutations = 1

# Creating the aloha problem
problem_factory = AlohaProblemFactory()
f_aloha, _, _ = problem_factory.create()

# Putting two copies together to make a multi-objective black box
f = MultiObjectiveBlackBox(
    info=f_aloha.info,
    objective_functions=[f_aloha, f_aloha],
)

# Creating a random initial population
x0 = np.random.choice(f.info.alphabet, size=(batch_size, 5))
y0 = f(x0)

# Creating an instance of the solver
solver = DiscreteNSGAII(
    black_box=f,
    x0=x0,
    y0=y0,
    population_size=population_size,
    num_mutations=num_mutations
)

# Running the evolution
solver.solve(max_iter=max_iterations)
print(f"Best solution: {solver.get_best_solution()}")
```

## See more

- Our implementation uses `pymoo`'s version of `NSGA-2` {cite:p}`pymoo`, plus [a wrapper for discrete objective functions](https://github.com/MachineLearningLifeScience/poli-baselines/blob/aacc02a2ab17ebcf94f381e92222dcf7711690ec/src/poli_baselines/core/utils/pymoo/interface.py#L44).
