import unittest
import sqlite3

from sqllite_agenda_medica import criando_banco
from sqllite_agenda_medica import agenda
from unittest.mock import MagicMock

class test_agenda_medica(unittest.TestCase):
    def banco(self):
        self.banco = criando_banco
        self.banco.criar_agenda()

    def setUp(self):
        self.agenda = agenda()
        
    def tearDown(self):
        del self.agenda

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



if __name__ == "__main__":
    unittest.main()