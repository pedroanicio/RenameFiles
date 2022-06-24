from importlib.resources import path
import os


def main():
    i = 1
    path = "C:/Users/pedra/visual studio codes/Renaming bulk files/files/"
    for filename in os.listdir(path):
        my_dest = "file"+ str(i) + ".txt"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == '__main__':
    main()