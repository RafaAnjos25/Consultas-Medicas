import unittest
from agenda_medica import Notification
from agenda_medica import medic
from agenda_medica import agenda
from unittest.mock import MagicMock


class test_agenda_medica(unittest.TestCase):
    def setUp(self):
        self.mock = MagicMock()
        self.notification = Notification(self.mock)
        self.medic = medic()
        self.agenda = agenda()

    def tearDown(self):
        del self.mock
        del self.notification
        del self.agenda
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
        self.assertFalse(self.notification.notify_pacient(email, message))

        self.mock.send_email.assert_called_once_with(email, message)

    def test_agendar_consulta_sucess(self):
        id_consulta = '3'
        pacient = "Eduardo"
        medic = "Rafael"
        time = "2025-07-02, 13:18"

        self.assertTrue(self.agenda.agendar_consulta(id_consulta, pacient, medic, time))

    def test_agendar_consulta_fail(self):
        id_consulta = None
        pacient = None
        medic = None
        time = None

        self.assertFalse(self.agenda.agendar_consulta(id_consulta, pacient, medic, time))

    def test_cancelar_consulta_sucess(self):
        id_consulta = '1'

        self.assertTrue(self.agenda.cancelar_consulta(id_consulta))

    def test_verificar_agenda(self):
        self.assertTrue(self.agenda.vericar_agenda())

    def test_filtrar_especialidade(self):
        filtro = 'Ortopedista'

        verificacao = {
            '1': {'Nome': 'Joao', 'Especialidade': 'Ortopedista'},
            '2': {'Nome': 'Mara', 'Especialidade': 'Ortopedista'}}
        
        filtragem = self.medic.filtrar_especialiade(filtro)
        self.assertEqual(verificacao, filtragem)

if __name__ == "__main__":
    unittest.main()