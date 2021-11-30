'''
##  Name:
        read_data.py

##  Version: [2.0]

##  Authors:
        Luz Rosario Guevara <lguevara@lcg.unam.mx>
        Cristina Sotomayor <cristina@lcg.unam.mx>

##  Created: [2021-11-28]

##  Description:
        Functions to read data from pathways.

##  Usage:
        python read_data.py

##  Arguments:
        None

##  Requirements:
        pandas

## Example

    Input:
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

def ReadPathways(path):
    """Read DataFrame with pathway gene data to obtain data in correct format.

    Parameters:
        - path (str): path where csv file with pathway data is stored

    Returns:
        - DataFrame with data in correct format

    """
    df = pd.read_csv(path)

    # If name has format ['(RefSeq) name'], remove punctuation and RefSeq
    if "'" in df.Name[0]:
        df.Name = df.Name.apply(lambda x: x.split("'")[1])
        df.Name = df.Name.apply(lambda x: x.replace("(RefSeq) ", ""))

    # Read Pathways col as list
    df.Pathways = df.Pathways.apply(eval)

    return df

def SplitData(df):
    """For DataFrames with list of pathways, return DataFrame with one line per
    pathway.

    Parameters:
        - df (DataFrame): DataFrame with pathway data, as obtained from
                        ListToData or ReadPathways functions

    Returns:
        - New DataFrame with one row for each pathway in each gene's pathway list.

    """
    # List to save entries
    pathway_list = []

    # Each line in df corresponds to one gene
    for index, gene in df.iterrows():
        # List containing (id, pathway name) pairs
        pathways = gene.Pathways
        # Save each as a line
        for code, pathway in pathways:
            pathway_list.append([gene.Entry, gene.Name, code, pathway])

    # Create new DataFrame
    df_pathways = pd.DataFrame(pathway_list, columns=['Gene_ID', 'Gene_Name',
                                                'Pathway_ID', 'Pathway_Name'])

    return df_pathways
