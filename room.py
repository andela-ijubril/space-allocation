import abc
import random

__author__ = 'Jubril'


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


    # Todo: Find room by name
    # Todo: Add rooms
    # Todo: Update room count
    # Todo: remove rooms
    # Todo: all rooms filled



class Office(Room):

    def __init__(self):
        # super(Office, self).__init__()
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
        self.available_space = (len(self.staff_offices_available) + len(
            self.fellow_offices_available)) * self.no_of_occupants

    def add_staff_office(self, office_name):
        # the fastest way to set an office
        self.staff_offices_available[office_name] = []
        return self.staff_offices_available

    def list_staff_offices(self):
        return self.staff_offices_available

    def add_fellow_office(self, office_name):
        self.fellow_offices_available[office_name] = []
        return self.fellow_offices_available

    def remove_staff_office(self, office_name):
        if office_name in self.staff_offices_available:
            del self.staff_offices_available[office_name] # self.staff_offices_available[office_name].pop(office_name, None)
        else:
            return office_name + "is not currently a valid office name"

    def rename_office_name(self, old_name, new_name):
        pass # mydict[new_key] = mydict.pop(old_key)

    # or
    # if newkey!=oldkey:
    #   dictionary[newkey] = dictionary[oldkey]
    #   del dictionary[oldkey]

    def no_of_occupant_in_the_room(self, office):
        pass

    def list_of_filled_rooms(self):
        pass

    def list_of_available_rooms(self):
        pass

    def allocate(self, fullname, role):

        for i in range(self.available_space):
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
