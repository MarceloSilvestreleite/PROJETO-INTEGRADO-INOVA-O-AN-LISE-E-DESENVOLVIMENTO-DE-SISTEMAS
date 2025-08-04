# Sistema de Cadastro de Pacientes para Clínica Vida+

pacientes = []

def cadastrar_paciente():
    print("\n=== CADASTRO DE PACIENTE ===")
    nome = input("Nome do paciente: ")
    
    while True:
        try:
            idade = int(input("Idade: "))
            if idade < 0 or idade > 120:
                print("Idade inválida. Digite um valor entre 0 e 120.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número válido para a idade.")
    
    telefone = input("Telefone: ")
    
    paciente = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    }
    
    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")

def calcular_estatisticas():
    if not pacientes:
        print("Nenhum paciente cadastrado ainda.")
        return
    
    total = len(pacientes)
    soma_idades = sum(paciente["idade"] for paciente in pacientes)
    media = soma_idades / total
    
    mais_novo = min(pacientes, key=lambda x: x["idade"])
    mais_velho = max(pacientes, key=lambda x: x["idade"])
    
    print("\n=== ESTATÍSTICAS ===")
    print(f"Total de pacientes: {total}")
    print(f"Idade média: {media:.1f} anos")
    print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")

def buscar_paciente():
    termo = input("\nDigite o nome do paciente a buscar: ").lower()
    encontrados = [p for p in pacientes if termo in p["nome"].lower()]
    
    if not encontrados:
        print("Nenhum paciente encontrado com esse nome.")
        return
    
    print("\n=== PACIENTES ENCONTRADOS ===")
    for paciente in encontrados:
        print(f"Nome: {paciente['nome']}")
        print(f"Idade: {paciente['idade']}")
        print(f"Telefone: {paciente['telefone']}")
        print("-----------------------")

def listar_pacientes():
    if not pacientes:
        print("Nenhum paciente cadastrado ainda.")
        return
    
    print("\n=== LISTA DE PACIENTES ===")
    for i, paciente in enumerate(pacientes, 1):
        print(f"Paciente #{i}:")
        print(f"Nome: {paciente['nome']}")
        print(f"Idade: {paciente['idade']}")
        print(f"Telefone: {paciente['telefone']}")
        print("-----------------------")

def main():
    while True:
        print("\n=== SISTEMA CLÍNICA VIDA+ ===")
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente")
        print("4. Listar todos os pacientes")
        print("5. Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue
        
        if opcao == 1:
            cadastrar_paciente()
        elif opcao == 2:
            calcular_estatisticas()
        elif opcao == 3:
            buscar_paciente()
        elif opcao == 4:
            listar_pacientes()
        elif opcao == 5:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Digite um número entre 1 e 5.")

if __name__ == "__main__":
    main()