class clase:
    def __init__(self, lista):
        self.lista= list(lista)

    def longitud(self):
        return len(self.lista)
a = [1, 3, 5, 3]

z = clase(a)
print(z.longitud())