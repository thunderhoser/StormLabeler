# StormLabeler

This library facilitates two human experiments.  The goal is to determine if machine learning can discover new knowledge about tornadoes.  You will be asked to label storm-centered radar images, some of tornadic storms and some of non-tornadic storms.  Your labels will be compared with a convolutional neural network (CNN).

Once you have labeled as many storms as you want, we ask that you e-mail your labels to [ryan.lagerquist@ou.edu](mailto:ryan.lagerquist@ou.edu).  The labels will be anonymized and contain no personally identifiable information.  By e-mailing your labels, you consent for them to be used in academic research.

## Experiment 1: Regions of Interest

In this experiment you will draw regions of interest for each storm.  Specifically, you will outline regions of the storm that, in your mind, contain evidence for next-hour tornado occurrence.  In other words, you will outline regions that most strongly support the prediction that the storm will be tornadic at *some* time in the next hour.

Please follow the steps below.

 1. **Download and installation**.  Run the following commands in a Linux terminal.

`git clone https://github.com/thunderhoser/StormLabeler.git` <br/>
`cd stormlabeler` <br/>
`python setup.py install` <br/>

This should install StormLabeler and all the packages on which it depends.

## Labeling Storms

First, you'll need to download storm images from [here](https://drive.google.com/file/d/1KkjNFr6rTcwTJfbUMzKZhA74Ns7AS3Up/view?usp=sharing).  Unzip the storm images to a directory on your machine.  We'll call this directory `INPUT_DIR_NAME`.

The script for labeling storms is called `capture_human_polygons.py`.  It takes two arguments: the input directory `INPUT_DIR_NAME` (containing images to be labeled) and output directory `OUTPUT_DIR_NAME` (where your labels will be saved, as one NetCDF file per storm image).  You can run the script from a Unix terminal with the following command.

`python capture_human_polygons.py -i ${INPUT_DIR_NAME} -o ${OUTPUT_DIR_NAME}`

For example, if you put the images in `/home/thunderhoser/storm_images` and want your labels saved to `/home/thunderhoser/storm_images/human_labels`, your exact command will be the following.

`python capture_human_polygons.py -i "/home/thunderhoser/storm_images" -o "/home/thunderhoser/storm_images/human_labels"`

The script will read storm images from `INPUT_DIR_NAME` and present them to you one at a time.  We ask you to outline the parts of the storm that support (give evidence for) tornado production within the next hour.  The interface looks like this:

FOOOO

The left panel shows maximum reflectivity from 1-3 km above ground level (AGL), and the right panel shows maximum vorticity from 2-4 km AGL.  Both grids are 32 x 32 with 1.5-km spacing (48 x 48 km) and rotated so that storm motion is towards the right.  Colour bars are omitted from the images to be labeled.  However, if you need them as a reference, an image with colour bars is shown below.  The colour scheme (correspondence of colour to value) is the same for every storm.

FOOOOO

To draw a new polygon (area that supports tornado production), click on "New ROI".  Left-click for a new vertex and right-click to close the polygon.  If you accidentally draw an invalid polygon (with less than 3 vertices), don't worry; the script will ignore it.  Once you are finished (you've outlined all the areas that, in your mind, support tornado production), click "Finish".  If the storm contains **no** areas that support tornado production, you can just click "Finish" right away without drawing anything.  After clicking "Finish", the script will save your polygons to a file and display the next image.  There are 400 images, but **don't feel obligated to label them all**.  Just label as many as you want then kill the script (by pressing `Ctrl + C` in the terminal).

# Sending Results

Once you've labeled as many storms as you want, we ask that you email results (the NetCDF files produced by the script) to [ryan.lagerquist@ou.edu](mailto:ryan.lagerquist@ou.edu).
