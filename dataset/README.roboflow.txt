
face_stuffs - v4 2023-04-19 6:04am
==============================

This dataset was exported via roboflow.com on April 19, 2023 at 1:05 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 745 images.
Hair are annotated in YOLOv8 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* 50% probability of vertical flip
* Random rotation of between -20 and +20 degrees
* Random shear of between -7° to +7° horizontally and -7° to +7° vertically
* Salt and pepper noise was applied to 3 percent of pixels

The following transformations were applied to the bounding boxes of each image:
* Random rotation of between -3 and +3 degrees
* Random brigthness adjustment of between -10 and +10 percent
* Random exposure adjustment of between -10 and +10 percent


