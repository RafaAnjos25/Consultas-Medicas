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
        time = "2025-07-27"

        self.assertTrue(self.consulta.agendar_consulta(pacient, medic, time))

    def test_agendar_consulta_fail(self):
        pacient = None
        medic = None
        time = None

        self.assertFalse(self.consulta.agendar_consulta(pacient, medic, time))

    def test_cancelar_consulta_sucess(self):
        id_consulta = '1'
        agenda_consulta = self.agenda.cancelar_consulta(id_consulta)
        message = "Consulta presente na agenda"
        self.assertNotIn(id_consulta, agenda_consulta, message)

    def test_cancelar_consulta_fail(self):
        id_consulta = None

        self.assertFalse(self.consulta.cancelar_consulta(id_consulta))

    def test_filtrar_especialidade(self):
        filtro = 'Ortopedista'

        verificacao = {
            '1': {'Nome': 'Joao', 'Especialidade': 'Ortopedista'},
            '2': {'Nome': 'Mara', 'Especialidade': 'Ortopedista'}}

        filtragem = self.medic.filtrar_especialidade(filtro)
        self.assertEqual(verificacao, filtragem)

    def test_verificar_agenda(self):
        self.assertTrue(self.agenda.verificar_agenda())

if __name__ == "__main__":
    unittest.main()