import json

class EmailService:
    def send_email(self, recipient, message):
        return recipient is not None and message is not None
    
class Notification:
    def __init__(self, email_service):
        self.email_service = email_service

    def notify_pacient(self, email, message):
        return self.email_service.send_email(email, message)
    
class consulta:
    def agendar_consulta(self, paciente, medic, time):
        return None

    def cancelar_consulta(self,id_consulta):
        return None
    
class medic:
    def filtrar_especialiade(self, filtro):
        return None
        
class agenda:
    def vericar_agenda():
        agenda = {
            '1': {'Nome': 'Joao', 'Medico': 'Rafael', 'Horario': '2025-06-02'},
            '2': {'Nome': 'Mari', 'Medico': 'Rafael', 'Horario': '2025-06-07'}
        }
        print(json.dumps(agenda, indent=3, ensure_ascii=False))
        return agenda
        