import requests


download_URL = "https://www.ebi.ac.uk/metagenomics/api/v1/genome-catalogues/human-gut-v2-0/genomes?format=json"


r = requests.get(download_URL)
data = r.json()
pages_total = data["meta"]["pagination"]["pages"]
IDs = list()

for i in range(1, pages_total + 1):
    current_URL = download_URL + "&page=" + str(i)
    r = requests.get(current_URL)
    data = r.json()
    innerscope = data["data"]
    for result in innerscope:
        IDs.append(result["id"])

print(IDs)