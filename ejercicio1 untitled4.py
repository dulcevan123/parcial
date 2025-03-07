valor_compra = int(input("monto de la compra: "))
descuento = 0

if (valor_compra < 50):
    descuento = 0
if (50 >= valor_compra <= 100):
    descuento = 0.05
if (valor_compra > 100):
    descuento = 0.10

valor_compra_descuento = valor_compra*descuento
nuevo_valor_compra = valor_compra - valor_compra_descuento

print(f"Descuento aplicado: ${valor_compra_descuento}")
print(f"Total a pagar: ${nuevo_valor_compra}")