# FABI Artifact

## Abstract

This work studies how documentation inconsistencies in software repositories affect automated software engineering agents. FABI applies controlled mutations to documentation that an agent may rely on, injects each mutation as a patch into an otherwise clean repository, and runs the same software task under the selected agent configuration. The resulting runs are evaluated with the corresponding official evaluation procedure and compared with clean runs. This artifact contains the documentation mutation patches, the agents' generated patches or predictions, evaluation results, and the metadata needed to inspect the cases and reproduce the reported analyses.

## Code Structure for FABI

```text
FABI/
├── SWE/
│   ├── script/
│   ├── original_passed_cases/
│   └── RIPPLE/
├── SWE_live/
│   ├── original_passed_cases/
│   └── RIPPLE/
├── SWE_pro/
│   ├── original_passed_cases/
│   └── RIPPLE/
└── Mining/
```

- `SWE/`, `SWE_live/`, and `SWE_pro/` contain the artifacts for the
  corresponding SWE-bench settings.
- `original_passed_cases/` contains clean cases that passed the original run,
  together with their essential metadata.
- `RIPPLE/` contains mutation and evaluation artifacts, including mutation
  patches, agent-generated patches or predictions, and result summaries.
- `SWE/script/` contains the experiment and analysis scripts retained with the
  artifact.
- `Mining/` contains the related documentation-mining material.


## Source code

The source code of running the original clean run is in  `./FABI/SWE/script`

The source code for mutation is in   `./FABI/{dataset}/RIPPLE/mutation_script`

To run the original dataset for clean profile, please run `bash ./FABI/SWE/script/launch_lite_gpt54mini_run1.sh`

To generate mutant for inference and evalutaion, please run `./FABI/{dataset}/RIPPLE/mutation_script/launch.sh`


## Experiments Result & Reproduction
The results of mining is in `./FABI/Mining`

The results of clean run experiment is in `./FABI/{dataset}/original_passed_cases`

The results of mutation experiment is in `./FABI/{dataset}/RIPPLE/mutation_result`

## Supplimentary Results
The detailed case study for Fig. 1 is in `./Supplyment_results/Fig1_case_study-cache-key-slash.md`

The detailed case study for the pydata__xarray-4094 illustrated in RQ2 is in `./Supplyment_results/pydata__xarray-4094_case_study.md`

The cost results for clean execution is in `./Supplyment_results/clean_execution_cost_results`

The cost results for mutation execution is in `./Supplyment_results/mutation_execution_cost_results`

The case study for RQ2 is in `./Supplyment_results/detailed_case_study_failures`