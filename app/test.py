import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        # Configura o cliente de teste do Flask
        self.app = app.test_client()
        self.app.testing = True

    def test_pagina_inicial_status_code(self):
        # Testa se a página inicial retorna o status 200
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_pagina_inicial_conteudo(self):
        # Testa se a página inicial retorna o conteúdo esperado
        response = self.app.get('/')
        self.assertEqual(response.data.decode('utf-8'), "Continuous Integration and Continuous Delivery")

    def test_pagina_inexistente(self):
        # Testa se uma rota inexistente retorna o status 404
        response = self.app.get('/rota-inexistente')
        self.assertEqual(response.status_code, 404)

    def test_metodo_nao_permitido(self):
        # Testa se um método não permitido (POST) retorna o status 405
        response = self.app.post('/')
        self.assertEqual(response.status_code, 405)

    def test_headers(self):
        # Testa se os headers da resposta contêm o tipo de conteúdo correto
        response = self.app.get('/')
        self.assertIn('Content-Type', response.headers)
        self.assertEqual(response.headers['Content-Type'], 'text/html; charset=utf-8')

if __name__ == '__main__':
    unittest.main()