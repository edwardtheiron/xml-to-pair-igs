from genericpath import isdir
import os

#added __name__ == "__main__"
#added recursive dir processor
#fixed minor things
#bugs: looses subdirs for GeomID
#todo: relative paths, terminal args

#temp global vars
template_path = r"C:\\d\\template.xml"
placeholder = "placeholder"
file_count = 0

def dir_processor(dir_path):
    print(os.listdir(dir_path))
    # Iterate target directory    
    for path in os.listdir(dir_path):
        #print("path is " + path)
        # check if current path is a folder
        
        joined_path = os.path.join(dir_path, path)
        #print("joined_path is " + joined_path)
        if os.path.isdir(joined_path):
            #print("dir_processor: --" + dir_path + "--")
            dir_processor(joined_path)
        if os.path.isfile(joined_path):
            #print("file_processor: --" + dir_path + "-- and path --" + path + "--")
            file_processor(dir_path, path)

def file_processor(dir_path, path):
    print("FP's dir_path " + dir_path)
    print("FP's path     " + path)
    #checks only for igs files
    if ".IGS" in path:
        base_name = path.removesuffix(".IGS")
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
                    new_xml.write(line)
            global file_count
            file_count = file_count + 1
            new_xml.close()
            template_file.close()
            #print("file \'" + xml_name + "\' created.")
        #else:
            #print("file \'" + xml_name + "\' exists.")        

def xml_creator():    
    # folder path
    dir_path = r"C:\\d\\" 
    
    # list to store files
    # res = []
    dir_processor(dir_path)

    print(str(file_count) + " files created")

if __name__ == "__main__":
    xml_creator()