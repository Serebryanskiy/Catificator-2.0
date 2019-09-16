# Catificator 2.0: Android application for image classification

Have you ever wondered whether this thing in your house is a cat or not? Well, now you can know for sure!

An elegant android application with which a user can take a photo and figure out if there is a cat in it.

## Dataset

The Google Open Image V5 dataset has been chosen for this application. For the purpose of this application the Google Open Images V5 dataset has been chosen. The whole dataset covers 6000 categories and ~9 million images with total size of 18TB. We chose a Subset with Bounding Boxes (600 classes with total size of 561GB) as in the subset specific images can be downloaded directly. https://storage.googleapis.com/openimages/web/download.html

There are two reasons taken into account for choosing OIV5. The first one is that the dimensions of images are high enough to train a network with a relativity large input shape. (The Images in a dataset have 1024x600 dimensions on average). The second reason is to have non-cat class images that more likely can represent an average cell phone photo image.  Subset with Bounding Boxes has 600 classes with majority in such classes as Person, Land vehicle, Furniture, Food, Building.

Steps to construct training dataset from Subset with Bounding Boxes:
* [Download train image’s indexes csv](https://datasets.figure-eight.com/figure_eight_datasets/open-images/train-annotations-bbox.csv)
* [Download test image’s indexes csv](https://datasets.figure-eight.com/figure_eight_datasets/open-images/test-annotations-bbox.csv)
* Download every image corresponding to [Cats class](./scripts/dl_cats.py) (14025 images)
* Download [test data set](https://datasets.figure-eight.com/figure_eight_datasets/open-images/zip_files_copy/test.zip)
* [Remove](./scripts/rm.py) all files corresponding to IsDepiction attribute (e.g., a cartoon or drawing of the object, not a real physical instance) and move cats images from test dir.
* Choose randomly 14025 images from test 
* Make train, validation, test subsets as (70%/15%/15%)

