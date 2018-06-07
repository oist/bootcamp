#! /usr/local/bin/python3

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
    dic = {}                        # create a dictionnary
    with open(filepath) as f:       # open file
        header = ""                     # for saving a header
        fasta = ""                      # for saving a sequence
        for line in f:                      # read each line
            if line[0] == ">":                  # if line is a header
                if fasta != "":                     # if there is a sequence saved
                    dic[header]=fasta                   # add the sequence to the dictionary
                    fasta = ""                          # reset the sequence
                header = line[1:].strip()           # save the header
            else:                               # line is a sequence
                fasta += line.strip()               # adds the chunk of sequence
    return dic

def filter_FASTA(dic, header_criterion):
    """
    This function filters the sequences in a dictionary according to a given
    criterion on their headers
    Input: dic - dictionnary of header: sequence
           header_criterion - Boolean function that takes in a string
    Returns: dictionnary of header: sequence
    """
    return { h:dic[h] for h in dic if header_criterion(h)}

def write_FASTA(dic, filepath):
    """
    This function writes a FASTA file from a dictionary
    Input: dic - dictionnary of header: sequence
           filepath - path to the file to write
    Returns: Nothing
    """
    with open(filepath, "w") as f:       # open file
        for header in dic:                  # for each sequence
            f.write(">" + header + "\n")        # write the header
            seq = dic[header]                   # extract the sequence
            while seq != "":                    # while there is some sequence left
                f.write(seq[:70] + "\n")            # write 70 characters
                seq = seq[70:]                      # cuts the 70 charachers
