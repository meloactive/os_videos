import os
from collections import OrderedDict

# 
videos = []
# file list from a dir
def list_dir_videos(dir_name):
    files_in_list = os.listdir(dir_name)
    for i in range(len(files_in_list)):
        # print(files_in_list[i])
        if(".mp4" in files_in_list[i]):
            # print(files_in_list[i])
            videos.append(files_in_list[i])
    return files_in_list

list_dir_videos("/mnt/f/Video")
print(list(OrderedDict.fromkeys(videos)))
print(len(list(OrderedDict.fromkeys(videos))))

list_dir_videos("/mnt/h/Big Booty Anal Babes 3 [2021]/Big Booty Anal Babes 3 [2021]")
print(list(OrderedDict.fromkeys(videos)))
print(len(list(OrderedDict.fromkeys(videos))))