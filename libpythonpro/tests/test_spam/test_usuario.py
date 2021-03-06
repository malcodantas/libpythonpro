class Conexao:
    def gerar_sessao(self):
        return Sessao()
    def fechar(self):
        pass

class Usuario:
    def __init__(self,nome):
        self.nome = nome
        self.id = None

class Sessao:
    contador = 0
    usuarios=[]
    def salvar(self,usuario):
        Sessao.contador += 1
        usuario.id = Sessao.contador
        self.usuarios.append(usuario)
    def listar(self):
        return self.usuarios

    def roll_back(self):
        pass
    def fechar(self):
        pass

def test_salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuario = Usuario(nome='Renzo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id,int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()

def test_listar_usuarios():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuarios = [Usuario(nome='Renzo'),Usuario(nome='Malco')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()
