import sqlite3
'''
conn = sqlite3.connect('agendaDATABASE.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Medico (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Especialidade TEXT NOT NULL
);          
""")

print('Tabela criada com sucesso.')
conn.close()'''


conn = sqlite3.connect('agendaDATABASE.db')
cursor = conn.cursor()

cursor.execute("""
INSERT INTO Medico (Nome, Especialidade) Values ('Joao', 'Ortopedista')
""")               
cursor.execute("""
INSERT INTO Medico (Nome, Especialidade) Values ('Rafael', 'Oftalmologista')
""")
cursor.execute("""
INSERT INTO Medico (Nome, Especialidade) Values ('Maria', 'Ortopedista')
""")
cursor.execute("""
INSERT INTO Medico (Nome, Especialidade) Values ('Carlos', 'Pediatra')
""")
cursor.execute("""
INSERT INTO Medico (Nome, Especialidade) Values ('Joao', 'Psicologo')
""")

conn.commit()
print('Dados inseridos')
conn.close()