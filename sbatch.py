"""
This file is a library for creating a sbatch job script
"""

template = """
#!/bin/bash

#SBATCH --job-name={name}
#SBATCH --partition=compute
#SBATCH --time=00:30:00
#SBATCH --mem-per-cpu=1G
#SBATCH --ntasks=1
#SBATCH --mail-user={mail}
#SBATCH --mail-type=BEGIN,FAIL,END
#SBATCH --input=none
#SBATCH --output=job_%j.out
#SBATCH --error=job_%j.err

{script}"""

def create_script(out_path="MyJob.sh", jobname="Jobby McJobFace", mail="", script=""):
    """
    This function creates a sbatch job script file given a script to run.
    Input: out_path - path to the output.
           jobname - name of the job. Note: spaces will be removed
           mail - email of the user.
           script - bash script to run on the cluster.
    """

    jobname = "".join(jobname.split()) # Quick way to remove all white spaces

    job = template.format(name=jobname, mail=mail, script=script)

    with open(out_path, "w") as f:
        f.write(job)
