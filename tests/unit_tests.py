# generate tests for files
from confirmarPagamento import confirmarPagamento
from filaConfirmação import filaConfirmação

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

test_confirmarPagamento_success()