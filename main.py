import random, re, abc
from room import Office, LivingSpace, Room

# print "awesome room allocation in amity"


def strip_whitespaces(line_to_format):
    match = re.search('(\w+\s[^\s]+)\s{0,}(\w+)\s{0,}(\w?)', line_to_format)
    return match.groups()


class Employee(object):

    def set_staff(self):
        pass


class Fellow(Employee):
    pass


class Staff(Employee):



    def find_room_allocated(self):
        pass

    def allocate_office(self):
        pass


class ReadFromTextFile(object):
    fellow_living_space = LivingSpace()
    office = Office()

    def read_then_allocate(self):
        with open("input.txt", 'r') as f:
            data = f.readlines()

            for line in data:
                fullname, role, choice = strip_whitespaces(line)
                if role == "STAFF":
                    self.office.allocate(fullname, role)
                    # print 'Living Space is only allocated to fellows try \
                    #  applying to become a fellow on http://apply.andela.co'
                elif choice == "Y":
                    self.office.allocate(fullname, role)
                    self.fellow_living_space.allocate(fullname, role)
                else:
                    self.office.allocate(fullname, role)
                    # print "you are not interested in our room abi... Diaris God o"

                # print "fullname is %s and he is a %s he wants %s house" %(fullname, role, choice)
        f = open('output.txt', 'w')
        # for item in
        # f.write('\n'.join(self.staff_office.get_member_details("STAFF")))
        print >> f, self.office.get_member_details("STAFF"), self.office.get_member_details("FELLOW")
        f.close()
        print type(self.office.get_member_details("FELLOW"))
        return self.office.get_member_details("STAFF"), self.office.get_member_details("FELLOW")

    def print_output(self):
        return self.office.get_member_details("FELLOW")

    def print_living_spaace_output(self):
        return self.fellow_living_space.get_member_details_without_room_name()
        #   todo: return in this format
        #             ROOM 1 (OFFICE)
        #     MEMBER 1, MEMBER 2, MEMBER 3
        #
        #     ROOM 2 (LIVING)
        #     MEMBER 1, MEMBER 2, MEMBER 3

    def get_room_arrangement(self):
        return self.office.get_member_details("FELLOW")


    def read_data(self, role):
        fellow_names = []
        staff_names = []
        with open("input.txt", 'r') as f:
            data = f.readlines()

            for line in data:
                fullname, role, choice = strip_whitespaces(line)
                if role == "STAFF":
                    staff_names.append(fullname)
                else:
                    fellow_names.append(fullname)
        names = staff_names if role == "STAFF" else fellow_names
        return names

    def read_return_all_names(self):
        names = []
        with open("input.txt", 'r') as f:
            data = f.readlines()

            for line in data:
                fullname, role, choice = strip_whitespaces(line)
                names.append(fullname)
        return names
