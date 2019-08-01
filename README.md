# Online Consent to Participate in Research 

## Would you like to be involved in research at the University of Oklahoma?

I am Amy McGovern from the School of Computer Science at University of Oklahoma, and I invite you to participate in my research project entitled “Comparing What Humans and Machines Learn About Tornadoes”. This research is being conducted at the University of Oklahoma. You were selected as a possible participant because you have expertise in meteorology. You must be at least 18 years of age to participate in this study.

**Please read this document and contact me to ask any questions that you may have BEFORE agreeing to take part in my research.**

**What is the purpose of this research?** The purpose of this research is to identify whether or not machine learning can discover new knowledge about tornadoes.

**How many participants will be in this research?** About 100 people will take part in this research.

**What will I be asked to do?** If you agree to be in this research, you will download this Python library, along with the accompanying thunderstorm images, label as many as of the images as you want, and email the labels to ryan.lagerquist@ou.edu.

**How long will this take?** Your participation will take 15-30 minutes.

**What are the risks and/or benefits if I participate?** There are no personal risks or benefits from being in this research.  However, you will be helping to advance research at the nexus of meteorology and machine learning, especially in using machine learning to discover new physical knowledge.

**Will I be compensated for participating?** You will not be reimbursed for your time and participation in this research.

**Who will see my information?** In research reports, there will be no information that will make it possible to identify you.  Research records will be stored securely and only approved researchers and the OU Institutional Review Board will have access to the records.

**What will happen to my data in the future?** After removing all identifiers, we might share your data with other researchers or use it in future research without obtaining additional consent from you.

**Do I have to participate?** No. If you do not participate, you will not be penalized or lose benefits or services unrelated to the research. If you decide to participate, you don’t have to answer any question and can stop participating at any time.

**Who do I contact with questions, concerns or complaints?** If you have questions, concerns or complaints about the research or have experienced a research-related injury, contact us at ryan.lagerquist@ou.edu or amcgovern@ou.edu (405-325-5427).

You can also contact the University of Oklahoma – Norman Campus Institutional Review Board (OU-NC IRB) at 405-325-8110 or irb@ou.edu if you have questions about your rights as a research participant, concerns, or complaints about the research and wish to talk to someone other than the researcher(s) or if you cannot reach the researcher(s).

*Please print this document for your records. By providing information to the researcher(s), I am agreeing to participate in this research.*

**This research has been approved by the University of Oklahoma, Norman Campus IRB.**
**IRB Number: ______			Approval date: ______**

# StormLabeler

This library facilitates two human experiments.  The goal is to determine if machine learning can discover new knowledge about tornadoes.  You will be asked to label storm-centered radar images, some of tornadic storms and some of non-tornadic storms.  Your labels will be compared with a convolutional neural network (CNN).

Once you have labeled as many storms as you want, we ask that you e-mail your labels to [ryan.lagerquist@ou.edu](mailto:ryan.lagerquist@ou.edu).  The labels will be anonymized and contain no personally identifiable information.  By e-mailing your labels, you consent for them to be used in academic research.

## Download and Installation

Run the following commands in a Linux terminal.

`git clone https://github.com/thunderhoser/StormLabeler.git` <br/>
`cd stormlabeler` <br/>
`python setup.py install` <br/>

This should install StormLabeler and all the packages on which it depends.

## Experiment 1: Regions of Interest

In this experiment you will draw regions of interest for each storm.  Specifically, you will outline regions of the storm that, in your mind, contain evidence for next-hour tornado occurrence.  In other words, you will outline regions that most strongly support the prediction that the storm will be tornadic at *some* time in the next hour.

Please follow the steps below.

 1. **Download storm images** from [here](https://drive.google.com/file/d/1KkjNFr6rTcwTJfbUMzKZhA74Ns7AS3Up/view?usp=sharing).  Unzip the storm images to a directory on your machine.  Henceforth, I will assume that this directory is `/home/thunderhoser/experiment1`.
 
 2. **Run the script** `capture_human_polygons.py`.  This requires two input arguments:
    - Input directory, containing the storm images that you just downloaded
    - Output directory, where you want your regions to be saved
    
    Run the following command from a Linux terminal (your input and output directories will probably be different).
    
    `python capture_human_polygons.py -i "/home/thunderhoser/experiment1" -o "/home/thunderhoser/experiment1/human_regions"`
    
    The script will read storm images and present them to you, one at a time.  You may draw as many regions as you want on top of each storm, indicating where you find the most evidence for next-hour tornado occurrence.  If you believe that no part of the storm contains evidence for next-hour tornado occurrence, just click "Finish" without drawing any regions.  The interface looks like this:
    
    ![Experiment 1 interface without regions](images/cam_screenshot01.png)
    
    The left panel shows maximum reflectivity from 1-3 km above ground level (AGL), and the right panel shows maximum vorticity from 2-4 km AGL.  Both grids are 32 x 32 with 1.5-km spacing (48 x 48 km), and stomrm motion is towards the right.  Colour bars are omitted from the images to be labeled.  However, if you need them as a reference, an image with colour bars is shown below.  The colour scheme (correspondence of colour to value) is the same for every storm.
    
    ![Storm image without colour bars](images/storm_image_with_colour_bars.png)
    
    To draw a new region, click "New ROI".  Left-click for a new vertex and right-click to close the polygon.  If you accidentally draw an invalid polygon (with less than 3 vertices), don't worry -- it will be ignored.  Once you have drawn all the regions you want, click "Finish".  After drawing one region, the interface might look like this:
    
    ![Experiment 1 interface with one region](images/cam_screenshot02.png)
    
    After drawing two regions, the interface might look like this:
    
    ![Experiment 1 interface with two regions](images/cam_screenshot03.png)
    
    **Do not feel obligated to label all the images.**  When you have labeled as many as you want, just exit the script.
    
 3. **Send results** (NetCDF files produced by the script, which contain your labels) to [ryan.lagerquist@ou.edu](mailto:ryan.lagerquist@ou.edu).  In so doing, you give your consent for the anonymized labels to be used for academic research.

## Experiment 2: Human Novelty Detection

In this experiment you will see machine-based regions of interest (according to the CNN) for each storm.  You will be asked to label regions of interest that disagree with your intuition -- *i.e.*, where the machine thinks there is strong evidence for next-hour tornado occurrence but you don't.

Please follow the steps below.

 1. **Download storm images** from [here](FOO).  Unzip the storm images to a directory on your machine.  Henceforth, I will assume that this directory is `/home/thunderhoser/experiment2`.
 
 2. **Run the script** `capture_human_mouse_clicks.py`.  The script requires two input arguments: the input and output directory.  Run the following command from a Linux terminal (your input and output directories will probably be different).
    
    `python capture_human_mouse_clicks.py -i "/home/thunderhoser/experiment2" -o "/home/thunderhoser/experiment2/human_labels"`
    
    The script will read storm images and present them to you, one at a time.  To label a region of interest as novel or unexpected, just click inside it.  A black diamond will show up wherever you click.  If you find no regions novel or unexpected, simply close the image and move on to the next one.  The interface looks like this:
    
    ![Experiment 2 interface with no regions labeled](images/nd_screenshot01.png)
    
    After labeling a few regions, the interface might look like this.  You can click in either panel -- the reflectivity or vorticity panel.
    
    ![Experiment 2 interface with a few regions labeled](images/nd_screenshot02.png)

 3. **Send results** (NetCDF files produced by the script, which contain your labels) to [ryan.lagerquist@ou.edu](mailto:ryan.lagerquist@ou.edu).  In so doing, you give your consent for the anonymized labels to be used for academic research.
