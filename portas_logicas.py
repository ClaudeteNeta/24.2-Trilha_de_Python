# Como funcionam?
falta_pao= True
falta_cafe = False 
# ATALHO:
# AND
# Porta Pessimista
if (falta_cafe and falta_pao):
    print("AND: Precisamos ir ao Guanabara!")

# OR
# Porta Otimista 
if falta_cafe or falta_pao:
    print("OR: Precisamos ir ao Guanabara!")

# NOT
# Porta do contra 
print(not True)