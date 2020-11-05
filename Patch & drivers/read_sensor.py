#!/usr/bin/python
import struct
import time
import sys

infile_path = "/dev/input/event" + (sys.argv[1] if len(sys.argv) > 1 else "0")

"""
FORMAT represents the format used by linux kernel input event struct
See https://github.com/torvalds/linux/blob/v5.5-rc5/include/uapi/linux/input.h#L28
Stands for: long int, long int, unsigned short, unsigned short, unsigned int
"""
FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)

#open file in binary mode
in_file = open(infile_path, "rb")

event = in_file.read(EVENT_SIZE)

while event:
    (tv_sec, tv_usec, type, code, value) = struct.unpack(FORMAT, event)

    if type != 0 or code != 0 or value != 0:
        print("Event type %u, code %u, value %u at %d.%d" % \
            (type, code, value, tv_sec, tv_usec))
    else:
        # Events with code, type and value == 0 are "separator" events
        print("===========================================")

    event = in_file.read(EVENT_SIZE)

in_file.close()
