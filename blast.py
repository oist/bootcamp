"""
This file is a library for creating a BLAST query
"""

def make_script(query_path, db_path, output="", out_format=0):
    """
    This function creates a script for a BLAST query
    Input: query_path - Path of the FASTA file to query
           db_path - Path to the database to query in
           output - name of the output file. Default is blank (output to screen)
           out_format - format of the output. Default is 0.
                        Format description here https://www.ncbi.nlm.nih.gov/books/NBK279684/
    """

    script = "blastn"
    script = script + " -db " + db_path
    script = script + " -query " + query_path
    if output != "":
        script = script + " -out " + output
    script = script + " -outfmt {}".format(out_format)

    return script
