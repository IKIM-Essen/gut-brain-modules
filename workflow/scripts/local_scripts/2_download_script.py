import json

with open("../../../results/files/GBM_combinations.json", "r") as input:
    GBM_combinations = json.load(input)

import pandas as pd
import requests

df = pd.read_csv("../../../results/tables/UHGG_human-gut-v2-0_genomes.csv")

GBMs_in_microorganisms = dict()
for index, row in df.iterrows():
    genome_ID = row["sample_name"]
    taxon_lineage = row["taxon_lineage"]
    url = row["url"]
    r = requests.get(url, allow_redirects=True)
    file_to_save = "../../../results/genomes/gff_files/" + genome_ID + ".gff"
    open(file_to_save, 'wb').write(r.content)

    with open("../../../results/genomes/gff_files/" + genome_ID + ".gff", "r") as input_file:
        gff_file = input_file.read()
        GBMs_in_microorganisms[taxon_lineage] = dict()
        for GBM_ID, reaction_dict in GBM_combinations.items():
            for combination_nr, combination_list in reaction_dict.items():
                for reaction in combination_list:
                    if "," in reaction:
                        for i in reversed(range(len(combination_list))):
                            combination_list[i:i+1] = combination_list[i].split(",")
                if all(combination in gff_file for combination in combination_list):
                    if GBM_ID not in GBMs_in_microorganisms[taxon_lineage]:
                        GBMs_in_microorganisms[taxon_lineage][GBM_ID] = [int(combination_nr)]
                    elif GBM_ID in GBMs_in_microorganisms[taxon_lineage]:
                        GBMs_in_microorganisms[taxon_lineage][GBM_ID].append(int(combination_nr))


json_object = json.dumps(GBMs_in_microorganisms, sort_keys = True, indent = 4)

with open("../../../results/files/GBMs_in_Microorganisms.json", "w") as output:
    output.write(json_object)