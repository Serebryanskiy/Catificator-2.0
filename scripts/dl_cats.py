import csv
import sys
from tqdm import tqdm

import asyncio

dir = sys.path[0]
tmp = []
dl_list = []
CLASS_DICT = {'/m/01yrx': 'Cat'}


async def dl_group(images):
    """
    gathering tasks for async run on group of images
    :param images: images list
    """
    tasks = [asyncio.ensure_future(dl_image(image)) for image in images]
    output = await asyncio.gather(*tasks, return_exceptions=False)


async def dl_image(image):
    """
    async download of an given image from amazon s3 bucket using shell command
    :param image: image metadata tuple (ImageID, Source, LabelName, Confidence)
    """
    execute_string = f'aws s3 --no-sign-request cp s3://open-images-dataset/train/{image[0]}.jpg' \
        f' {dir}/{CLASS_DICT[image[2]]}/'

    proc = await asyncio.create_subprocess_shell(
        execute_string,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    # if stdout:
    #     print(f'[stdout]\n{stdout.decode()}') #
    # if stderr:
    #     print(f'[stderr]\n{stderr.decode()}') #


def chunks(l, n):
    """Yield successive n-sized chunks from l"""
    for i in range(0, len(l), n):
        yield l[i:i + n]


with open(dir + '/train-annotations-human-imagelabels.csv', newline='') as csvfile:

    bboxs = csv.reader(csvfile, delimiter=',', quotechar='|')
    for bbox in tqdm(bboxs):
        if bbox[0] == tmp:
            continue  # Avoid downloading one image many times for the image which contains multiple target classes
        if bbox[2] in CLASS_DICT:
            dl_list.append(bbox)
            tmp = bbox[0]

    dl_groups = list(chunks(dl_list, 120)) #would error with "Too many open files" if set > 120
    for images in tqdm(dl_groups):
        asyncio.run(dl_group(images))