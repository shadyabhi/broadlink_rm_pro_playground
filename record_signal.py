#!/usr/bin/python

import pickle
import broadlink
import glob
import sys


def discovery_device():
    """
    discovery_device returns the first found on LAN
    """
    device = broadlink.discover()
    if device is None:
        raise Exception("RM Pro device not found")

    return device


def main():
    device = discovery_device()
    device.auth()

    print "Device under recording mode... Send signal now"
    device.enter_learning()
    raw_input("Press Enter to continue...")
    ir_packet = device.check_data()
    pickle.dump(ir_packet, open(sys.argv[1], "wb"))


if __name__ == "__main__":
    main()
