import os

line = "//Brogan Jowers-Wilding: 1538252\n"

#Looks through all the files starting at the current working directory that end in .ts
for root, dirs, files in os.walk(os.getcwd()):
    #Removes the node_modules directory as shouldn't be changing these and are already in the git ignore 
    if("node_modules" in dirs):
        dirs.remove("node_modules")
        print("Skipped directory##############")
    for filename in files:
        if filename.endswith(".ts"):
             with open(os.path.join(root, filename), 'r+', encoding='utf-8') as f:
                #Checks if the firstline is already commented 
                if(f.readline() != line): 
                    content = f.read()
                    f.seek(0, 0)
                    f.write(line.rstrip('\r\n') + '\n' + content)
                    print(os.path.join(root, filename))
                else:
                    print(filename + "Line already commented skipping")