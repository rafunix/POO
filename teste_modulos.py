import random
#Autor: Rafael Araujo 
class obj_contagem(object):

    def __init__(self, contagem):
        self.contagem = contagem
                 
    def __str__(self):
        return self.tombadas


gerador = random.randrange(1,60)
obj_contagem1 = obj_contagem(gerador)
obj_contagem2 = obj_contagem(gerador)
obj_contagem3 = obj_contagem(gerador)
