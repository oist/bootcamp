"""
This file is a library for manipulating FASTA files.
It can:
  - Read FASTA files and save them as dictionnaries
  - Filter sequences in a dictionnary
  - Write FASTA files from dictionnaries
"""

def parse_FASTA(filepath):
    """
    This function reads and parses a FASTA file.
    Input: filepath - path to the FASTA file (string)
    Returns: dictionary of sequence name (AKA header, without the '>')
             associated with the sequence (without newlines)
    """

def filter_FASTA(dic, header_criterion):
    """
    This function filters the sequences in a dictionary according to a given
    criterion on their headers
    Input: dic - dictionnary of header: sequence
           header_criterion - Boolean function that takes in a string
    Returns: dictionnary of header: sequence
    """

def write_FASTA(dic, filepath):
    """
    This function writes a FASTA file from a dictionary
    Input: dic - dictionnary of header: sequence
           filepath - path to the file to write
    Returns: Nothing
    """
