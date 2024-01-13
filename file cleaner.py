#import the libraries and modules.
import os
import shutil

#store the filepath of the targeted folder
a=os.path.expanduser("~/downloads")
#make a dict to stor file paths according to extensions
dict1 = {}
#loop through files one by one
for file_path in os.listdir(a):
    #make full path of files by joining the paths
    file_full_name=os.path.join(a,file_path)
    #check if the file is a file
    if os.path.isfile(file_full_name):
        #split the file and store the extension
        file_ext=os.path.splitext(file_full_name)[1]
        #check if the file extension is in the dictionary
        if file_ext not in dict1:
            #store the file extensions as keys with empty array for full file paths
            dict1[file_ext]=[]
        #append the full file path to the dictionary according to the extnesion
        dict1[file_ext].append(file_full_name)
#divide keys and values in separate file
for ext,file_p in dict1.items():
    # create folder with extension
    folder=f'{ext[1:].upper()} Files'
    #create full file path according with folder name
    filepath=os.path.join(a,folder)
    #check if the file exist ,if not make a new file
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    #loop through files in the values of dict
    for file_pat in file_p:
        #move the files one by one to destination folder
        shutil.move(file_pat,filepath)


