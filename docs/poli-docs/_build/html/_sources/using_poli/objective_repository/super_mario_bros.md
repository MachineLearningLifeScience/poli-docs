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

The `&` at the end will allow the process to run in the background. We also recommend you set `DISPLAY=:99` as an environment variable.

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

## How to cite

If you use this black box, we expect you to cite the following resources:

::::{tab-set}

:::{tab-item} References as text

[1] Khalifa, Ahmed. (2009). The Mario AI Framework. GitHub. Available at: https://github.com/amidos2006/Mario-AI-Framework. Accessed on 12th of April, 2024.

[2] Togelius, J., Karakovskiy, S., & Baumgarten, R. (2010). The 2009 Mario AI Competition. In IEEE Congress on Evolutionary Computation (pp. 1-8). doi:10.1109/CEC.2010.5586133

[3] Volz, Vanessa, Simon M. Lucas, Jacob Schrum, Adam Smith, Jialin Liu, and Sebastian Risi. “Evolving Mario Levels in the Latent Space of a Deep Convolutional Generative Adversarial Network.” GECCO 2018 - Proceedings of the 2018 Genetic and Evolutionary Computation Conference, 2018, 221–28. https://doi.org/10.1145/3205455.3205517.

[4] González-Duque, M., Bartels, S., & Michael, R. (2024). poli: a libary of discrete sequence objectives [Computer software]. https://github.com/MachineLearningLifeScience/poli


:::

:::{tab-item} References as `BibTeX`

```
@misc{Khalifa:marioAIFramework:2009,
  title = {The Mario AI Framework},
  author = {Ahmed Khalifa},
  year = {2009},
  howpublished = {\url{https://github.com/amidos2006/Mario-AI-Framework}},
  note = {Accessed: 20/03/2024}
}

@INPROCEEDINGS{MarioAICompetition:Baumgarten:2010,
  author={Togelius, Julian and Karakovskiy, Sergey and Baumgarten, Robin},
  booktitle={IEEE Congress on Evolutionary Computation}, 
  title={The 2009 Mario AI Competition}, 
  year={2010},
  volume={},
  number={},
  pages={1-8},
  doi={10.1109/CEC.2010.5586133}
}

@article{Volz:MarioGAN:2018,
    title={Evolving Mario levels in the latent space of a deep convolutional generative adversarial network},
    ISSN={9781450356183},
    DOI={10.1145/3205455.3205517},
    journal={GECCO 2018 - Proceedings of the 2018 Genetic and Evolutionary Computation Conference},
    author={Volz, Vanessa and Lucas, Simon M. and Schrum, Jacob and Smith, Adam and Liu, Jialin and Risi, Sebastian},
    year={2018},
    pages={221–228}
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