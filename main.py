import os


def main(superlist, stage):
    global path, pathlist
    for j in superlist:
        if os.path.isdir(path + f'\\{j}'):
            print(' ' * (stage * 4) + j)
            path += f'\\{j}'
            main(os.listdir(path), stage + 1)
        else:
            print(' ' * (stage * 4) + j)
            pathlist[j] = path + f'\\{j}'


pathlist = dict()
path = 'E:\\Testfolder'
superlist = os.listdir(path)
main(superlist, 0)
print(pathlist)
