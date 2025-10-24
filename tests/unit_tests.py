from ConfirmaPagamento import confirmarPagamento
from ConfirmaPagamentosFila import filaConfirmação

def test_confirmarPagamento_success():
    payload = {
        "agencia": "1234",
        "conta": "56789-0",
        "tipo_conta": "corrente",
        "valor": 150.00
    }
    filaConfirmação.put(payload)
    assert confirmarPagamento() == {"status": 200, 
                    "mensagem": "Pagamento confirmado com sucesso!"}

def test_confirmarPagamento_fail():
    payload = {
        #"agencia": "0000",
        "conta": "00000-0",
        "tipo_conta": "poupanca",
        "valor": 200.00
    }
    filaConfirmação.put(payload)
    assert confirmarPagamento() == {'status': 500,
                                    "mensagem": "Preencha todos os campos obrigatórios!"}
test_confirmarPagamento_success()
test_confirmarPagamento_fail()