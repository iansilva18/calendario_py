
from caloendario import *
class Agenda:
    def __init__(self):
 
        self.listaContatos = []
        
    def salvar_contatos(self):
        self.listaContatos.append(Contato())

    def listar_contatos(self):
        for i in range(len(self.listaContatos)):
            print('Código: ', self.listaContatos[i].cod,
            'Nome: ', self.listaContatos[i].nome,
            'Telefone: ', self.listaContatos[i].telefone)
            
            