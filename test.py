import unittest
from unittest.mock import patch, Mock
import requests
import client  # assuming your code is in a file named client.py

class TestRegister(unittest.TestCase):
    @patch('requests.post')
    def test_register_success(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'message': 'Registration successful'}
        mock_post.return_value = mock_response

        server_url = client.register('client1', 8080)
        self.assertEqual(server_url, 'http://localhost:8080')
        mock_post.assert_called_once_with('http://localhost:8080/register', json={'client_id': 'client1', 'port': 8080})

    @patch('requests.post')
    def test_register_fail(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response

        server_url = client.register('client1', 8080)
        self.assertIsNone(server_url)
        mock_post.assert_called_once_with('http://localhost:8080/register', json={'client_id': 'client1', 'port': 8080})

    @patch('requests.post')
    def test_register_exception(self, mock_post):
        mock_post.side_effect = requests.exceptions.RequestException

        server_url = client.register('client1', 8080)
        self.assertIsNone(server_url)
        mock_post.assert_called_once_with('http://localhost:8080/register', json={'client_id': 'client1', 'port': 8080})

    @patch('requests.post')
    def test_data_shared(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'message': 'Data received'}
        mock_post.return_value = mock_response

        client_id = 'client1'
        preferred_port = 8080
        client.register(client_id, preferred_port)

        expected_url = f'http://localhost:{preferred_port}/register'
        expected_json = {'client_id': client_id, 'port': preferred_port}
        mock_post.assert_called_once_with(expected_url, json=expected_json)

if __name__ == '__main__':
    unittest.main()