import pandas as pd

# helper functions


def get_samples():
    print(list(pep.sample_table["sample_name"].values))
    return list(pep.sample_table["sample_name"].values)


def get_urls():
    print(list(pep.sample_table["url"].values))
    return list(pep.sample_table["url"].values)
