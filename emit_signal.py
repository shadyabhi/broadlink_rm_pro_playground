#!/usr/bin/python

import pickle
import broadlink
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

    payload = sys.argv[1]
    ir_payload = pickle.load(open(payload, "rb"))
    device.send_data(ir_payload)
    print "Signal %s sent" % (payload)


if __name__ == "__main__":
    main()
