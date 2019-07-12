# StormLabeler

This library allows humans to outline tornadic parts of thunderstorms.  Specifically, we ask you to outline the parts of each storm that support tornado production within the next hour.  The human labels will be compared with class-activation maps from a convolutional neural network (CNN), which is a type of deep-learning model.  Our goal is to discover if humans and CNNs focus on different parts of the storm.

## Download and Installation

Run the following commands in a Unix terminal, where `PYTHON_EXE_NAME` is the path to your Python executable.  For example, my Python executable is at `/home/thunderhoser/anaconda3/bin/python3.6`, so my install command is `/home/thunderhoser/anaconda3/bin/python3.6 setup.py install`.  To use your default Python installation, just type `python setup.py install`.

`git clone https://github.com/thunderhoser/StormLabeler.git` <br/>
`cd stormlabeler` <br/>
`${PYTHON_EXE_NAME} setup.py install` <br/>

This should install StormLabeler and all the packages on which it depends.

## Labeling Storms

First, you'll need to download storm images from [here](https://www.google.com).  Unzip the storm images to a directory on your machine.  We'll call this directory `INPUT_DIR_NAME`.

The script for labeling storms is called `capture_human_polygons.py`.  It takes two arguments: the input directory `INPUT_DIR_NAME` (containing images to be labeled) and output directory `OUTPUT_DIR_NAME` (where your labels will be saved, as one NetCDF file per storm image).  You can run the script from a Unix terminal with the following command.

`python capture_human_polygons.py -i ${INPUT_DIR_NAME} -o ${OUTPUT_DIR_NAME}`

The script will read storm images from `INPUT_DIR_NAME` and present them to you one at a time.  We ask you to outline the parts of the storm that support (give evidence for) tornado production within the next hour.  The interface looks like this:

FOOOO

The left panel shows maximum reflectivity from 1-3 km above ground level (AGL), and the right panel shows maximum vorticity from 2-4 km AGL.  Both grids are 32 x 32 with 1.5-km spacing (48 x 48 km) and rotated so that storm motion is towards the right.  Colour bars are omitted from the images to be labeled.  However, if you need them as a reference, an image with colour bars is shown below.  The colour scheme (correspondence of colour to value) is the same for every storm.

FOOOOO

To draw a new polygon (area that supports tornado production), click on "New ROI".  Left-click for a new vertex and right-click to close the polygon.  If you accidentally draw an invalid polygon (with less than 3 vertices), don't worry; the script will ignore it.  Once you are finished (you've outlined all the areas that, in your mind, support tornado production), click "Finish".  If the storm contains **no** areas that support tornado production, you can just click "Finish" right away without drawing anything.  After clicking "Finish", the script will save your polygons to a file and display the next image.  There are 400 images, but **don't feel obligated to label them all**.  Just label as many as you want then kill the script (by pressing `Ctrl + C` in the terminal).

# Sending Results

Once you've labeled as many storms as you want, we ask that you email results (the NetCDF files produced by the script) to [ryan.lagerquist@ou.edu](mailto:ryan.lagerquist@ou.edu).
