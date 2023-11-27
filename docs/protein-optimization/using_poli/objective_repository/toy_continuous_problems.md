# Toy continuous objective functions

![Type of objective function: continuous](https://img.shields.io/badge/Input_type-continuous-red)
![Environment to run this objective function: poli base](https://img.shields.io/badge/Environment-poli____base-teal
)

## About

These are the usual objective function people use to test continuous optimizers {cite:p}`Al-Roomi:continuous_objective_benchmarks:2015`. In particular, we include:

- For $n$-dimensional optimization:
    - [`ackley_function_01`](https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/227-ackley-s-function-no-1-or-ackley-s-path-function),
    - [`alpine_01`](https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/162-alpine-function-no-1),
    - [`alpine_02`](https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/163-alpine-function-no-2),
    - [`bent_cigar`](https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/164-bent-cigar-function),
    - [`brown`](https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/241-brown-s-function),
    - [`chung_reynolds`](https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/165-chung-reynolds-function),
    - [`cosine_mixture`](https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/166-cosine-mixture-function),
    - [`deb_01`](https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/231-deb-s-function-no-01),
    - [`deb_02`](https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/232-deb-s-function-no-02),
    - [`deflected_corrugated_spring`](https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/238-deflected-corrugated-spring-function),
    - `shifted_sphere` ($\sum_{d=1}^n (x_d - 1)^2$),
    - [`egg_holder`](https://www.al-roomi.org/benchmarks/unconstrained/n-dimensions/187-egg-holder-function),
- For specific dimensions:
    - [`easom`](https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/22-easom-s-function), which is only available in 2 dimensions.
    - [`cross_in_tray`](https://www.al-roomi.org/benchmarks/unconstrained/2-dimensions/44-cross-in-tray-function), which is only available in 2 dimensions.

:::{warning}

Some of the signs might be flipped, since we are usually interested in maximization. Some of the constants inside might also be changed for scale. [For the definitive version we used, check the implementation](https://github.com/MachineLearningLifeScience/poli/blob/dev/src/poli/objective_repository/toy_continuous_problem/definitions.py).

:::

## Prerequisites

None, this function should always run out-of-the-box

## How to run

```python
import numpy as np
from poli import objective_factory

# Choose a function name and number of dimensions
function_name = "ackley_function_01"
n_dimensions = 2  # it's 2 by default.

# How to create
problem_info, f, x0, y0, run_info = objective_factory.create(
    name="toy_continuous_problem",
    function_name=function_name,
    n_dimensions=n_dimensions,  # For some, this can be arbitrary.
)


# Example input:
x = np.array([[0.0, 0.0]])  # must be of shape [b, n_dimensions], in this case [1, 2].

# Querying:
print(f(x))  # Should be [[0.0]] in this example
```
