########## STEP 1 ##########
# We have two files with raw sequences we want to search, raw1.fa and raw2.fa
# We are only interesetd in the fungi or Bacillus sequences
# We need to read both files, extract the fungi sequences and write them to a new file

import os
import fasta

raw_data_path = "data/raw/"
db_path = "data/database/My16sAmplicon"
query_path = "data/MyQuery.fa"
script_output = "data/blastjob.slurm"
result_path = "data/results.out"

species = {}
for root, dirs, files in os.walk(raw_data_path):
    for file in files:
        if ".fa" in file:
            tmp = fasta.parse_FASTA(root + file)
            species.update(tmp) # Adding the values of tmp to d

def filter_function(header):
    return "fungi" in header or "Bacillus" in header

print("\nRaw sequences before filtering:")
for h in species:
    print(h)

species = fasta.filter_FASTA(species, filter_function)

print("\nRaw sequences after filtering:")
for h in species:
    print(h)

fasta.write_FASTA(species, query_path)
print("\nQuery FASTA file written in {}.".format(query_path))

########## STEP 2 ##########
# Prepare a SLURM file to run the query on Tombo

import blast

fmt = 6 # tabular output
name = "BLAST" # Name of the job
mail = "" # Add your email here

blastscript = blast.blast_query(query_path, db_path, result_path, fmt)

blast.sbtach_job(script_output, name, mail, blastscript)

print("sbatch script created. Run with \"sbatch {}\"".format(script_output))
