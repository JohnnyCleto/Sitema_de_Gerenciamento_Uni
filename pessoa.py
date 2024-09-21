class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, CPF: {self.cpf}")


class Aluno(Pessoa):
    def __init__(self, nome, idade, cpf, matricula):
        super().__init__(nome, idade, cpf)
        self.matricula = matricula
        self.disciplinas = []

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Matrícula: {self.matricula}")
        print("Disciplinas:")
        for disciplina in self.disciplinas:
            print(f" - {disciplina.nome}")


class Professor(Pessoa):
    def __init__(self, nome, idade, cpf, salario):
        super().__init__(nome, idade, cpf)
        self.salario = salario

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Salário: {self.salario}")


class Disciplina:
    def __init__(self, nome, codigo, professor):
        self.nome = nome
        self.codigo = codigo
        self.professor = professor
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        aluno.adicionar_disciplina(self)

    def exibir_informacoes(self):
        print(f"Disciplina: {self.nome}, Código: {self.codigo}")
        print(f"Professor: {self.professor.nome}")
        print("Alunos matriculados:")
        for aluno in self.alunos:
            print(f" - {aluno.nome}")


class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []
        self.professores = []
        self.disciplinas = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def exibir_alunos(self):
        print("\nAlunos matriculados:")
        for aluno in self.alunos:
            aluno.exibir_informacoes()

    def exibir_professores(self):
        print("\nProfessores cadastrados:")
        for professor in self.professores:
            professor.exibir_informacoes()

    def exibir_disciplinas(self):
        print("\nDisciplinas oferecidas:")
        for disciplina in self.disciplinas:
            disciplina.exibir_informacoes()

    def adicionar_aluno_na_disciplina(self):
        if len(self.disciplinas) == 0:
            print("Não há disciplinas cadastradas.")
            return

        if len(self.alunos) == 0:
            print("Não há alunos cadastrados.")
            return

        # Exibir disciplinas disponíveis
        print("\nDisciplinas disponíveis:")
        for idx, disciplina in enumerate(self.disciplinas):
            print(f"{idx + 1}. {disciplina.nome}")

        disciplina_idx = int(input("Escolha a disciplina pelo índice: ")) - 1
        if disciplina_idx < 0 or disciplina_idx >= len(self.disciplinas):
            print("Disciplina inválida!")
            return

        # Exibir alunos disponíveis
        print("\nAlunos disponíveis:")
        for idx, aluno in enumerate(self.alunos):
            print(f"{idx + 1}. {aluno.nome}")

        aluno_idx = int(input("Escolha o aluno pelo índice: ")) - 1
        if aluno_idx < 0 or aluno_idx >= len(self.alunos):
            print("Aluno inválido!")
            return

        # Adicionar o aluno à disciplina
        disciplina = self.disciplinas[disciplina_idx]
        aluno = self.alunos[aluno_idx]
        disciplina.adicionar_aluno(aluno)
        print(f"Aluno {aluno.nome} adicionado à disciplina {disciplina.nome}.")
