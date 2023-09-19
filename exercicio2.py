valorcompra = float(input("Digite a compra: $ "))

if valorcompra <= 1000:
    desconto = valorcompra * 0.10
elif valorcompra <= 5000:
    desconto = valorcompra * 0.20
else:
    desconto = valorcompra * 0.30
total = valorcompra - desconto

print(f"Desconto: $ {desconto:.1f}")
print(f"Valortotal : $ {total:.1f}")
