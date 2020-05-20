
import os, os.path, shutil

print('Current directory is {}'.format(os.getcwd()))
os.chdir('FilesToSort')
print('Change directory to FilesToSort')
print('Current directory is {}'.format(os.getcwd()))
files_list = os.listdir('.')
print(files_list)



for file in files_list:
    if os.path.isdir(file):
        continue
    for i in range(len(file)):
        if file[i] == '.':
            new_directory = file[i+1:]
            try:
                os.mkdir(new_directory)
            except FileExistsError:
                pass
            shutil.move(file, new_directory)
            break

print(files_list)






