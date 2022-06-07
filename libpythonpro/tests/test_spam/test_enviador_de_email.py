import pytest
from libpythonpro.spam.enviador_de_email import Enviador
def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None
@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br','renzo@python.pro.br']
    )
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
                    destinatario,
                    'malcodantas18@gmail.com',
                    'Curso python Pro',
                    'turma do curso de python')
    assert destinatario in resultado