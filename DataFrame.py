'''
##  Name:
        DataFrame.py
##  Version: [1.1]
##  Author:
        Cristina Sotomayor <cristina@lcg.unam.mx>
        Luz Rosario Guevara <lguevara@lcg.unam.mx>

##  Created: [2021-11-28]
##  Description:
        Function to read list from genes.py and store genes and attributes as data frame with
        pandas.
##  Usage:
        python DataFrame.py
##  Arguments:
        None
##  Requirements:
        pandas
## Example

    Imput:
    genes
        Function:
        ListToData(Genes)
    Output:
    df

'''

import pandas as pd

def ListToData(genes):
    """Gets object´s list "genes" from genes.py, and returns Data Frame with named attributes.
        Parameters:
            - genes (list):  List with genes as Gene objects from Bio.KEGG.Gene

        Returns:
            - df (DataFrame): DataFrame made with gene´s attributes ('Entry',
            'Name', 'Position', 'Pathways')
        """
    # List to store Genes and mains attributes
    gene_list = []

    for gene in genes:
        # Store entries of mains attributes of the object gene of genes
        Entry = gene.entry
        Name = gene.name
        Pos = gene.position
        Path = gene.pathways

        # Append entries to empty list
        gene_list.append([Entry, Name, Pos, Path])

    # Convert list to DataFrame and name the columns 
    df = pd.DataFrame(gene_list, columns=['Entry', 'Name', 'Position', 'Pathways'])
    return df