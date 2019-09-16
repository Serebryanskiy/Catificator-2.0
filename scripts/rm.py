import csv
import sys
from tqdm import tqdm
from subprocess import Popen, PIPE


dir = sys.path[0]
class_dict = {'/m/01yrx': 'Cat'}

images_list = []

def rm_files(images, path):
    cmds_list = [['rm', f'{path}{image[0]}.jpg'] for image in
                 images]
    procs_list = [Popen(cmd, stdout=PIPE, stderr=PIPE) for cmd in cmds_list]
    for proc in procs_list:
        proc.wait()



def chunks(l, n):
    """Yield successive n-sized chunks from l"""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def sort_labels(csv_file,path, all_classes):
    """
    sorts files by dirs (labels in class_dict)
    :param csv_file: input csv files with image file names and labels
    """
    tmp = []
    print('Starting with ', csv_file)
    global count, count_err
    count, count_err = 0, 0

    with open(dir + '/' + csv_file, newline='') as csvfile:

        bboxs = csv.reader(csvfile, delimiter=',', quotechar='|')
        for bbox in tqdm(bboxs):
            if bbox[0] == tmp or bbox[11] == 'IsDepiction':
                continue  # Avoid downloading one image many times for the image which contains multiple target classes
            if int(bbox[11]) == 1 and (all_classes or bbox[2] in class_dict):
                images_list.append(bbox)
                tmp = bbox[0]

        dl_groups = list(chunks(images_list, 100))  # would error with "Too many open files" if set > 120
        for images in tqdm(dl_groups):
                rm_files(images, path)
    print('Items moved: ', count)


count = 0
count_err = 0

sort_labels('test-annotations-bbox.csv', './test/', True)
sort_labels('train-annotations-bbox.csv', './cats/', False)

