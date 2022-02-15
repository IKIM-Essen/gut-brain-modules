# Sample table assembly from the UHGG Human Gut v2.0 catalogue

import pandas as pd
import requests
import time
import threading
# No threading, no sleep
# could not implement time and threading... yet!


download_URL = "https://www.ebi.ac.uk/metagenomics/api/v1/genome-catalogues/human-gut-v2-0/genomes?format=json"

r = requests.get(download_URL)
data = r.json()
pages_total = data["meta"]["pagination"]["pages"]
IDs = list()

limiter_for_testing = pages_total - 2   # integrating a limiter to test for only 2 pages (not all, for management/testing reason)



for i in range(1, pages_total + 1 - limiter_for_testing):   # limiter_for_testing needs to be taken out for final code
    current_URL = download_URL + "&page=" + str(i)
    r = requests.get(current_URL)
    data = r.json()
    innerscope = data["data"]
    for result in innerscope:
        IDs.append(result["id"])


download_links_list = list()
for ID in IDs:
    download_request_raw = requests.get("https://www.ebi.ac.uk/metagenomics/api/v1/genomes/" + str(ID) + "/downloads")
    download_request = download_request_raw.json()
    innerscope = download_request["data"]
    for element in innerscope:
        if ".gff" in element["links"]["self"]:
            download_links_list.append(element["links"]["self"])

data_frame = {
    "sample_name": IDs,
    "url": download_links_list
}

df = pd.DataFrame(data_frame)

df.to_csv("/local/work/ata/gut-brain-modules/config/pep/UHGG_human-gut-v2-0_genomes.csv", index = False) # path can be rewritten with snakemake concepts
