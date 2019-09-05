# bootcamp
Code for the Programming Bootcamp

Data and commands are [adapted from here](https://github.com/edamame-course/BLAST-tutorial/blob/master/running-BLAST.md)

Steps to get things to work

0. Log into Tombo and create/move to a folder in `/work/scratch/`

1. Clone repo with `git clone https://github.com/oist/bootcamp.git` (note the use of https) then `cd bootcamp/BLAST`

2. Create the BLAST database: `makeblastdb -in data/database/Refsoil16s.fa -dbtype nucl -out data/database/My16sAmplicon`

3. Run `module load python/3.5.2`

4. Run `python3 fasta.py`

5. Run `sbatch blastjob.slurm`

6. Run `python3 analysis.py`
