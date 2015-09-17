import unittest
from main import Fellow, Staff, LivingSpace, Office, ReadFromTextFile


class TestingOfficeAllocation(unittest.TestCase):
    """TODO: implement all this test to pass"""

    def setUp(self):
        self.fel = Fellow()
        self.stf = Staff()
        self.living_space = LivingSpace()
        self.ofc = Office()
        self.read_txt = ReadFromTextFile()

    def test_can_allocate_staff_to_office(self):
        self.ofc.allocate("Chidi", "STAFF")
        self.assertEqual("Chidi", self.ofc.search(self.ofc.staff_offices_available, "Chidi"))

    def test_can_allocate_fellow_to_office(self):
        self.ofc.allocate("Jubril", "FELLOW")
        self.assertEqual("Jubril", self.ofc.search(self.ofc.fellow_offices_available, "Jubril"))

    def test_cannot_add_fellow_to_staff_office(self):
        self.ofc.allocate("Inioluwa", "FELLOW")
        self.assertNotEqual("Inioluwa", self.ofc.search(self.ofc.staff_offices_available, "Inioluwa"), msg="You are not a staff")

    def test_cannot_add_staff_to_fellow_office(self):
        self.ofc.allocate("Prosper", "STAFF")
        self.assertNotEqual("Prosper", self.ofc.search(self.ofc.fellow_offices_available, "Prosper"), msg="You are not a fellow")

    def test_can_allocate_office_to_staff(self):
        self.read_txt.read_then_allocate()
        # self.assertLessEqual(7, )

    def test_staff_is_not_allocated_to_living_space(self):
        self.living_space.allocate("Nadayar", "STAFF")
        # self.assertIn("Nadayar", self.living_space.rooms_available)
        self.assertNotEqual("Nadayar", self.ofc.search(self.living_space.rooms_available, "Nadayar"), msg="You are not a fellow")

    def test_people_allocated_to_offices_are_not_more_than_six(self):
        pass

    def test_people_allocated_to_living_space_are_not_more_than_four(self):
        pass

    def test_fellow_not_interested_in_room_not_given(self):
        self.read_txt.fellow_living_space.allocate("NWAMINA PHILLIPS", "FELLOW")
        self.assertNotEqual("NWAMINA PHILLIPS", self.ofc.search(self.living_space.rooms_available, "NWAMINA PHILLIPS"), msg="You are not a fellow")




# def test_calculator_add_method_returns_correct_result(self):
#         result = self.calc.add(2, 2)
#         self.assertEqual(4, result)
#
#     def test_calculator_returns_error_message_if_both_args_not_numbers(self):
#         self.assertRaises(ValueError, self.calc.add, 'two', 'three')
#
#     def test_calculator_returns_error_message_if_x_arg_not_numbers(self):
#         self.assertRaises(ValueError, self.calc.add, 'two', 3)
#
#     def test_calculator_returns_error_message_if_y_arg_not_numbers(self):
#         self.assertRaises(ValueError, self.calc.add, 2, 'three')
