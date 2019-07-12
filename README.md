# StormLabeler

This library allows human to outline tornadic parts of thunderstorms.  Specifically, we ask you to outline the parts of each storm that most support tornado production within the next hour (whether it's a new tornado or one that's already on the ground).  The human labels will be compared with class-activation maps from machine learning.

# Download and Installation

Run the following commands in a Unix terminal, where `PYTHON_EXE_NAME` is the path to your Python executable.  For example, my Python executable is at `/home/thunderhoser/anaconda3/bin/python3.6`, so my install command is `/home/thunderhoser/anaconda3/bin/python3.6 setup.py install`.  To use your default Python installation, just type `python setup.py install`.

`git clone https://github.com/thunderhoser/StormLabeler.git`
`cd stormlabeler`
`${PYTHON_EXE_NAME} setup.py install`

This should install StormLabeler and all the packages on which it depends.

# Running the Script

The script is called `capture_human_polygons.py`, and it's in the directory `stormlabeler/scripts`.  You can run it with the following syntax, where `INPUT_DIR_NAME` is the path to the input directory (containing images to be labeled) and `OUTPUT_DIR_NAME` is the path to the output directory (where your labels will be saved, as one NetCDF file per storm image).

`python capture_human_polygons.py -i ${INPUT_DIR_NAME} -o ${OUTPUT_DIR_NAME}`

