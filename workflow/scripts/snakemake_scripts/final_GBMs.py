import pandas as pd
import json
import csv

with open(snakemake.input.GBMs, "r") as input_1:
    GBMs_in_Microorganisms = json.load(input_1)

with open(snakemake.input.combinations, "r") as input_2:
    GBM_combinations = json.load(input_2)

GBM_ID_list = []
for GBM_IDs in GBM_combinations.keys():
    GBM_ID_list.append(GBM_IDs)

for GBMs in GBM_ID_list:
    for species, identified_GBMs in GBMs_in_Microorganisms.items():
        if GBMs not in GBMs_in_Microorganisms[species]:
            GBMs_in_Microorganisms[species][GBMs] = [0]

json_object = json.dumps(GBMs_in_Microorganisms, sort_keys = True, indent = 4)

with open(snakemake.output[0], "w") as output:
    output.write(json_object)

df = pd.read_json(snakemake.output[0], orient = "index")
df.to_csv(snakemake.output[1])