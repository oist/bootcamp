#! /usr/local/bin/python3

"""
This file is a library for creating a sbatch job script
"""

def import_template(filepath):
    """
    This function returns the template located at filepath as a string.
    """
    with open(filepath, "r") as f:
        return f.read()

def export_script(filepath, script):
    """
    This function writes the sbatch job script to a filepath
    """
    with open(filepath, "w") as f:
        f.write(script)

def create_script(template_path, out_path="MyJob.sh", jobname="My_Job", mail="", script=""):
    """
    This function creates a sbatch job script file given a script to run.
    Input: template_path - path to the template
           out_path - path to the output. Default is MyJob.sh
           jobname - name of the job. Default is "My_Job". Note: spaces will be removed
           mail - email of the user. Default is blank.
           script - script to run on the cluster.
    """
    template = import_template(template_path)

    jobname = "".join(jobname.split()) # Quick way to remove all white spaces

    template = template.replace("__JOBNAME__", jobname)
    template = template.replace("__USERMAIL__", mail)
    template = template.replace("__SCRIPT__", script)

    export_script(out_path, template)
