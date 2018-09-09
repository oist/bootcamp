import os

def print_exercise(n):
    print("-"*15, "exercise", n, "-"*15)

def ex1():
    print_exercise(1)
    """
    In the folder files and all of its subfolders, replace all spaces from all
    the text files names into underscores. Ex: 001 740.txt => 001_740.txt
    """
    for root, dirs, files in os.walk("files"):
        for file in files:
            if ".txt" in file:
                file2 = file.replace(" ", "_")
                os.rename(os.path.join(root, file), os.path.join(root, file2))


def ex2():
    print_exercise(2)
    """
    append the name of the all the text files to the end of the text files.
    """
    for root, dirs, files in os.walk("files"):
        for file in files:
            if ".txt" in file:
                with open(file, "a") as f:
                    f.write(file)


def ex3():
    print_exercise(6)
    """
    for each name in “order.txt”, make a numbered directory
        Ex: “01 - John Doe”
    """
    with open("order.txt","r") as f:
        for i, name in enumerate(f):
            folder="{:02d} - {}".format(i+1, name.strip())
            print(folder)
            if not os.path.exists("./"+folder):
                os.makedirs("./"+folder)
