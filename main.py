import os


def main():
    i = 0
    path = "just_a_folder/"

    for filename in os.listdir(path):
        if filename[-4:] == '.txt':
            print('txt - ', filename)
            my_dest = 'text_' + str(i) + '.txt'
            my_source = path + filename
            my_dest = path + my_dest
            os.rename(my_source, my_dest)
            i += 1
        elif filename[-4:] == '.png':
            print('png - ', filename)
            my_dest = 'img_' + str(i) + '.png'
            my_source = path + filename
            my_dest = path + my_dest
            os.rename(my_source, my_dest)
            i += 1


if __name__ == '__main__':
    main()
