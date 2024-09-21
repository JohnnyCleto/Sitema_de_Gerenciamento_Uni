from pessoa import Pessoa, Aluno, Professor, Disciplina, Escola

def criar_aluno():
    nome = input("\nNome do aluno: ")
    idade = input("Idade do aluno: ")
    cpf = input("CPF do aluno: ")
    matricula = input("Matrícula do aluno: ")
    return Aluno(nome, idade, cpf, matricula)

def criar_professor():
    nome = input("\nNome do professor: ")
    idade = input("Idade do professor: ")
    cpf = input("CPF do professor: ")
    salario = float(input("Salário do professor: "))
    return Professor(nome, idade, cpf, salario)

def criar_disciplina(professores):
    nome = input("\nNome da disciplina: ")
    codigo = input("Código da disciplina: ")
    for idx, professor in enumerate(professores):
        print(f"{idx + 1}. {professor.nome}")
    opcao = int(input("Escolha o professor pelo índice: ")) - 1
    if opcao < 0 or opcao >= len(professores):
        print("Professor inválido!")
        return None
    return Disciplina(nome, codigo, professores[opcao])

# Sistema de gerenciamento
escola = Escola("Universidade de Vassouras")

while True:
    print("\n--- Sistema de Gerenciamento Universitário ---")
    print("1. Adicionar aluno")
    print("2. Adicionar professor")
    print("3. Adicionar disciplina")
    print("4. Exibir alunos")
    print("5. Exibir professores")
    print("6. Exibir disciplinas")
    print("7. Adicionar aluno em disciplina")
    print("0. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        aluno = criar_aluno()
        escola.adicionar_aluno(aluno)
    elif opcao == 2:
        professor = criar_professor()
        escola.adicionar_professor(professor)
    elif opcao == 3:
        if len(escola.professores) == 0:
            print("\nNão há professores cadastrados.")
        else:
            disciplina = criar_disciplina(escola.professores)
            if disciplina:
                escola.adicionar_disciplina(disciplina)
    elif opcao == 4:
        escola.exibir_alunos()
    elif opcao == 5:
        escola.exibir_professores()
    elif opcao == 6:
        escola.exibir_disciplinas()
    elif opcao == 7:
        escola.adicionar_aluno_na_disciplina()
    elif opcao == 0:
        print("\nSaindo do sistema...")
        break
    else:
        print("\nOpção inválida! Tente novamente.")
