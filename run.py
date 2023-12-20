import cv2
import tkinter 
import signal
import gi
import os
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3, GObject

# change the working directory when script is run through command-line
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)

class Indicator():
    def __init__(self):
        self.app = 'zoom-lens'
        iconpath = os.path.abspath('zoom-lens.svg')
        self.indicator = AppIndicator3.Indicator.new(
            self.app, iconpath,
            AppIndicator3.IndicatorCategory.OTHER)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.create_menu())

    def create_menu(self):
        
        menu = Gtk.Menu()
        
        # show camera
        display = Gtk.MenuItem('activate cam')
        display.connect('activate', self.cam)
        menu.append(display)
        
        # quit app
        quit = Gtk.MenuItem('quit')
        quit.connect('activate', self.quit)
        menu.append(quit)
        
        menu.show_all()
        return menu

    def cam(self,source):
        # open webcam
        capture = cv2.VideoCapture(0)
        
        # make cam viewer
        cv2.namedWindow('zoom-lens', flags=cv2.WINDOW_GUI_NORMAL)
        cv2.setWindowProperty('zoom-lens', cv2.WND_PROP_TOPMOST, 1)
        
        # get screen resolution to define initial win location
        root = tkinter.Tk()
        x = root.winfo_screenwidth()
        cv2.moveWindow('zoom-lens', x, 0)
        
        # stream loop
        while cv2.getWindowProperty('zoom-lens', cv2.WND_PROP_VISIBLE) > 0:
            
            # read webcam stream
            _,frame = capture.read()

            # display webcam in window
            cv2.imshow('zoom-lens', frame)
            
            # back-up exit handle
            if cv2.waitKey(1) == ord('~'):
                break
            
        #clean up
        capture.release()
        cv2.destroyAllWindows()
            
    def quit(self, source):
        Gtk.main_quit()    


Indicator()
signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()
