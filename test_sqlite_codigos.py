import unittest
import sqlite3

from sqllite_agenda_medica import criando_banco
from sqllite_agenda_medica import agenda
from sqllite_agenda_medica import medic
from sqllite_agenda_medica import Notification
from unittest.mock import MagicMock

class test_agenda_medica(unittest.TestCase):
    def banco(self):
        self.banco = criando_banco
        self.banco.criar_agenda()

    def setUp(self):
        self.agenda = agenda()
        self.medic = medic()
        self.mock = MagicMock()
        self.notification = Notification(self.mock)
        
    def tearDown(self):
        del self.agenda
        del self.medic
        del self.mock
        del self.notification

    def test_agendar_consulta_sucess(self):
        pacient = "Eduardo"
        medic = "Rafael"
        time = "2025-07-02, 13:18"
        lista = [(pacient, medic, time)]
        lista2 = [
                ('Joao', 'Rafael', '2025-06-02, 15:30'),
                ('Mari', 'mateus', '2025-06-07, 16:50'),
                ('Carlos', 'Rafael', '2025-06-14, 09:40')
                 ]

        self.assertTrue(self.agenda.agendar_consulta(lista, pacient, medic, time))

    def test_agendar_consulta_fail(self):
        pacient = None
        medic = None
        time = None
        lista = []

        self.assertFalse(self.agenda.agendar_consulta(lista, pacient, medic, time))

    def test_cancelar_consulta(self):
        id_consulta = 34
        agenda_consulta = self.agenda.cancelar_consulta(id_consulta)
        message = "Consulta presente na agenda"
        self.assertNotIn(id_consulta, agenda_consulta, message)
    
    def test_verificar_agenda(self):
        lista = [
                (18,'Eduardo', 'Rafael', '2025-07-02, 13:18')
                ]
        agenda = self.agenda.verificar_agenda()
        self.assertEqual(lista, agenda)

        
    def test_filtrar_especialidade(self):
        filtro = 'Ortopedista'

        verificacao = [
                (1,'Joao', 'Ortopedista'),
                (3,'Maria', 'Ortopedista')
                ]
        
        filtragem = self.medic.filtrar_especialidade(filtro)
        self.assertEqual(verificacao, filtragem)   

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

if __name__ == "__main__":
    unittest.main()