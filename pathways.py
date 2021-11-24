'''

##  Name:
        pathways.py

##  Version: [1.0]

##  Author:
        Cristina Sotomayor <cristina@lcg.unam.mx>

##  Created: [2021-11-23]

##  Description:
        Functions to download, read and store pathway data from KEGG pathway
        database.

##  Usage:
        python pathways.py

##  Arguments:
        None

##  Requirements:
        Bio.KEGG

## Example

'''

from Bio.KEGG.KGML import KGML_parser
from Bio.KEGG.REST import kegg_get

from genes import GetGenes


def GetPathway(kegg_id):
    """
    Gets pathway from KEGG database, reads data and returns Pathway object.

    Parameters:
        - kegg_id (string): KEGG identifier for the pathway, organism code + five
        digit number

    Returns:
        - Pathway object
    """
    # Look for kegg_id, if not found, alert user and exit function
    try:
        result = kegg_get(kegg_id, 'kgml').read()
    except:
        print('Pathway file not found. Check KEGG ID and try again. ')
        return

    # If kegg_id is found and kgml file read, turn into Pathway object
    pathway = KGML_parser.read(result)
    return pathway
