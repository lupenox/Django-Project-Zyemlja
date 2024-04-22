import unittest, course
from unittest.mock import Mock


class MyTestCase(unittest.TestCase):

    def setUp(self):
        mock = CourseClass(name="CS361", instructors="Rock", ta=["Apoorv", "Tarun"],
                           sections=["801", "802", "803", "804"])

    def test_addTA(self):
        self.assertTrue(mock.addTA("Lizze"))
        self.assertIn("Lizzie", mock.ta)
        self.assertFalse(mock.addTA(1))

    def test_removeTA(self):
        self.assertTrue(mock.removeTA("Apoorv"))
        self.assertNotIn("Apoorv", mock.ta)
        self.assertFalse(mock.removeTA("Lizzie"))

    def test_addSection(self):
        self.assertTrue(mock.addSection("805"))
        self.assertIn("805", mock.sections)
        self.assertFalse(mock.addSection(2))

    def test_removeSection(self):
        self.assertTrue(mock.removeSection("801"))
        self.assertNotIn("801", mock.sections)
        self.assertFalse(mock.removeSection("609"))

    def test_getTAs(self):
        self.assertEqual(mock.getTAs(), ["Apoorv", "Tarun"])

    def test_getSections(self):
        self.assertEqual(mock.getSections(), ["801", "802", "803", "804"])
