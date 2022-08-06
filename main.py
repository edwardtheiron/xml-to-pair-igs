import os

# folder path
dir_path = r"C:\\d\\"
template_path = r"C:\\d\\template.xml"
placeholder = "placeholder"
file_count = 0
# list to store files
# res = []

# Iterate target directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        #checks only for igs files
        if ".IGS" in path:                
            base_name = path.removesuffix(".IGS") # 
            xml_name = base_name + ".xml"
            #check if xml already exists
            if not os.path.exists(xml_name):
                with open(template_path,'r') as template_file, open(dir_path + xml_name, 'w') as new_xml:                        
                    for line in template_file:                           
                        if placeholder in line:
                            line = line.replace(placeholder,base_name)
                        #else:
                            #print(f"No {placeholder} in file")
                        new_xml.write(line)
                file_count = file_count + 1
                new_xml.close()
                template_file.close()
                #print("file \'" + path + "\' created.")
            #else:
                #print("file \'" + path + "\' exists.")
print(str(file_count) + " files created")