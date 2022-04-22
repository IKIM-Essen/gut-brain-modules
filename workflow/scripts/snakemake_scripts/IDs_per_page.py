import requests


download_URL = "https://www.ebi.ac.uk/metagenomics/api/v1/genome-catalogues/human-gut-v2-0/genomes?format=json"

r = requests.get(download_URL)
data = r.json()
pages_total = data["meta"]["pagination"]["pages"]
IDs = list()

limiter_for_testing = (
    pages_total - 2
)  # integrating a limiter to test for only 2 pages (not all, for management reason)


for i in range(
    1, pages_total + 1
):  # limiter_for_testing needs to be taken out for final code
    current_URL = download_URL + "&page=" + str(i)
    r = requests.get(current_URL)
    data = r.json()
    innerscope = data["data"]
    for result in innerscope:
        IDs.append(result["id"])

# with open(snakemake.output[0], "w") as output:
#     for i in IDs:
#         output.write(i + "\n")

# snakemake.wildcards.page_ID
