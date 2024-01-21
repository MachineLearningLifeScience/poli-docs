# Bayesian Optimization

![Type of optimizer algorithm: continuous inputs](https://img.shields.io/badge/Type-continuous_inputs-cyan)

## About

Bayesian Optimization is a sample-efficient black box optimization algorithm which uses an uncertainty-aware approximation $\tilde{f}(\bm{x})$ of the objective function $f$. This surrogate model $\tilde{f}$ is usually a Gaussian Process, whose predictions and uncertainties are used to build an _acquisition function_ $\alpha(\bm{x})$. Optimizing $\alpha$ renders points that are _likely_ to perform well for $f$. By smartly including uncertainties in $\alpha$, Bayesian Optimization balances exploration and exploitation.

Our implementation uses `gpytorch` and `botorch` as the engines for Bayesian Optimization {cite+p}`Balandat:botorch:2020,gardner:gpytorch:2018`. We use the default `botorch` single-task Gaussian Process, and we optimize the acquisition function using grid-search for 1 and 2 dimensions, and using `botorch`'s utilities from 3 onwards.

## How to run

```python
import numpy as np

from poli import objective_factory

from poli_baselines.solvers import VanillaBayesianOptimization

problem_info, f_ackley, _, _, _ = objective_factory.create(
    name="toy_continuous_problem",
    function_name="ackley_function_01",
    n_dimensions=2,
)

x0 = np.random.randn(2).reshape(1, -1).clip(-2.0, 2.0)
y0 = f_ackley(x0)

bo_solver = VanillaBayesianOptimization(
    black_box=f_ackley,
    x0=x0,
    y0=y0,
)

bo_solver.solve(max_iter=10)
```

## See more

- [*Taking the human out of the loop*](https://www.cs.ox.ac.uk/people/nando.defreitas/publications/BayesOptLoop.pdf) is a great tutorial of Bayesian Optimization {cite:p}`Shahriari:BOReview:2016`.
- Since `poli` works mostly on discrete inputs, this baseline is implemented with the intention of optimizing in the latent spaces of deep generative models like Generative Adversarial Networks (GANs) or Variational Autoencoders (VAEs) {cite:p}`GomezBombarelli:VAEsAndOpt:2018`.