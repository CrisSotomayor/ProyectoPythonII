'''

##  Name:
        genes.py

##  Version: [2.1]

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
        gene = GetGenes('hsa:7157')

'''
from Bio.KEGG.REST import kegg_get
from Bio.KEGG.Gene import *


class Gene(Record):
    """Class to hold Gene object. Modified from KEGG.Gene.Record (Copyright
    2017 by Kozo Nishida.  All rights reserved.) to include pathway data.

    Attributes:
     - entry       The entry identifier.
     - name        A list of the gene names.
     - definition  The definition for the gene.
     - orthology   A list of 2-tuples: (orthology id, role)
     - organism    A tuple: (organism id, organism)
     - position    The position for the gene
     - motif       A list of 2-tuples: (database, list of link ids)
     - dblinks     A list of 2-tuples: (database, list of link ids)
     - pathways    A list of 2-tuples: (pathway id, name)

    """
    def __init__(self):
        """Initialize new Gene object from Record object. """
        super().__init__()

        # Adding pathway data
        self.pathways = []


def ParseGenes(handle):
    """Parse KEGG Gene file and return iterable. Modified from KEGG.Gene.parse
    (Copyright 2017 by Kozo Nishida.  All rights reserved.).

    Parameters:
        - kegg_id (string): KEGG identifier for the gene, organism code + five
        digit number

    Returns:
        - Iterable over Gene objects
    """
    record = Gene()  # Gene calls Record class
    # Original code Copyright 2017 by Kozo Nishida.  All rights reserved.
    for line in handle:
        if line[:3] == "///":
            yield record
            record = Gene()
            continue
        if line[:12] != "            ":
            keyword = line[:12]
        data = line[12:].strip()
        if keyword == "ENTRY       ":
            words = data.split()
            record.entry = words[0]
        elif keyword == "NAME        ":
            data = data.strip(";")
            record.name.append(data)
        elif keyword == "DEFINITION  ":
            record.definition = data
        elif keyword == "ORTHOLOGY   ":
            id, name = data.split("  ")
            orthology = (id, name)
            record.orthology.append(orthology)
        elif keyword == "ORGANISM    ":
            id, name = data.split("  ")
            organism = (id, name)
            record.organism = organism
        elif keyword == "POSITION    ":
            record.position = data
        elif keyword == "MOTIF       ":
            key, values = data.split(": ")
            values = values.split()
            row = (key, values)
            record.motif.append(row)
        elif keyword == "DBLINKS     ":
            if ":" in data:
                key, values = data.split(": ")
                values = values.split()
                row = (key, values)
                record.dblinks.append(row)
            else:
                row = record.dblinks[-1]
                key, values = row
                values.extend(data.split())
                row = key, values
                record.dblinks[-1] = row

        # Modified, read pathways in file, store ID : name pairs
        elif keyword == "PATHWAY     ":
            if "  " in data:
                key, value = data.split("  ")
                row = (key, value)
                record.pathways.append(row)

def GetGenes(kegg_id):
    """Gets genes from KEGG database, reads data and returns list with Gene
    objects.

    Parameters:
        - kegg_id (string): KEGG identifier for the gene

    Returns:
        - List with Gene objects.
    """
    # Look for kegg_id, if not found, alert user and exit function
    try:
        handle = kegg_get(kegg_id)
    except:
        print('Gene file not found. Check KEGG ID and try again. ')
        return

    # If kegg_id is found and file read, parse result to get Gene objects
    genes = [gene for gene in ParseGenes(handle)]

    return genes
