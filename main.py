from genericpath import isdir
import os

#fixed "looses subdirs for GeomID"
#bugs: 1.file counter works wrong 2.ignores old xmls
#todo: relative paths, terminal args

#temp global vars
template_path = r"C:\\d\\template.xml"
placeholder = "placeholder"
path_placeholder = "PATH_PLACEHOLDER"
file_count = 0

def dir_processor(dir_path):
    # Iterate target directory    
    for path in os.listdir(dir_path):
        # check if current path is a folder        
        joined_path = os.path.join(dir_path, path)
        if os.path.isdir(joined_path):
            dir_processor(joined_path)
        if os.path.isfile(joined_path):
            file_processor(dir_path, path)

def file_processor(dir_path, path):
    #checks only for igs files
    if ".igs" in path.lower():
        base_name = path.lower().removesuffix(".igs")
        xml_name = base_name + ".xml"
        #check if xml already exists
        if not os.path.exists(xml_name):
            with open(template_path,'r') as template_file, open(os.path.join(dir_path, xml_name), 'w') as new_xml:                        
                for line in template_file:
                    #print(type(line))                           
                    if placeholder in line:
                        line = line.replace(placeholder,base_name)
                    #else:
                        #print(f"No {placeholder} in file")
                    if path_placeholder in line:
                        adapted_path = adapt_path(os.path.join(dir_path, path))
                        line = line.replace(path_placeholder,adapted_path)
                    #else:
                        #print(f"No {placeholder} in file")
                    #print(os.path.join(dir_path, path))                
                    new_xml.write(line)
            global file_count
            file_count = file_count + 1
            new_xml.close()
            template_file.close()
            print("file \'" + xml_name + "\' created.")
        else:
            print("file \'" + xml_name + "\' exists.")

def adapt_path(dir_path):
    dir_path = dir_path.lower().split(r"\\")
    x = 0 # iterator
    skip = 0 # skip flag
    path = 0 # flag and path, init with 0 so there won't be opening with backslash
    while x < len(dir_path):    
        if dir_path[x] == "source": #called once we find TS specific dir
            if skip == 1:
                #bad path, there should be only one source dir
                print("path is incorrect. source dir is doubled")
            x = x + 3
            skip = 1
        if skip == 1:
            #print(dir_path[x])
            if path == 0:
                path = dir_path[x]
            else:
                path = path + "\\" + dir_path[x]
        x = x + 1
    return path    

def xml_creator():    
    # folder path
    dir_path = r"C:\\d\\" 
    
    # list to store files
    # res = []
    dir_processor(dir_path)

    print(str(file_count) + " files created")

if __name__ == "__main__":
    xml_creator()