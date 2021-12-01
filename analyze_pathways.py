'''
##  Name:
        analyze_pathways.py

##  Version: [1.1]

##  Author:
        Cristina Sotomayor <cristina@lcg.unam.mx>

##  Created: [2021-11-29]

##  Description:
        Given pathway ID or list of pathway IDs, obtain data from KEGG database
        and write a csv file for each pathway.

##  Usage:
        python analyze_pathways.py --ids id1 [id2, id3, ...]

##  Arguments:
        -i --ids Pathway IDs to look up in KEGG database. Three letter organism
                 code + 5 digit identifier each, separated by spaces.
        -h --help Print help file

##  Requirements:
        os, pandas, argparse, Bio.KEGG
        genes, pathways and DataFrame submodules from this module

## Example:
        python analyze_pathways.py --ids hsa05203

'''

import os
import argparse
import pandas as pd

from genes import *
from pathways import *
from attributes import *


## Arguments
# Create parser to read arguments from command line
parser = argparse.ArgumentParser(description="Given pathway IDs, save information "
                                "from KEGG database as csv for each pathway. ")

# Add arguments
parser.add_argument("-i", "--ids", nargs='+',
                    help="Pathway IDs, three letter organism code + five digit "
                         "identifier each, separated by a space",
                    required=True)
parser.add_argument("-p", "--path",
                    help="Path to save csv files. If not given, saved in cwd ",
                    required=False)

args = parser.parse_args()

# Iterate over given IDs and save data for each one
for pathway_id in args.ids:
    # Get information from database, and obtain individual genes
    pathway = get_pathway(pathway_id)

    # If pathway was found, save genes, if not, go to next pathway_id
    if pathway:
        genes = parse_pathway(pathway)
    else:
        continue

    # Turn information into a DataFrame
    df_genes = list_to_data(genes)

    # Path, if given, save there, else, save in current directory
    if args.path:
        path = os.path.join(args.path, f'{pathway_id}.csv')
    else:
        path = f'{pathway_id}.csv'

    # Save DataFrame
    df_genes.to_csv(path, index=False)
