import os, sys, logging, picamera
from datetime import datetime
from cysystemd import journal

class Recorder(object): 

    
    def __init__(self, res_width, res_height, res_bitrate=25, recording_path="./", cleanup=False):
        """ Initialize the recorder instance
        """
        self.Cleanup = cleanup
        self.Width = res_width
        self.Height = res_height
        self.Bitrate = res_bitrate
        self.RecordingPath = recording_path
        self.Max_Video_Duration = 0
        self.FreeSpace_Mb = 0
        self.Min_Free_Space_Mb = 1000

        # Write to journald
        journal.write("Recorder initialized.")

    def getDiskFreeSpace(self):
        """ Determine free space in recording path
        """

        st = os.statvfs(self.RecordingPath) 
        self.FreeSpace_Mb = (st.f_bavail * st.f_frsize) / 1024

    def calculate_possible_length(self):
        """ Return max possible video lenght in seconds based on resolution
        """
        
        journal.write("There are " + str(self.FreeSpace_Mb) + " mb free space in " + self.RecordingPath + " .")
        mb_per_sec = self.Bitrate / 8
        
        journal.write("1 Second video recording requires " + str(mb_per_sec) + " mb free space.")
        self.Max_Video_Duration = self.FreeSpace_Mb - 1000 / mb_per_sec
        journal.write("Based on your free space and limits we are able to record max " + str(round(self.Max_Video_Duration/60)) + " minutes or " + str(round(self.Max_Video_Duration/3600)) + " hours." )
        return self.Max_Video_Duration 

    def start_recording(self):
        """Start recording
        """

        # Set todays date
        today = str(datetime.now().year) + "-" + str(datetime.now().month) + "-" + str(datetime.now().day)

        # Check if there is already a 
        if os.path.isfile(today + '-record.h264'):
            journal.write("Start recording in rollup file")
            filename = today + "-" + str(datetime.now().hour) + str(datetime.now().minute) + '-record.h264'
            with picamera.PiCamera() as camera:
                camera.resolution = (self.Width, self.Height)
                camera.start_recording(filename)
                camera.wait_recording(self.Max_Video_Duration)
                camera.stop_recording()
        else:
            journal.write("Start recording in new file")
            with picamera.PiCamera() as camera:
                camera.resolution = (self.Width, self.Height)
                camera.start_recording(today + '-record.h264')
                camera.wait_recording(self.Max_Video_Duration)
                camera.stop_recording()
