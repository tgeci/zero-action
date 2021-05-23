#!/usr/bin/python3

from Recorder import Recorder

action_recoder = Recorder(1024, 768)
action_recoder.getDiskFreeSpace()
action_recoder.calculate_possible_length()
action_recoder.start_recording()


