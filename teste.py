import pytest
from main import *

# Resetando o sistema antes de cada teste
@pytest.fixture(autouse=True)
def resetar_sistema():
    resetar()

def testaCriarUsuarioValido():
    criar_usuario("Gleison")
    assert usuarios[0] == {
        'id': 1, 'nome': 'Gleison', 'seguidores': [], 'seguindo': []
    }

def testaCriarUsuarioSemNome():
    with pytest.raises(Exception):
        criar_usuario("") 

def testaCriarPostagemValida():
    criar_usuario("Maria")
    criar_postagem(1, "Olá Mundo")
    assert postagens[0] == {
        'id': 1, 'usuario': 1, 'mensagem': 'Olá Mundo', 'curtidores': [], 'comentarios': []
    }

def testaCriarPostagemTextoEmBranco():
    criar_usuario('Arthur')
    with pytest.raises(Exception):
        criar_postagem(1, "")

def testaCriarPostagemUsuarioInexistente():
    with pytest.raises(IndexError):
        criar_postagem(999, "Postagem de usuário inexistente")

def testaSeguirUsuarioExistente():
    criar_usuario('Gleison')
    criar_usuario('Karen')
    seguir_usuario(1, 2)
    assert usuarios[0]['seguindo'] == [2]
    assert usuarios[1]['seguidores'] == [1]

def testaSeguirUsuarioInexistente():
    criar_usuario('Gleison')
    with pytest.raises(IndexError):
        seguir_usuario(1, 999)

def testaSeguirMesmoUsuario():
    criar_usuario('Gleison')
    with pytest.raises(Exception):
        seguir_usuario(1, 1) 

def testaCurtirPostagemValida():
    criar_usuario('Gleison')
    criar_usuario('José')
    criar_postagem(1, 'Acorda povo!')
    curtir_postagem(2, 1)
    assert postagens[0]['curtidores'] == [2]

def testaCurtirPostagemNovamente():
    criar_usuario('Gleison')
    criar_usuario('José')
    criar_postagem(1, 'Adoro testar!')
    curtir_postagem(2, 1)
    with pytest.raises(Exception):
        curtir_postagem(2, 1) 

def testaCurtirPostagemInexistente():
    criar_usuario('Gleison')
    criar_postagem(1, 'Postagem válida')

    with pytest.raises(IndexError):
        curtir_postagem(1, 999) 

def testaComentarPostagemValido():
    criar_usuario('Gleison')
    criar_postagem(1, 'Postagem importante!')
    comentar_postagem(1, 1, 'Muito bom!')
    assert postagens[0]['comentarios'] == [{'usuario': 1, 'texto': 'Muito bom!'}]

def testaComentarTextoEmBranco():
    criar_usuario('Gleison')
    criar_postagem(1, 'Postagem válida')

    with pytest.raises(ValueError):
        comentar_postagem(1, 1, '')

def testaComentarPostagemInexistente():
    criar_usuario('Gleison')
    with pytest.raises(IndexError):
        comentar_postagem(1, 999, "Comentário")


def testaExcluirContaValido():
    resetar()
    criar_usuario('Rafael')
    criar_usuario('Miguel')
    criar_postagem(1, 'Olá Mundo')
    
    excluir_conta(1)

    with pytest.raises(IndexError):
        encontrar_usuario_por_id(1)
    
    assert len(postagens) == 0
