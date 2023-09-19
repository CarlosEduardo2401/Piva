largura = float(input("Digite a largura  em metros: "))
comprimento = float(input("Digite o comprimento  em metros: "))
pe_direito = 2.80
area_paredes = 2 * (largura + comprimento) * pe_direito
larguraporta = 0.80
alturaporta = 2.10
areaporta = larguraporta * alturaporta
area_paredes -= areaporta
quantidade_tinta_por_lata = float(input("Digite a quantidade de tinta por lata em litros: "))
litros_tinta_necessarios = area_paredes / 3

quantidade_latas_tinta = litros_tinta_necessarios / quantidade_tinta_por_lata


import math
quantidade_latas_tinta = math.ceil(quantidade_latas_tinta)
print(f"Quantidade de latas de tinta necessárias: {quantidade_latas_tinta}")
