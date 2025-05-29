import unittest
import datetime
from agenda_medica import Notification
from agenda_medica import consulta
from unittest.mock import MagicMock

class test_agenda_medica(unittest.TestCase):
    def setUp(self):
        self.mock = MagicMock()
        self.notification = Notification(self.mock)
        self.consulta = consulta()

    def tearDown(self):
        del self.mock
        del self.notification

    def test_notification_sucess(self):
        email = "guts@gmai.com"
        message = "Dia da consulta"

        self.mock.send_email.return_value = True
        self.assertTrue(self.notification.notify_pacient(email, message))

        self.mock.send_email.assert_called_once_with(email, message)

    def test_notification_fail(self):
        email = None
        message = None

        self.mock.send_email.return_value = False
        self.assertTrue(self.notification.notify_pacient(email, message))

        self.mock.send_email.assert_called_once_with(email, message)

    def test_agendar_consulta_sucess(self):
        pacient = "Eduardo"
        medic = "Rafael"
        time = datetime.datetime(2025, 6, 7, 14, 20, 0)

        self.consulta.agendar_consulta.return_value = True
        self.assertTrue(self.consulta.agendar_consulta(pacient, medic, time))

    def test_agendar_consulta_fail(self):
        pacient = None
        medic = None
        time = None

        self.consulta.agendar_consulta.return_value = False
        self.assertFalse(self.consulta.agendar_consulta(pacient, medic, time))

    def test_cancelar_consulta_sucess(self):
        id_consulta = 1

        self.consulta.cancelar_consulta.return_value = True
        self.assertTrue(self.consulta.cancelar_consulta(id_consulta))

    def test_cancelar_consulta_fail(self):
        id_consulta = 1

        self.consulta.cancelar_consulta.return_value = False
        self.assertFalse(self.consulta.cancelar_consulta(id_consulta))

if __name__ == "__main__":
    unittest.main()