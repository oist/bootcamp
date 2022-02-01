#!/bin/bash

#SBATCH -p short
#SBATCH -t 1:00:00
#SBATCH --mem=16G
#SBATCH -c 8
#SBATCH --job-name=BootcampBlast
#SBATCH --output=Bootcamp-%j.out
#SBATCH --error=Bootcamp-%j.err
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=jeremie.gillet@oist.jp


module load ncbi-blast/2.10.0+ 

blastn -db /apps/unit/GradschoolD/blast/human_genome/GCF_000001405.38_top_level \
       -query random_sequences.fa \
       -out out.txt \
       -outfmt 7 \
       -word_size 7 \
       -evalue 50

