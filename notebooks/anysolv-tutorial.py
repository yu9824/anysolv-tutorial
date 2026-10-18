# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.6
#   kernelspec:
#     display_name: work
#     language: python
#     name: python3
# ---

# %%
from anysolv import predict_solvation_energy
from ase.build import molecule
from fairchem.core import FAIRChemCalculator
from fairchem.core.units.mlip_unit import load_predict_unit

# %%
predictor = load_predict_unit(
    "../models/uma-s-1p2.pt",
    inference_settings="default",
    device="cuda",
    seed=41,
)
calc = FAIRChemCalculator(predictor, task_name="omol")


# %%
atoms = molecule("CH4")
atoms.info["charge"] = 0
atoms.info["spin"] = 1
atoms.calc = calc
