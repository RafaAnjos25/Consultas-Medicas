class EmailService:
    def send_email(self, recipient, message):
        return recipient is not None and message is not None
    
class Notification:
    def __init__(self, email_service):
        self.email_service = email_service

    def notify_pacient(self, email, message):
        return self.email_service.send_email(email, message)
    
    
class medic:
    def filtrar_especialiade(self, filtro):
        medicos = {
            '1': {'Nome': 'Joao', 'Especialidade': 'Ortopedista'},
            '2': {'Nome': 'Mara', 'Especialidade': 'Ortopedista'},
            '3': {'Nome': 'Jose', 'Especialidade': 'Pediatra'},
            '4': {'Nome': 'Rafael', 'Especialidade': 'Oftamologista'}
        }

        filtragem = {
            id : detalhes    
            for id, detalhes in medicos.items()
                if detalhes['Especialidade']  == filtro
        }

        for id, detalhes in filtragem.items():
            print(f"{id}: {detalhes}")
        return filtragem

agenda_consulta = {
    '1': {'Nome': 'Joao', 'Medico': 'Rafael', 'Horario': '2025-06-02, 15:30'},
    '2': {'Nome': 'Mari', 'Medico': 'Rafael', 'Horario': '2025-06-07, 16:50'}
    }  

class agenda:        
    
    def agendar_consulta(self, id_consulta, paciente, medic, time):
        if paciente is not None and id_consulta is not None and medic is not None and time is not None:
            global agenda_consulta

            agenda_consulta [id_consulta] = {'Nome': paciente, 'Medico': medic, 'Horario': time}

            return True
        else:
            return False
    
    def cancelar_consulta(self,id_consulta):
        global agenda_consulta

        agenda_consulta.pop(id_consulta)
        return agenda_consulta

    def vericar_agenda(self):
        global agenda_consulta  
            
        for id_chave, detalhes in agenda_consulta.items():
            print(f"{id_chave}: {detalhes}")
        return agenda_consulta