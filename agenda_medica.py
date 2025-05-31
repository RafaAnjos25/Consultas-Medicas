

agenda = {
            '1': {'Nome': 'Joao', 'Medico': 'Rafael', 'Horario': '2025-06-02'},
            '2': {'Nome': 'Mari', 'Medico': 'Rafael', 'Horario': '2025-06-07'}
        }    


class EmailService:
    def send_email(self, recipient, message):
        return recipient is not None and message is not None
    
class Notification:
    def __init__(self, email_service):
        self.email_service = email_service

    def notify_pacient(self, email, message):
        return self.email_service.send_email(email, message)
    
class consulta:
    def agendar_consulta(self, id_consulta, paciente, medic, time):
        self.id_consulta = id_consulta
        self.paciente = paciente
        self.medic = medic
        self.time = time
        global agenda

        agenda = {
        self.id_consulta : {'Nome': self.paciente, 'Medico': self.medic, 'Horario': self.time}
        }
        return agenda

    def cancelar_consulta(self,id_consulta):
        global agenda
        self.id_consulta = id_consulta

        del agenda[self.id_consulta]
    
class medic:
    def filtrar_especialiade(self, filtro, filtragem):
        medicos = {
            '1': {'Nome': 'Joao', 'Especialidade': 'Ortopedista'},
            '2': {'Nome': 'Mara', 'Especialidade': 'Ortopedista'}
        }

        self.filtro = filtro

        filtragem = {
            id : detalhes    
            for id, detalhes in medicos.items()
                if detalhes['Especialidade']  == self.filtro
        }
        print(json.dumps(agenda, indent=3, ensure_ascii=False))
        return filtragem

class agenda:        
    def return_agenda():
            agenda1 = {
                    '1': {'Nome': 'Joao', 'Medico': 'Rafael', 'Horario': '2025-06-02'},
                    '2': {'Nome': 'Mari', 'Medico': 'Rafael', 'Horario': '2025-06-07'}
                }    
            return agenda1

    def vericar_agenda(self):
            valor = agenda.return_agenda()

            print(valor)
            
            for id_chave, detalhes in valor.items():
                print(f"{id_chave}: {detalhes}")
            return valor