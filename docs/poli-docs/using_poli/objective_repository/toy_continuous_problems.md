# Toy continuous objective functions

![Type of objective function: continuous](https://img.shields.io/badge/Input_type-continuous-red)
![Environment to run this objective function: poli base](https://img.shields.io/badge/Environment-poli____base-teal
)

## About

These are the usual objective function people use to test continuous optimizers {cite:p}`Al-Roomi:continuous_objective_benchmarks:2015,SurjanovicBingham:test_functions:2013`. In particular, we include:

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
from poli.objective_repository import (
    ToyContinuousBlackBox,
    ToyContinuousProblemFactory,
)

function_name = "ackley_function_01"
n_dimensions = 2

# Creating the black box
f = ToyContinuousBlackBox(
    function_name=function_name,
    n_dimensions=n_dimensions,
)

# Creating a problem
problem = ToyContinuousProblemFactory().create(
    function_name=function_name,
    n_dimensions=n_dimensions,
)
f, x0 = problem.black_box, problem.x0

# Example input:
x = np.array([[0.5, 0.5]])  # must be of shape [b, L], in this case [1, 2].

# Querying:
print(f(x))
```

## Creating problems with low intrinsic dimensionality

Some optimization algorithms (like [LineBO](https://arxiv.org/abs/1902.03229) or [SAASBO](https://proceedings.mlr.press/v161/eriksson21a.html)) rely on the assumption that there is a _low intrinsic dimensionality_ to the problem. Roughly speaking, this means that only a subset of the variables are actually relevant to the problem in question. This `poli` objective allows you to create such problems. For example, consider `camelback_2d` (which is usually only defined in two dimensions). You can embed this function into, say, 30 dimensions by creating the objective as follows:

```python
problem = ToyContinuousProblemFactory().create(
    function_name="camelback_2d",
    embed_in=30,  #  This will create a function that takes 30d input values
)

f, x0 = problem.black_box, problem.x0
```

During the creation process, the two relevant dimensions of `camelback_2d` will be randomly embedded into two of the 30 dimensions. These are accessible under `f.function.dimensions_to_embed_in` (which is an array of integers).

## How to cite

If you use this black box, we expect that you cite the following resources:

::::{tab-set}

:::{tab-item} References as text

[1] Al-Roomi, A. R. (2015). Unconstrained Single-Objective Benchmark Functions Repository. Dalhousie University, Electrical and Computer Engineering. Halifax, Nova Scotia, Canada. Available at: https://www.al-roomi.org/benchmarks/unconstrained

[2] Surjanovic, S., Bingham, D., “Optimization Test Functions and Datasets.” Accessed April 12, 2024. https://www.sfu.ca/~ssurjano/optimization.html.

[3] González-Duque, M., Bartels, S., & Michael, R. (2024). poli: a libary of discrete sequence objectives [Computer software]. https://github.com/MachineLearningLifeScience/poli


:::

:::{tab-item} References as `BibTeX`

```

@MISC{Al-Roomi:continuous_objective_benchmarks:2015,
    author = {Ali R. Al-Roomi},
    title = {{Unconstrained Single-Objective Benchmark Functions Repository}},
    year = {2015},
    address = {Halifax, Nova Scotia, Canada},
    institution = {Dalhousie University, Electrical and Computer Engineering},
    url = {https://www.al-roomi.org/benchmarks/unconstrained}
}


@misc{SurjanovicBingham:test_functions:2013,
  author = {Surjanovic, S. and Bingham, D.},
  title = {Optimization Test Functions and Datasets},
  year = {2013},
  howpublished = {\url{https://www.sfu.ca/~ssurjano/optimization.html}},
  note = {Accessed: 2024-04-12}
}

@software{Gonzalez-Duque:poli:2024,
author = {González-Duque, Miguel and Bartels, Simon and Michael, Richard},
month = jan,
title = {{poli: a libary of discrete sequence objectives}},
url = {https://github.com/MachineLearningLifeScience/poli},
version = {0.0.1},
year = {2024}
}

```

:::

::::

