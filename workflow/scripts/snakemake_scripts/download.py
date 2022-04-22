import json

with open(snakemake.input.combinations, "r") as input:
    GBM_combinations = json.load(input)

import pandas as pd

df = pd.read_csv(snakemake.input.sample_table)

GBMs_in_microorganisms = dict()
for i, s in zip(snakemake.input.gff_files, snakemake.params.samples):
    taxon_lineage = df.loc[df["sample_name"] == s, "taxon_lineage"].iloc[0]
    with open(i, "r") as input_file:
        gff_file = input_file.read()
        GBMs_in_microorganisms[taxon_lineage] = dict()
        for GBM_ID, reaction_dict in GBM_combinations.items():
            for combination_nr, combination_list in reaction_dict.items():
                if all(combination in gff_file for combination in combination_list):
                    if GBM_ID not in GBMs_in_microorganisms[taxon_lineage]:
                        GBMs_in_microorganisms[taxon_lineage][GBM_ID] = [
                            int(combination_nr)
                        ]
                    elif GBM_ID in GBMs_in_microorganisms[taxon_lineage]:
                        GBMs_in_microorganisms[taxon_lineage][GBM_ID].append(
                            int(combination_nr)
                        )


json_object = json.dumps(GBMs_in_microorganisms, sort_keys=True, indent=4)

with open(snakemake.output[0], "w") as output:
    output.write(json_object)
