import random, re, abc

print "awesome room allocation in amity"


def strip_whitespaces(line_to_format):
    match = re.search('(\w+\s[^\s]+)\s{0,}(\w+)\s{0,}(\w?)', line_to_format)
    return match.groups()


class Room(object):
    __metaclass__ = abc.ABCMeta  # indicate that this is an ABC(Abstract base class)

    def __init__(self):
        self.no_of_occupants = 0
        self.rooms = {}

    @abc.abstractproperty
    def allocate(self, fullname, role):
        pass

    @staticmethod
    def search(values, search_for):  # there is no self there because of the static
        for k in values:
            for v in values[k]:
                if search_for in v:
                    return search_for
        return None


class Office(Room):

    def __init__(self):
        self.staff_offices_available = {"finance": [],
                                        "intern": [],
                                        "tech trainers": [],
                                        "success department": [],
                                        "kitchen": []}
        self.fellow_offices_available = {'pythonroom': [],
                                         'javascripter': [],
                                         'Rubyist': [],
                                         'ElePHPants': [],
                                         'Androiders': []}
        self.no_of_occupants = 6

    # def set_staff_office(self, office_name):
    #     return self.staff_offices_available.append(office_name)

    def get_offices(self):
        return self.staff_offices_available

    # def set_fellow_office(self, office_name):
    #     return self.fellow_offices_available.append(office_name)



    def allocate(self, fullname, role):

        for i in range(100):
            # room = random.choice(self.staff_offices_available.values())
            room = self.staff_offices_available.values() if role == "STAFF" else self.fellow_offices_available.values()
            room = random.choice(room)
            if len(room) < self.no_of_occupants:
                room.append("%s " % fullname)
                break

        return self.staff_offices_available

    def confirm_allocate(self):
        pass

    # def get_member_details(self, role):
    #     room = self.staff_offices_available if role == "STAFF" else self.fellow_offices_available
    #     print room
    #     for key, value in room.iteritems():
    #         print key, len(value)

    def get_member_details(self, role):
        room = self.staff_offices_available if role == "STAFF" else self.fellow_offices_available
        # print room
        for key, value in room.iteritems():
            print key + " (OFFICE)\n", value


class LivingSpace(Room):

    def __init__(self):
        self.no_of_occupants = 4
        self.rooms_available = {"sleeproom": [],
                                "danceroom": [],
                                "coderoom": [],
                                "cafeteria": [],
                                "carat": [],
                                "rayyan": [],
                                "glass": [],
                                "rock": [],
                                "fire": [],
                                "storm": []}

    def allocate(self, fullname, role):
        if role == "STAFF":
            return False
        else:
            for i in range(100):
                room = random.choice(self.rooms_available.values())
                if len(room) < self.no_of_occupants:
                    room.append("%s " % fullname)
                    break

        return self.rooms_available

    def get_member_details(self, office_name):
        room = self.rooms_available
        print self.rooms_available[office_name]
        list_size_of_office = []
        for key, value in self.rooms_available.iteritems():
            print key, len(value)
            list_size_of_office.append(len(value))

    def get_member_details_without_room_name(self):
        room = self.rooms_available
        # print room
        for key, value in room.iteritems():
            print key + " (LIVING SPACE)\n", value


class Employee(object):
    pass


class Fellow(Employee):
    pass


class Staff(Employee):
    pass


class ReadFromTextFile(object):
    fellow_living_space = LivingSpace()
    staff_office = Office()

    def read_then_allocate(self):
        with open("input.txt", 'r') as f:
            data = f.readlines()

            for line in data:
                fullname, role, choice = strip_whitespaces(line)
                if role == "STAFF":
                    self.staff_office.allocate(fullname, role)
                    print 'Living Space is only allocated to fellows try applying to become a fellow on http://apply.andela.co'
                elif choice == "Y":
                    self.staff_office.allocate(fullname, role)
                    self.fellow_living_space.allocate(fullname, role)
                else:
                    self.staff_office.allocate(fullname, role)
                    print "you are not interested in our room abi... Diaris God o"

                # print "fullname is %s and he is a %s he wants %s house" %(fullname, role, choice)

        return self.staff_office.get_member_details("STAFF")

    def print_output(self):
        return self.staff_office.get_member_details("FELLOW")

    def print_living_spaace_output(self):
        return self.fellow_living_space.get_member_details_without_room_name()
        #   todo: return in this format
        #             ROOM 1 (OFFICE)
        #     MEMBER 1, MEMBER 2, MEMBER 3
        #
        #     ROOM 2 (LIVING)
        #     MEMBER 1, MEMBER 2, MEMBER 3

    def get_room_arrangement(self):
        return self.staff_office.get_member_details("FELLOW")


# def file_len(fname):
#     with open(fname) as f:
#         for i, l in enumerate(f):
#             pass
#     return i + 1
#
#
# num_lines = sum(1 for line in open('input.txt'))
# # print num_lines
#
# # print file_len("input.txt")
