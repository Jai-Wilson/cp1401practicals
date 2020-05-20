import os, os.path, shutil


def main():
    print('Current directory is {}'.format(os.getcwd()))
    os.chdir('FilesToSort')
    print('Change directory to FilesToSort')
    print('Current directory is {}'.format(os.getcwd()))
    files_list = os.listdir('.')
    print(files_list)

    extensions = get_extensions(files_list)
    get_user_directories(extensions, files_list)


def get_extensions(files_list):
    extensions = []
    for file in files_list:
        extension = file.split('.')[-1]
        if extension in extensions:
            pass
        else:
            extensions.append(extension)
    return extensions


def get_user_directories(extensions, files_list):
    for extension in extensions:
        user_extension = input('What category would you like to sort {} files into? '.format(extension))
        try:
            os.mkdir(user_extension)
        except FileExistsError:
            pass
        move_files(files_list, user_extension, extension)


def move_files(files_list, user_extension, extension):
    for file in files_list:
        current_extension = file.split('.')[-1]
        if current_extension == extension:
            shutil.move(file, user_extension)


main()
