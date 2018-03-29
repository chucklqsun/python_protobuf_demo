from apollo import conti_radar_pb2
import sys


def get_header_info(radar_data):
    print(radar_data.header)


def list_obstacles(radar_data):
    pass
    # for person in address_book.people:
    #     print("Person ID:", person.id)
    #     print("  Name:", person.name)
    #     if person.HasField('email'):
    #         print("  E-mail address:", person.email)
    #
    #     for phone_number in person.phones:
    #         if phone_number.type == addressbook_pb2.Person.MOBILE:
    #             print("  Mobile phone #: ")
    #         elif phone_number.type == addressbook_pb2.Person.HOME:
    #             print("  Home phone #: ")
    #         elif phone_number.type == addressbook_pb2.Person.WORK:
    #             print("  Work phone #: ")
    #         print(phone_number.number)


if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "radar_data_file")
    sys.exit(-1)

radar_data = conti_radar_pb2.ContiRadar()

# Read the existing address book.
f = open(sys.argv[1], "rb")
radar_data.ParseFromString(f.read())
f.close()

get_header_info(radar_data)
