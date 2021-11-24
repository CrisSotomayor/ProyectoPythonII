'''

##  Name:
        genes.py

##  Version: [1.0]

##  Author:
        Cristina Sotomayor <cristina@lcg.unam.mx>

##  Created: [2021-11-23]

##  Description:
        Functions to download, read and store gene data from KEGG pathway
        database.

##  Usage:
        python genes.py

##  Arguments:
        None

##  Requirements:
        Bio.KEGG, pandas

## Example

'''
from Bio.KEGG.REST import kegg_get
from Bio.KEGG.Gene import parse


def GetGenes(kegg_id):
    """
    Gets genes from KEGG database, reads data and returns Gene object.

    Parameters:
        - kegg_id (string): KEGG identifier for the gene, organism code + five
        digit number

    Returns:
        - Gene object
    """
    # Look for kegg_id, if not found, alert user and exit function
    try:
        result = kegg_get(kegg_id)
    except:
        print('Gene file not found. Check KEGG ID and try again. ')
        return

    # If kegg_id is found and file read, parse result to get gene objects
    genes = [gene for gene in parse(result)]

    if len(genes) == 1:
        return genes[0]
    else:
        return genes
