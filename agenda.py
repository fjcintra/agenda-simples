"""
Este arquivo é dedicado para o treinamento das habilidades de programação orientada a objetos no python.
"""     

class Agenda():

    contact_id = 0
    contact_qty = 0
    contacts = {}

    def __init__(self, nome, telefone, email):
         self.__nome = nome
         self.__telefone = telefone
         self.__email = email
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def telefone(self):
        return self.__telefone
    
    @property
    def email(self):
        return self.__email
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @telefone.setter
    def telefone(self, novo_tel):
        self.__telefone = novo_tel
    
    @email.setter
    def email(self, novo_email):
        self.__email = novo_email
    
    def armazena_pessoa(self):
        """Verifica se a agenda está cheia e caso não esteja cheia adiciona um novo contato."""
        if self.contact_qty == 1:
            return f'Agenda lodata! Por favor apague um contato para poder inserir novos.'
        else:
            self.contact_id += 1
            self.contacts[self.contact_id] = [self.__nome, self.__telefone, self.__email]
            print(f'Contato {self.__nome} armazenado com sucesso!')
            self.contact_qty += 1

contato1 = Agenda('Fabio', 123456789, 'fjcintra90@gmail.com')
contato2 = Agenda('Andre', 987654321, 'arcin_es@gmail.com')

contato1.armazena_pessoa()
contato2.armazena_pessoa()