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