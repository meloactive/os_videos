from django.shortcuts import render, redirect
from collections import OrderedDict
# from collections import OrderedDict
import os
from django.conf import settings
from django.http import JsonResponse


# import win32api

# global list for pictures & videos
pic_list = []
pic_direc_names = []
vid_direc_names = []
vid_list = []
# global tests
# tests = []
files = []

# function to find photos/videos
# in the desired path.
def check_drive(dir_path):
    tests =[]
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
                # print(list(set(vid_direc_names)))
                # tests = list(set(vid_direc_names))
                # print(tests)
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
    # print(tests)
    for test in list(set(vid_direc_names)):
        print(test)
        files_in_list = os.listdir(test)
        for files2 in files_in_list:
            # print(test + "\\" + files2)
            files.append("Video" + "/" + files2)
    return files



# 
videos = []
# file list from a dir
def list_dir_videos(dir_name):
    try:
        files_in_list = os.listdir(dir_name)
        for i in range(len(files_in_list)):
            # print(files_in_list[i])
            if(".mp4" in files_in_list[i]):
                # print(files_in_list[i])
                videos.append(files_in_list[i])
    except:
        print("problems with : " + dir_name)
    # return files_in_list

# list_dir_videos("/mnt/f/Video")
# print(list(OrderedDict.fromkeys(videos)))
# print(len(list(OrderedDict.fromkeys(videos))))

# list_dir_videos("/mnt/h/Big Booty Anal Babes 3 [2021]/Big Booty Anal Babes 3 [2021]")
# print(list(OrderedDict.fromkeys(videos)))
# print(len(list(OrderedDict.fromkeys(videos))))

# Create your views here.
def demo_view(request):
    for folder in settings.STATICFILES_DIRS:
        print(folder)
        list_dir_videos(folder)
        print(len(list(OrderedDict.fromkeys(videos))))
    # test_arr = []
    # test_arr = check_drive("/mnt/f")
    # print(test_arr)
    # for i in range(10):
    #     test_arr.append(i)
    return render(request, 'os_videos_list/demo.html', {"lists": list(OrderedDict.fromkeys(videos))})


# test js
def test_js(request):
    return JsonResponse({'version': '0.1.0-beta'})



def post_add(request):
    a = request.POST.get("a")
    b = request.POST.get("b")

    a = float(a)
    b = float(b)
    c = a + b
    return JsonResponse({'result': c})

def test_js_html(request):
    return render(request, 'os_videos_list/test_js.html')