import sqlite3

class criando_banco:
    def criar_agenda():
        conn = sqlite3.connect('agendaDATABASE.db')
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS agenda (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                paciente TEXT NOT NULL,
                medico TEXT NOT NULL,
                time TEXT NOT NULL
                );          
        """)
        print('Tabela criada com sucesso.')
        conn.close()
    criar_agenda()

class medic:
   def filtrar_especialidade(self, especialidade):
        conn = sqlite3.connect('agendaDATABASE.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM Medico
        WHERE Especialidade = ?              
        """, (especialidade,))

        filtragem = cursor.fetchall() 

        for linha in filtragem:
            print(linha)
        conn.close()

        return filtragem

class agenda:
    
    def agendar_consulta(self, lista, pacient, medic, time):
        if pacient is not None and medic is not None and time is not None:
            conn = sqlite3.connect('agendaDATABASE.db')
            cursor = conn.cursor()

            cursor.executemany("""
            INSERT INTO agenda (paciente, medico, time)
            VALUES (?,?,?)""", lista)
      
            conn.commit()

            print('Dados inseridos com sucesso')

            conn.close()
            return True
        else:
            return False
        
    def verificar_agenda(self):
        conn = sqlite3.connect('agendaDATABASE.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM agenda;               
        """)

        agenda = cursor.fetchall() 

        for linha in agenda:
            print(linha)
        conn.close()
        return agenda
    
    def cancelar_consulta(self, id_consulta):
        conn = sqlite3.connect('agendaDATABASE.db')
        cursor = conn.cursor()

        cursor.execute("""
        DELETE FROM agenda
        WHERE id = ?    
        """,(id_consulta,))

        conn.commit()
        print('Consulta excluida com sucesso.')

        cursor.execute("""
        SELECT * FROM agenda;               
        """)

        agenda = cursor.fetchall()
        conn.close()
        return agenda

class EmailService:
    def send_email(self, recipient, message):
        return recipient is not None and message is not None
    
class Notification:
    def __init__(self, email_service):
        self.email_service = email_service

    def notify_pacient(self, email, message):
        return self.email_service.send_email(email, message)    