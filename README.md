# Catificator 2.0: Android application for image classification

Have you ever wonder if that thing in your house a cat or not? Well now you can know for sure!

An elgeant android application where user can take a photo and figure out if there is a cat or not.

## Dataset 

For the purpose of this application the Google Open Images V5 dataset has been chosen. The whole dataset covers 6000 categories and ~ ~9 million images with total size of 18TB. We chose an Subset with Bounding Boxes (600 classes with total size of 561GB) as specific images can be downloaded directly. https://storage.googleapis.com/openimages/web/download.html

There were two reasons for that choice. The first one is that dimensions of images high enough to train network with relativity large input shape. (Images in subset has 1024x600 dimensions on average, input size was choose as 498x498). The second one is to make non-cat class images represent an average cellphone photo image. Subset with Bounding Boxes has 600 classes with majority such classes as Person, Land vehicle, Furniture, Food, Building.

Steps to construct training dataset:
* Download every image corresponding to cats
* Convert the model to TFLite Format and create optimized graphs
* Setup Android App
* Test Run our customized app 


We are retraining final layer of images to create labels and graphs for our provided set of images, classification model is getting created by Transfer Learning.  

We are using TensorFlow library of python here. TensorFlow is an open-source software library for dataflow programming across a range of tasks. It is a symbolic library used for machine learning applications such as neural networks.  
<br>
##### Following are the tasks we will be performing in this exercise:
* Retrain a MobileNet
* Convert the model to TFLite Format and create optimized graphs
* Setup Android App
* Test Run our customized app 
  
##### Prerequisites are as follow:  
* Install Tensorflow `$ pip install --upgrade "tensorflow==1.7.*"`  
* Android Studio setup [v3.1+]
* Android Device(With Debugging Enabled) or Emulator (API Level = 27, Target = Android 8.1)

#### Output will be similiar to below images in real device:
<p float="center">
  <img src="https://drive.google.com/uc?id=1yDcRRrjgrig1R2Bpo2u-6neLrQ9bLkKh" width="195" />
  <img src="https://drive.google.com/uc?id=1oc7hk3796frk6eCw-udGNy8GatUczbvt" width="195" /> 
  <img src="https://drive.google.com/uc?id=15ix8M0mGlIzKLj2fe6h-JSUj1yfNpGns" width="195" />
  <img src="https://drive.google.com/uc?id=1tkabGhP12KaWRoRsJATDI1-lwqQVn3IX" width="195" />
</p><br>

##### _CLI version of same_:
> **https://github.com/tarunmaini16/image-classifier**