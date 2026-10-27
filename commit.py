


class Commit:
    
    def __init__(self, id, mensagem, autor, pai=None):
        self.id = id
        self.mensagem = mensagem
        self.autor = autor
        self.pai = pai

    
    def historico(self):
        print(f"#{self.id} {self.mensagem} ({self.autor})")

        if self.pai is None:
            return

        self.pai.historico()



class Repositorio:
    
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.head = None
        self.contador = 0

    
    def commitar(self, mensagem):
        self.contador += 1

        novo_commit = Commit(
            self.contador,
            mensagem,
            self.autor,
            self.head
        )

        self.head = novo_commit

    
    def log(self):
        if self.head is None:
            print("Nenhum commit ainda")
            return

        self.head.historico()

    
    def total_de_commits(self):
        total = 0
        commit_atual = self.head

        while commit_atual is not None:
            total += 1
            commit_atual = commit_atual.pai

        return total



repositorio = Repositorio("meu-projeto", "Ana Souza - 6326207")


repositorio.log()


repositorio.commitar("Cria o projeto")
repositorio.commitar("Adiciona o README")
repositorio.commitar("Corrige o titulo do README")


repositorio.log()
print(repositorio.total_de_commits())
