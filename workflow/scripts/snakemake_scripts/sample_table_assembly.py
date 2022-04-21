import pandas as pd
import requests

with open(snakemake.input[0], "r") as input:
    IDs = input.readlines()
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

    df.to_csv(snakemake.output[0], index = False)