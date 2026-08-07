# 1. Superclasse (Classe Mãe)

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


# 2. Subclasse (Classe Filha)

class Carro(Veiculo):
    def __init__(self, marca, modelo, qtd_portas):
        # Chama o construtor da classe mãe
        super().__init__(marca, modelo)
        self.qtd_portas = qtd_portas


# 3. Teste no Script

meu_carro = Carro("Toyota", "Corolla", 4)

print(
    f"Marca: {meu_carro.marca} | "
    f"Modelo: {meu_carro.modelo} | "
    f"Portas: {meu_carro.qtd_portas}"
)