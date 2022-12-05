import asyncio
import subprocess
import unittest
import time

import requests



class CypherAppTests(unittest.TestCase):
	""" Test the app class. """

	def test_caesar_cypher_encrypt(self):
		url = 'http://localhost:8000/caesar-cypher/encrypt'
		params = {'plaintext': 'hello', 'shift': 3}
		response = requests.get(url, params)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.text, '"khoor"')

	def test_caesar_cypher_decrypt(self):
		url = 'http://localhost:8000/caesar-cypher/decrypt'
		params = {'plaintext': 'khoor', 'shift': 3}
		response = requests.get(url, params)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.text, '"hello"')


	def test_atbash_cypher_encrypt(self):
		url = 'http://localhost:8000/atbash-cypher/encrypt'
		params = {'plaintext': 'hello'}
		response = requests.get(url, params)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.text, '"svool"')

	def test_atbash_cypher_decrypt(self):
		url = 'http://localhost:8000/atbash-cypher/decrypt'
		params = {'plaintext': 'svool'}
		response = requests.get(url, params)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.text, '"hello"')

	def test_vigenere_cypher_encrypt(self):
		url = 'http://localhost:8000/vigenere-cypher/encrypt'
		params = {'plaintext': 'hello', 'key': 'lemon'}
		response = requests.get(url, params)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.text, '"sixzb"')

	def test_vigenere_cypher_decrypt(self):
		url = 'http://localhost:8000/vigenere-cypher/decrypt'
		params = {'plaintext': 'sixzb', 'key': 'lemon'}
		response = requests.get(url, params)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.text, '"hello"')

	def test_vernam_cypher_encrypt(self):
		url = 'http://localhost:8000/vernam-cypher/encrypt'
		params = {'plaintext': 'hello', 'key': 'lemon'}
		response = requests.get(url, params)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.text, '"12 0 7 5 3"')

	def test_vernam_cypher_decrypt(self):
		url = 'http://localhost:8000/vernam-cypher/decrypt'
		params = {'plaintext': "12 0 7 5 3", 'key': 'lemon'}
		response = requests.get(url, params)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.text, '"hello"')

	def test_substitution_cypher_encrypt(self):
		url = 'http://localhost:8000/substitution-cypher/encrypt'
		params = {'plaintext': "hello", 'key_alphabet': 'zebrascdfghijklmnopqtuvwxy'}
		response = requests.get(url, params)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.text, '"daiil"')

	def test_substitution_cypher_decrypt(self):
		url = 'http://localhost:8000/substitution-cypher/decrypt'
		params = {'plaintext': "daiil", 'key_alphabet': 'zebrascdfghijklmnopqtuvwxy'}
		response = requests.get(url, params)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.text, '"hello"')

	def test_invalid_cypher(self):
		url = 'http://localhost:8000/unknown-cypher'
		response = requests.get(url)
		self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
	p = subprocess.Popen(["python", "-m", "uvicorn", "app:app", "--reload"])
	time.sleep(3)
	unittest.main()
	p.terminate()

