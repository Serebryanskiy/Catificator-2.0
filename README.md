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

Or you can simply explore and [download](https://drive.google.com/drive/folders/1bKuF3p7DAhR7fvZwLdivT2ZFUCNjJzAK) constructed dataset from Google Drive. 

## The model
<hr />
<h1 id="documentation-for-individual-models">Documentation for individual models</h1>
<table>
<thead>
<tr>
<th>Model</th>
<th align="right">Size</th>
<th align="right">Top-1 Accuracy</th>
<th align="right">Top-5 Accuracy</th>
<th align="right">Parameters</th>
<th align="right">Depth</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#xception">Xception</a></td>
<td align="right">88 MB</td>
<td align="right">0.790</td>
<td align="right">0.945</td>
<td align="right">22,910,480</td>
<td align="right">126</td>
</tr>
<tr>
<td><a href="#vgg16">VGG16</a></td>
<td align="right">528 MB</td>
<td align="right">0.713</td>
<td align="right">0.901</td>
<td align="right">138,357,544</td>
<td align="right">23</td>
</tr>
<tr>
<td><a href="#vgg19">VGG19</a></td>
<td align="right">549 MB</td>
<td align="right">0.713</td>
<td align="right">0.900</td>
<td align="right">143,667,240</td>
<td align="right">26</td>
</tr>
<tr>
<td><a href="#resnet">ResNet50</a></td>
<td align="right">98 MB</td>
<td align="right">0.749</td>
<td align="right">0.921</td>
<td align="right">25,636,712</td>
<td align="right">-</td>
</tr>
<tr>
<td><a href="#resnet">ResNet101</a></td>
<td align="right">171 MB</td>
<td align="right">0.764</td>
<td align="right">0.928</td>
<td align="right">44,707,176</td>
<td align="right">-</td>
</tr>
<tr>
<td><a href="#resnet">ResNet152</a></td>
<td align="right">232 MB</td>
<td align="right">0.766</td>
<td align="right">0.931</td>
<td align="right">60,419,944</td>
<td align="right">-</td>
</tr>
<tr>
<td><a href="#resnet">ResNet50V2</a></td>
<td align="right">98 MB</td>
<td align="right">0.760</td>
<td align="right">0.930</td>
<td align="right">25,613,800</td>
<td align="right">-</td>
</tr>
<tr>
<td><a href="#resnet">ResNet101V2</a></td>
<td align="right">171 MB</td>
<td align="right">0.772</td>
<td align="right">0.938</td>
<td align="right">44,675,560</td>
<td align="right">-</td>
</tr>
<tr>
<td><a href="#resnet">ResNet152V2</a></td>
<td align="right">232 MB</td>
<td align="right">0.780</td>
<td align="right">0.942</td>
<td align="right">60,380,648</td>
<td align="right">-</td>
</tr>
<tr>
<td><a href="#resnet">ResNeXt50</a></td>
<td align="right">96 MB</td>
<td align="right">0.777</td>
<td align="right">0.938</td>
<td align="right">25,097,128</td>
<td align="right">-</td>
</tr>
<tr>
<td><a href="#resnet">ResNeXt101</a></td>
<td align="right">170 MB</td>
<td align="right">0.787</td>
<td align="right">0.943</td>
<td align="right">44,315,560</td>
<td align="right">-</td>
</tr>
<tr>
<td><a href="#inceptionv3">InceptionV3</a></td>
<td align="right">92 MB</td>
<td align="right">0.779</td>
<td align="right">0.937</td>
<td align="right">23,851,784</td>
<td align="right">159</td>
</tr>
<tr>
<td><a href="#inceptionresnetv2">InceptionResNetV2</a></td>
<td align="right">215 MB</td>
<td align="right">0.803</td>
<td align="right">0.953</td>
<td align="right">55,873,736</td>
<td align="right">572</td>
</tr>
<tr>
<td><a href="#mobilenet">MobileNet</a></td>
<td align="right">16 MB</td>
<td align="right">0.704</td>
<td align="right">0.895</td>
<td align="right">4,253,864</td>
<td align="right">88</td>
</tr>
<tr>
<td><a href="#mobilenetv2">MobileNetV2</a></td>
<td align="right">14 MB</td>
<td align="right">0.713</td>
<td align="right">0.901</td>
<td align="right">3,538,984</td>
<td align="right">88</td>
</tr>
<tr>
<td><a href="#densenet">DenseNet121</a></td>
<td align="right">33 MB</td>
<td align="right">0.750</td>
<td align="right">0.923</td>
<td align="right">8,062,504</td>
<td align="right">121</td>
</tr>
<tr>
<td><a href="#densenet">DenseNet169</a></td>
<td align="right">57 MB</td>
<td align="right">0.762</td>
<td align="right">0.932</td>
<td align="right">14,307,880</td>
<td align="right">169</td>
</tr>
<tr>
<td><a href="#densenet">DenseNet201</a></td>
<td align="right">80 MB</td>
<td align="right">0.773</td>
<td align="right">0.936</td>
<td align="right">20,242,984</td>
<td align="right">201</td>
</tr>
<tr>
<td><a href="#nasnet">NASNetMobile</a></td>
<td align="right">23 MB</td>
<td align="right">0.744</td>
<td align="right">0.919</td>
<td align="right">5,326,716</td>
<td align="right">-</td>
</tr>
<tr>
<td><a href="#nasnet">NASNetLarge</a></td>
<td align="right">343 MB</td>
<td align="right">0.825</td>
<td align="right">0.960</td>
<td align="right">88,949,818</td>
<td align="right">-</td>
</tr>
</tbody>
</table>
<p>The top-1 and top-5 accuracy refers to the model's performance on the ImageNet validation dataset.</p>
<p>Depth refers to the topological depth of the network. This includes activation layers, batch normalization layers etc.</p>
<hr />
 
