from apollo import conti_radar_pb2
import sys


def get_header_info(data):
    print(data.header)


def get_obstacles(data):
    print(len(data.contiobs))
    print(data.contiobs[1])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "radar_data_file")
        sys.exit(-1)

    radar_data = conti_radar_pb2.ContiRadar()

    # Read the existing address book.
    f = open(sys.argv[1], "rb")
    radar_data.ParseFromString(f.read())
    f.close()

    # get_header_info(radar_data)
    get_obstacles(radar_data)
