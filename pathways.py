'''

##  Name:
        pathways.py

##  Version: [2.1]

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

## Example:
        pathway = GetPathway('hsa05203')
        genes = ParsePathway(pathway)

'''

from Bio.KEGG.KGML import KGML_parser
from Bio.KEGG.REST import kegg_get

from genes import GetGenes


def GetPathway(kegg_id):
    """Gets pathway from KEGG database, reads data and returns Pathway object.

    Parameters:
        - kegg_id (string): KEGG identifier for the pathway, organism code + five
        digit number

    Returns:
        - Pathway object as defined in KEGG.KGML
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


def ParsePathway(pathway):
    """Gets Pathway object, iterates over genes found in it, and returns list with
    Gene objects for those genes.

    Parameters:
        - pathway (Pathway): pathway from KEGG database as returned by GetPathway
                function

    Returns:
        - List with genes as Gene objects from Bio.KEGG.Gene
    """
    # List to store genes
    genes = []

    for entry in pathway.genes:
        # Some entries return codes separated by spaces, replace for + to find
        # them in database
        entry = entry.name.replace(' ', '+')
        gene = GetGenes(entry)
        # If GetGenes was successful
        if gene:
            genes.extend(gene)

    return genes
