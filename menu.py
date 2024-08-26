class Escola:
    def __init__ (self):
        self.turma = []
        self.professor = []
        self.estudante = []
        self.notaSalva = []
        self.nota = []
    
    def mostrar_menu(self):
        print("\nEscolha uma opção:")
        print("1 - Criar Turma")
        print("2 - Adicionar Professor")
        print("3 - Adicionar Estudante")
        print("4 - Adicionar Nota")
        print("5 - Consultar Nota")
        print("6 - Salvar Nota")
        print("7 - Sair\n")

    def criarTurma(self):
        numTurma = input("Digite o nome da Turma: ")
        self.turma.append(numTurma)
        print(f"Turma '{numTurma}' foi criada.")
    
    def adicionarProfessor(self):
        nomeProfessor = input("Digite o nome do Professor: ")
        self.professor.append(nomeProfessor)
        print(f"Professor: '{nomeProfessor} atribuido.")
    
    def adicionarEstudante(self):
        nomeEstudante = input("Digite o nome do Estudante: ")
        self.estudante.append(nomeEstudante)
        print(f"Aluno: '{nomeEstudante}' atribuido.")
        
    def consultarNota(self):
        print("Consultando nota")
    
    def adicionarNota(self):
        nota = input("Digite a nota: ")
        self.notaSalva.append(nota)
        print("Nota foi salva.")

    def salvarNota(self):
        print("Salvando nota")
        
    def sair(self):
        print("Saindo")
        
escolinha = Escola()

escolhas = {
    "1": escolinha.criarTurma,
    "2": escolinha.adicionarProfessor,
    "3": escolinha.adicionarEstudante,
    "4": escolinha.adicionarNota,
    "5": escolinha.consultarNota,
    "6": escolinha.salvarNota,
    "7": escolinha.sair,
}

while True:
    escolinha.mostrar_menu()
    try:
        escolha = input("Escolha um valor: ")
        escolhas[escolha]()
        if escolha == "7":
            break
    except:
        print("Opção invalida.")
