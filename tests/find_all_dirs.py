from collections import OrderedDict
import os
from threading import Thread

vid_direc_names = []
vid_list = []

def check_drive(dir_path):
    try:
        # lists the files in the directory
        files_in_list = os.listdir(dir_path)
        for file_ in files_in_list:
            # storing the name of the file
            search_file = file_
            # checks file or directory
            dir_if = os.path.join(dir_path, search_file)
            # file extension
            name, ext = os.path.splitext(file_)            
            # checks if the file is a image
            # if ext[1:] in ('jpg', 'png', 'jpeg', 'gif', 'webp', 'tiff', 'tif', 'bmp', 'dib', 'raw', 'arw', 'svg', 'svgz', 'psd', 'jpe', 'jif', 'jfif', 'jfi'):
            #     # if the file is image then
            #     # the file's folder name is added to a list
            #     pic_direc_names.append(os.path.basename(dir_path))
            # checks if the file is video
            if ext[1:] in ('mp4', 'mov', 'flv', 'wmv', 'avi', 'avchd', 'mpeg-2'):
                # if the file is video then
                # the file's folder name is added to a list
                vid_direc_names.append(dir_path)
            # checks if the file is a directory 
            if os.path.isdir(dir_if):
                # if the file is a directory
                # then the function is called 
                # to check for image/video in the directory.
                check_drive(dir_if)
    # excepts if the file is 
    # protected.
    except PermissionError:
        pass

    # with open("dir_list.txt", "a") as f:
    #     f.write(str(list(OrderedDict.fromkeys(vid_direc_names))) + "\n")
# arr = [ 'c', 'e', 'f', 'h']
# for i in range(len(arr)):
#     # t1 = check_drive("/mnt/"+ arr[i])
#     t1 = Thread(target=check_drive, args=("/mnt/"+ str(arr[i]),))
#     t1.start()

check_drive("/mnt/h")
print(list(OrderedDict.fromkeys(vid_direc_names)))
check_drive("/mnt/h")
print(list(OrderedDict.fromkeys(vid_direc_names)))
/mnt/h
# i have list of array with folder 
#  want to get the files list which contains mp4