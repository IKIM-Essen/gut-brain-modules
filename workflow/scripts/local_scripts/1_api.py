# No threading, no sleep

import pandas as pd
import requests
import time
import threading


download_URL = "https://www.ebi.ac.uk/metagenomics/api/v1/genome-catalogues/human-gut-v2-0/genomes?format=json" # &size=-1 as a solution?

r = requests.get(download_URL)
data = r.json()
pages_total = data["meta"]["pagination"]["pages"]
IDs = list()
taxon_lineage = list()

limiter_for_testing = pages_total - 1 # integrating a limiter to test for only 4 pages (not all, for management reason)



for i in range(1, pages_total + 1 - limiter_for_testing): # limiter_for_testing needs to be taken out for final code
    current_URL = download_URL + "&page=" + str(i)
    r = requests.get(current_URL)
    data = r.json()
    innerscope = data["data"]
    for result in innerscope:
        taxon_lineage.append(result["attributes"]["taxon-lineage"])
        IDs.append(result["id"])


download_links_list = list()
for ID in IDs:
    download_request_raw = requests.get("https://www.ebi.ac.uk/metagenomics/api/v1/genomes/" + str(ID) + "/downloads")
    download_request = download_request_raw.json()
    innerscope = download_request["data"]
    download_tag = str(ID) + ".gff"
    for element in innerscope:
        if element["links"]["self"].endswith(download_tag):
            download_links_list.append(element["links"]["self"])

data_frame = {
    "sample_name": IDs,
    "taxon_lineage": taxon_lineage,
    "url": download_links_list
}

df = pd.DataFrame(data_frame)

df.to_csv("results/tables/UHGG_human-gut-v2-0_genomes.csv", index = False)