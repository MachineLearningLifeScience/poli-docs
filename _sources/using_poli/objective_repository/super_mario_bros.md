# Optimizing jumps in Super Mario Bros

![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli mario](https://img.shields.io/badge/Environment-poli____mario-teal
)

## About

Levels from the classic game Super Mario Bros can be considered as $14\times 14$ words, where the tokens correspond to the ground floor, pipe parts, enemies, etc {cite:p}`VGLC`.

This black box provides access to a simulator which takes levels as arrays of strings `[b, 14*14]` and returns the number of jump actions performed by an artificial agent[^robin], or `NaN` if the agent was not able to finish the level {cite:p}`Khalifa:marioAIFramework:2009,Volz:MarioGAN:2018`.

[^robin]: The agent in question is Robin Baumgarten's A* agent, which won the 2009 MarioAI competition {cite:p}`MarioAICompetition:Baumgarten:2010`.

This is a good toy example for **constrained** discrete optimization, where the constraints are given by whether the agent is able to solve the level or not.

## Prerequisites

This black box will require a virtual frame buffer or a screen.

:::{admonition} Running this in a cluster?
:class: dropdown

If you plan to run this inside an HPC cluster or a dockerized container, make sure you have `Xvfb` available.

Once you do, we recommend setting up a screen by running something like
```
Xvfb :99 -screen 0 1024x768x24 -ac +extension GLX +render -noreset &
```

The `&` at the end will allow the process to run in the background.

:::


## How to run

```python
from poli.objective_repository import (
    SuperMarioBrosBlackBox,
    SuperMarioBrosProblemFactory,
)

# Creating the black box
f = SuperMarioBrosBlackBox()

# Creating a problem
problem = SuperMarioBrosProblemFactory().create(visualize=False)
f, x0 = problem.black_box, problem.x0

# Let's print the level
print(x0.reshape(1, 14, 14))

# Querying (the flattened level):
print(f(x0))
```
