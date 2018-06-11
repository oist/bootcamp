"""
This file is a library for creating a BLAST query
"""

def make_script(query_path, db_path, output="", out_format=0):
    """
    This function creates a script for a BLAST query
    Input: query_path - Path of the FASTA file to query
           db_path - Path to the database to query in
           output - name of the output file. Default is blank (output to screen)
           out_format - format of the output.
                        Format description here https://www.ncbi.nlm.nih.gov/books/NBK279684/
    """

    if output != "":
         output= " -out {}".format(output)

    modules = "module load ncbi-blast"

    blast = "blastn -db {db} -query {qry} -outfmt {fmt} {out}"\
            .format(qry=query_path, db=db_path, out=output, fmt=out_format)

    return "{}\n\n{}".format(modules, blast)
