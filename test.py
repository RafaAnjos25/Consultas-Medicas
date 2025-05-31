def return_agenda():
        agenda1 = {
                '1': {'Nome': 'Joao', 'Medico': 'Rafael', 'Horario': '2025-06-02'},
                '2': {'Nome': 'Mari', 'Medico': 'Rafael', 'Horario': '2025-06-07'}
            }    
        return agenda1

def vericar_agenda(self):
        valor = return_agenda()

        print(valor)
        
        for id_chave, detalhes in valor.items():
            print(f"{id_chave}: {detalhes}")

if __name__ == '__main__':
        vericar_agenda()