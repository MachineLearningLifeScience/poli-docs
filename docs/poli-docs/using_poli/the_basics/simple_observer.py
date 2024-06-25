from pathlib import Path
from uuid import uuid4
import json

import numpy as np

from poli.core.black_box_information import BlackBoxInformation
from poli.core.util.abstract_observer import AbstractObserver

THIS_DIR = Path().resolve()

class SimpleObserver(AbstractObserver):
    def __init__(self):
        # Creating a unique id for this experiment in
        # particular:
        experiment_id = str(uuid4())
        self.experiment_id = experiment_id

        # Creating a local directory for the results
        experiment_path = THIS_DIR / "results" / experiment_id
        experiment_path.mkdir(exist_ok=True, parents=True)
        
        self.experiment_path = experiment_path
    
    def initialize_observer(
        self,
        problem_setup_info: BlackBoxInformation,
        caller_info: object,
        seed: int
    ) -> object:

        # Saving the metadata for this experiment
        metadata = problem_setup_info.as_dict()

        # Adding the information the user wanted to provide
        # (Recall that this caller info gets forwarded
        # from the objective_factory.create function)
        metadata["caller_info"] = caller_info

        metadata["seed"] = seed

        # Saving the metadata
        with open(self.experiment_path / "metadata.json", "w") as f:
            json.dump(metadata, f)
    
    def observe(self, x: np.ndarray, y: np.ndarray, context=None) -> None:
        # Appending these results to the results file.
        with open(self.experiment_path / "results.txt", "a") as fp:
            fp.write(f"{x.tolist()}\t{y.tolist()}\n")
