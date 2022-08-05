import os

# folder path
dir_path = r'C:\\c\\'

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        pathtemp = path #using temp var in case I'll need full list later
        if ".igs" in pathtemp: #check only for igs files
            pathtemp.removesuffix(".igs")
            pathtemp = pathtemp + ".xml"
            #print(pathtemp)
            if not os.path.exists(pathtemp):
                open(dir_path + pathtemp, 'w')
                #os.mknod(pathtemp)
                #print("file \'" + pathtemp + "\' created.")
            #else:
                #print("file \'" + pathtemp + "\' exists.")
        #res.append(path) -- adds up to list
#print(res) -- total list