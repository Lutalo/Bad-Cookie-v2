#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata

import pprint

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.sfgov.org", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.sfgov.org,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
#results = client.get("cuks-n6tp", limit=2000)
results = client.get("cuks-n6tp", limit=100)

# Convert to pandas DataFrame
#results_df = pd.DataFrame.from_records(result_list)
results_df = pd.DataFrame.from_records(results)

#print(results_df)
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(results[0])
