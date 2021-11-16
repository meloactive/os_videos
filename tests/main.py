import os
import hashlib
path = '/mnt/h' # Dir name Videos
path_thumb = 'thumb' # Subdir thumbs
python_scrypt = 'sudo python3 thumbs.py ' # Windows

def main(): 
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            
            if ('.mp4' in file) or ('.mpg' in file) or ('.avi' in file) or ('.wmv' in file) or ('.webm' in file)  or ('.mkv' in file):
                files.append([os.path.join(r, file) , file])
    for fileinfo in files:
        fname = fileinfo[0].replace(" ", "\ ")
        bname = fileinfo[1]

        str_exec = python_scrypt + "\"" + path + "\" " +fname+ " \"" + path_thumb + "\"" # form a string for execution - формируем строку для выполнения
        print("Execute ",str_exec) # Displaying - Выводим на экран
        os.system(str_exec) # Run the script for execution - Запускаем скрипт на выполнение
    
if __name__ == "__main__":
    main()    