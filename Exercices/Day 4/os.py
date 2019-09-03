import os

"""     .
       ,O,
      ,OOO,
'oooooOOOOOooooo'
  `OOOOOOOOOOO`
    `OOOOOOO`
    OOOO'OOOO
   OOO'   'OOO
  O'         'O
"""

"""
Print the names of all the files in the "files" folder
"""
for root, dirs, files in os.walk("files"):
    for file in files:
        print(file)

"""     .                 .
       ,O,               ,O,
      ,OOO,             ,OOO,
'oooooOOOOOooooo' 'oooooOOOOOooooo'
  `OOOOOOOOOOO`     `OOOOOOOOOOO`
    `OOOOOOO`         `OOOOOOO`
    OOOO'OOOO         OOOO'OOOO
   OOO'   'OOO       OOO'   'OOO
  O'         'O     O'         'O
"""

"""
In the folder "files/moreFiles" and all of its subfolders, replace all spaces from all
the text files names into underscores. Ex: 001 740.txt => 001_740.txt
"""
for root, dirs, files in os.walk("files"):
    for file in files:
        if ".txt" in file:
            file2 = file.replace(" ", "_")
            os.rename(os.path.join(root, file), os.path.join(root, file2))


"""
append the name of the all the text files to the end of the text files.
"""
for root, dirs, files in os.walk("files"):
    for file in files:
        if ".txt" in file:
            with open(file, "a") as f:
                f.write(file)


"""
for each name in “files/order.txt”, make a numbered directory
    Ex: “01 - John Doe”
"""
with open("order.txt","r") as f:
    for i, name in enumerate(f):
        folder="{:02d} - {}".format(i+1, name.strip())
        print(folder)
        if not os.path.exists("./"+folder):
            os.makedirs("./"+folder)
