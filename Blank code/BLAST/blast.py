"""
This file is a library for creating a BLAST query and slurm job
"""

def blast_query(query_path, db_path, output="", out_format=0):
    """
    This function creates a script for a BLAST query
    Input: query_path - Path of the FASTA file to query
           db_path - Path to the database to query in
           output - name of the output file. Default is blank (output to screen)
           out_format - format of the output.
                        Format description here https://www.ncbi.nlm.nih.gov/books/NBK279684/
    """

sbtach_template = """
#!/bin/bash

#SBATCH --job-name={name}
#SBATCH --time=00:30:00
#SBATCH --mem-per-cpu=1G
#SBATCH --ntasks=1
#SBATCH --mail-user={mail}
#SBATCH --mail-type=BEGIN,FAIL,END
#SBATCH --output=job_%j.out

{script}"""

def sbtach_job(out_path="MyJob.slurm", jobname="Jobby McJobFace", mail="", script=""):
    """
    This function creates a sbatch job script file given a script to run.
    Input: out_path - path to the output.
           jobname - name of the job. Note: spaces will be removed
           mail - email of the user.
           script - bash script to run on the cluster.
    """
