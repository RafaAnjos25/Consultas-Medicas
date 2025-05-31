import unittest
from agenda_medica import Notification
from agenda_medica import consulta
from agenda_medica import medic
from agenda_medica import agenda
from unittest.mock import MagicMock


class test_agenda_medica(unittest.TestCase):
    def setUp(self):
        self.mock = MagicMock()
        self.notification = Notification(self.mock)
        self.consulta = consulta()
        self.medic = medic()
        self.agenda = agenda()

    def tearDown(self):
        del self.mock
        del self.notification
        del self.consulta
        del self.medic

    def test_verificar_agenda(self):
        self.assertTrue(self.agenda.vericar_agenda())

if __name__ == "__main__":
    unittest.main()