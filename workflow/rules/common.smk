import pandas as pd

# helper functions


def get_samples():
    return list(pep.sample_table["sample_name"].values)


def get_urls():
    print("this prints:", list(pep.sample_table["url"].values)[0])
    return list(pep.sample_table["url"].values)


def get_url_for_sample(wildcards):
    return pep.sample_table.loc[wildcards.sample, "url"]
