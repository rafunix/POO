import teste_modulos 
import json
contagem1 = teste_modulos.obj_contagem1.contagem
contagem2 = teste_modulos.obj_contagem2.contagem
contagem3 = teste_modulos.obj_contagem3.contagem

x =  { "tombadas":contagem1, "turno_01":contagem2, "turno_02":contagem3}
y = json.dumps(x)
print(y)