"""
This script is a barebones example of how to
use the FoldX class to perform a single mutation.

Just to have an example, we download 101m from PDB.
See here for more information:
https://www.rcsb.org/structure/101M
"""
from pathlib import Path
import subprocess
import shutil

from Bio import PDB
from Bio.PDB.Residue import Residue
from Bio.SeqUtils import seq1

PATH_TO_FOLDX_FILES = Path().home() / "foldx"
THIS_DIR = Path(__file__).parent.resolve()
WORKING_DIR = THIS_DIR / "tmp"
WORKING_DIR.mkdir(exist_ok=True)

if __name__ == "__main__":
    # TODO: download the file automatically
    assert (
        THIS_DIR / "101m.pdb"
    ).exists(), "Please download 101m.pdb from PDB, and place it adjacent to this file."
    shutil.copyfile(THIS_DIR / "101m.pdb", WORKING_DIR / "101m.pdb")
    shutil.copyfile(PATH_TO_FOLDX_FILES / "rotabase.txt", WORKING_DIR / "rotabase.txt")

    # Building the command for repairing the wildtype PDB
    if not (WORKING_DIR / "101m_Repair.pdb").exists():
        repair_cmd = [
            str(PATH_TO_FOLDX_FILES / "foldx"),
            "--pdb",
            "101m.pdb",
            "--command",
            "RepairPDB",
            "--water",
            "-CRYSTAL",
            "--pH",
            "7.0",
        ]

        # Running the repair command
        subprocess.run(repair_cmd, cwd=WORKING_DIR)

    # If this process ran correctly, a file
    # called 101m_Repair.pdb should have been created
    # inside the working directory.
    # Now we parse it using Biopython to read the residues, and their
    # positions.

    # Parsing the wildtype PDB
    parser = PDB.PDBParser()
    structure = parser.get_structure("pdb", WORKING_DIR / "101m_Repair.pdb")
    residues = list(structure.get_residues())

    # Building a list of substitutions
    mutation_list = [
        {
            "seq_idx": 0,
            "to": "G",
        }
    ]

    # FoldX expects a individual_list.txt of mutations.
    # The description of these mutations need to be
    # {original_residue}{chain_id}{sequence_id_in_chain}{mutated_residue};

    # We will grab the mutation list, and write it to a file using this specification.
    with open(WORKING_DIR / "individual_list.txt", "w") as f:
        for mutation in mutation_list:
            # We get the initial residue from the PDB file, this is a Residue type.
            # You can check the documentation of these inside Biopython.
            residue = residues[mutation["seq_idx"]]

            # The original residue lies in residue.resname. This is the 3-letter code.
            # To tranform it into the 1-letter code, we use seq1 from Bio.SeqUtils.
            original_residue = seq1(residue.resname)

            # We can read the position as the second position of the ID:
            # residue.id = (' ', position_in_chain, ' ')
            position = residue.id[1]

            # The chain ID can be read from the parent of the residue
            chain_id = residue.get_parent().id

            # The line we need to write, then, is:
            f.write(f"{original_residue}{chain_id}{position}{mutation['to']};")

    # Now we can run FoldX using the BuildModel command.
    # This will create four different files:
    foldx_cmd = [
        str(PATH_TO_FOLDX_FILES / "foldx"),
        "--pdb",
        "101m_Repair.pdb",
        "--command",
        "BuildModel",
        "--mutant-file",
        str(WORKING_DIR / "individual_list.txt"),
        "--water",
        "-CRYSTAL",
        "--pH",
        "7.0",
    ]

    # Running the command
    subprocess.run(foldx_cmd, cwd=WORKING_DIR)

    # The output files are:
    # [TODO: add]

    # We can now parse the output files to get the results.
    # These are stored in the last two lines of the file
    # Raw_101m_Repair.
    with open(WORKING_DIR / f"Raw_101m_Repair.fxout", "r") as f:
        lines = f.readlines()
        second_to_last_line = lines[-2]
        last_line = lines[-1]

    wild_stability = float(second_to_last_line.split()[1])
    mutant_stability = float(last_line.split()[1])

    print(f"Wildtype stability: {wild_stability}")
    print(f"Mutant stability: {mutant_stability}")
