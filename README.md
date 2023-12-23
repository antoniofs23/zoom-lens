[![Python application](https://github.com/antoniofs23/zoom-lens/actions/workflows/python-app.yml/badge.svg)](https://github.com/antoniofs23/zoom-lens/actions/workflows/python-app.yml)
# Quick Intro
Ever wanted to quickly check your webcam before hopping on a video call? Now you can with zoom-lens. 

Zoom-lens is a simple linux panel app that toggles a small webcam stream on the upper right of your screen. Since it fully runs on python3 it should in theory work in any OS, but was built and tested on ubuntu

## Functionality

- **click the menu icon** to toggle the cam or **mouse-wheel click** the app icon to toggle cam
- to end stream just close the window

![zoom-lens](https://github.com/antoniofs23/zoom-lens/assets/39067846/8cf2619f-eef6-4067-aa49-f922ece2cf3b)

Retains all openCV functionality, i.e. you can zoom in with mouse scroll wheel and drag



## Installation
*the install file assumes python is already installed (which it normally is)* if not python3 is required prior to running `INSTALL.sh`

to quickly check if python is installed run `python -V` in your terminal

clone this repo to your home directory via:

1. `git clone https://github.com/antoniofs23/zoom-lens.git`
2. In app directory run the `INSTALL.sh` file

### running the app
The app should auto-start on login.
However, it can also be run through the `zoom-lens` terminal command
