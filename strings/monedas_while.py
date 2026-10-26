# coding = utf-8


# Define un prodecimiento, euros, que toma como entrada un entero positivo en euros
# y devuelve el número de monedas de 5 céntimos, de 2 cénts. y de 1 cénts. requeridos 
# para formar ese valor. El valor retornado debe ser una lista de tres números:
# el número de monedas de 5 cénts, de 2 cénts. y de 1 cénts. necesarias.
#
# Tu respuesta debe usar el menor número posible usandp primero cuantas más monedas
# de 5 cénts posible, luego de 2 y finalmente de 1 (para sumar el total)
def euros(valor):
    while valor <= 0:
        return [0, 0, 0]
    while valor != 0:
        amount = int(valor)   
        tipo_de_monedas = [5, 2, 1]
        result = []
        for moneda in tipo_de_monedas:
            result.append(amount // moneda)
            amount %= moneda
        return result

print(euros(8))
print(euros(29))
print(euros(-29))
print(euros(0))