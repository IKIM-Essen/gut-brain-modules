# No threading, no sleep

import pandas as pd
import requests
import time
import threading


download_URL = "https://www.ebi.ac.uk/metagenomics/api/v1/genome-catalogues/human-gut-v2-0/genomes?format=json"

r = requests.get(download_URL)
data = r.json()
pages_total = data["meta"]["pagination"]["pages"]
IDs = list()

limiter_for_testing = pages_total - 2 # integrating a limiter to test for only 2 pages (not all, for management reason)



for i in range(1, pages_total + 1): # limiter_for_testing needs to be taken out for final code
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
    download_tag = str(ID) + ".gff"
    for element in innerscope:
        if element["links"]["self"].endswith(download_tag):
            download_links_list.append(element["links"]["self"])

data_frame = {
    "sample_name": IDs,
    "url": download_links_list
}

df = pd.DataFrame(data_frame)

df.to_csv("config/pep//UHGG_human-gut-v2-0_genomes.csv", index = False)