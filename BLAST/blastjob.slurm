#!/bin/bash

#SBATCH --job-name=BLAST
#SBATCH --time=00:30:00
#SBATCH --mem-per-cpu=1G
#SBATCH --ntasks=1
#SBATCH --mail-user=
#SBATCH --mail-type=BEGIN,FAIL,END
#SBATCH --output=job_%j.out

module load ncbi-blast

blastn -db data/database/My16sAmplicon -query data/MyQuery.fa -outfmt 7 -out data/results.out
