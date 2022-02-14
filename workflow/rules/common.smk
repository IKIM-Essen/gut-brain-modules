import pandas as pd

# helper functions


def get_samples():
    return list(pep.sample_table["sample_name"].values)


def get_urls():
    return list(pep.sample_table["url"].values)
