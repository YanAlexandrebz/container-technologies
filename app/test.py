from app import app
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        # Cria uma instância do unittest, precisa do nome "setUp"
        self.app = app.test_client()

    def test_requisicao(self):
        # Envia uma requisição GET para a URL e verifica o status
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_conteudo(self):
        # Verifica o retorno do conteúdo da página
        result = self.app.get('/')
        self.assertEqual(result.data.decode('utf-8'), "Continuous Integration and Continuous Delivery")

    def test_404(self):
        # Testa uma rota inexistente para garantir que retorna 404
        result = self.app.get('/rota-inexistente')
        self.assertEqual(result.status_code, 404)

    def test_metodo_post(self):
        # Testa um método POST na rota principal (se aplicável)
        result = self.app.post('/')
        self.assertEqual(result.status_code, 405)  # Método não permitido (se não implementado)

    def test_headers(self):
        # Verifica os headers da resposta
        result = self.app.get('/')
        self.assertIn('Content-Type', result.headers)
        self.assertEqual(result.headers['Content-Type'], 'text/html; charset=utf-8')

if __name__ == '__main__':
    unittest.main()