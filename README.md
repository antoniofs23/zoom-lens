# Quick Intro
Ever wanted to quickly check your webcam before hopping on a video call? Now you can with zoom-lens. 

Zoom-lens is a simple linux panel app that toggles a small webcam stream on the upper right of your screen. Since it fully runs on python3 it should in theory work in any OS

![zoom-lens](https://github.com/antoniofs23/zoom-lens/assets/39067846/8cf2619f-eef6-4067-aa49-f922ece2cf3b)

Retains all openCV functionality, i.e. you can zoom in with mouse scroll wheel and drag

## Installation
clone this repo to your home directory via:

`git clone https://github.com/antoniofs23/zoom-lens.git`

### dependencies
This was built using OpenCV.
For python dependencies you can run the `pip install -r requirements.txt` command 

### running the app

To run via your terminal you can create an alias in your `.bashrc`:

`alias zoom-lens='python3 ~/zoom-lens/run.py &'`

dont forget to `source .bashrc` after making the change
