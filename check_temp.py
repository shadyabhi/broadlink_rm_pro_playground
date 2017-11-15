import pickle
import broadlink
import glob


def discovery_device():
    """
    discovery_device returns the first found on LAN
    """
    device = broadlink.discover()
    if device is None:
        raise Exception("RM Pro device not found")

    return device


def read_payloads():
    """
    #read_payloads reads all IR payloads available
    """
    payloads = glob.glob("./payloads/*")
    if len(payloads) < 1:
        raise Exception("No payloads found")
    else:
        return payloads


def main():
    device = discovery_device()
    device.auth()

    print device.check_temperature()


if __name__ == "__main__":
    main()
