import unittest
from unittest.mock import Mock, patch


class SectionTestCase(unittest.TestCase):
    def setUp(self):
        mock = Mock(name="801", course="CS361", ta="Apoorv")

    def test_removeTA(self):
        self.assertTrue(mock.removeTA())
        self.assertEqual(mock.ta, None)

    def test_setTA(self):
        self.assertTrue(mock.setTA("Apoorv"))
        self.assertEqual(mock.ta, "Apoorv")
        self.assertFalse(mock.setTA(1))