import os
import shutil
import sys
from PIL import Image

def get_files(path):
    files = os.listdir(path)
    # print(files)
    return files

def get_sizes(img_path):
    im = Image.open(img_path)
    width, height = im.size
    # print('width is: {0}; height is: {1}'.format(width, height))
    return width, height

def sort_hor_vert(path):
    images = get_files(path)

    horizontal_images = []
    vertical_images = []
    square_images = []

    for image in images:
        image = os.path.join(path, image)
        # print(os.path.join(path, image))
        if get_sizes(image)[0] > get_sizes(image)[1]:
            horizontal_images.append(image)
        elif get_sizes(image)[0] < get_sizes(image)[1]:
            vertical_images.append(image)
        else:
            square_images.append(image)

    return horizontal_images, vertical_images, square_images

def copy_files(src, dst):
    '''src - array of paths
    dst - end path
    '''

    for f in src:
        print('Copying: {0} to {1}\n\n'.format(f, dst))
        shutil.copy(f, dst)

def sort_hor_vert_folders(path):

    images = sort_hor_vert(path)
    hor = images[0]
    vert = images[1]
    sq = images[2]

    if len(hor) > 0:
        os.makedirs(os.path.join(path, 'horizontal'), exist_ok=True)
    if len(vert) > 0:
        os.makedirs(os.path.join(path, 'vertical'), exist_ok=True)
    if len(sq) > 0:
        os.makedirs(os.path.join(path, 'square'), exist_ok=True)

    copy_files(hor, os.path.join(path, 'horizontal'))
    copy_files(vert, os.path.join(path, 'vertical'))
    copy_files(sq, os.path.join(path, 'square'))




if __name__ == '__main__':
    inpath = sys.argv[1]
    print(inpath)
    # get_files(inpath)
    # print(get_sizes(inpath)[1])

    print(sort_hor_vert_folders(inpath))
