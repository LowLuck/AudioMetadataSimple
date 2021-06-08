import os
import eyed3


def main(superlist, stage):
    global path, pathlist
    for j in superlist:
        if os.path.isdir(path + f'\\{j}'):
            print(' ' * (stage * 4) + j)
            path += f'\\{j}'
            main(os.listdir(path), stage + 1)
            path = path[:-1 * len(f'\\{j}')]
        else:
            print(' ' * (stage * 4) + j)
            pathlist[j] = path + f'\\{j}'


pathlist = dict()
path = 'E:\\Testfolder'
superlist = os.listdir(path)
main(superlist, 0)
print(pathlist)

while True:
    w = input('\n Please, type name of audio file that you want to get (not all audiotypes supported) \n')
    if w in pathlist:
        mode = input('Type R to reading mode, or W to writing mode \n')
        if mode == 'R':
            audiofile = eyed3.load(pathlist[w])
            print(f'Artist: {audiofile.tag.artist}')
            print(f'Album: {audiofile.tag.album}')
            print(f'Title: {audiofile.tag.title}')
            print(f'Track_num: {audiofile.tag.track_num}')
            break
        elif mode == 'W':
            audiofile = eyed3.load(pathlist[w])
            audiofile.tag.artist = input('type artist tag \n')
            audiofile.tag.album = input('type album tag \n')
            audiofile.tag.title = input('type title tag \n')
            audiofile.tag.track_num = input('type track_num tag \n')
            audiofile.tag.save()
            break
        else:
            print('Err')
    else:
        print('File not found')

