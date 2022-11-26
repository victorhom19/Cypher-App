import random
from string import ascii_lowercase as alphabet

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/caesar-cypher/{type}")
async def get_caesar_cypher(type, plaintext, shift=1):
	if type == 'encrypt':
		return "".join(list(map(lambda char: alphabet[(alphabet.index(char) + int(shift)) % len(alphabet)], plaintext)))
	if type == 'decrypt':
		return "".join(list(map(lambda char: alphabet[(alphabet.index(char) - int(shift)) % len(alphabet)], plaintext)))


@app.get("/atbash-cypher/{type}")
async def get_atbash_cypher(type, plaintext):
	if type in ['encrypt', 'decrypt']:
		return "".join(list(map(lambda char: alphabet[len(alphabet) - 1 - (alphabet.index(char))], plaintext)))


@app.get("/vigenere-cypher/{type}")
async def get_vigenere_cypher(type, plaintext, key):
	a, b = divmod(len(alphabet), len(key))
	extended_key = key * a + key[:b]
	result_string = ''
	if type == 'encrypt':
		for i, char in enumerate(plaintext):
			result_string += alphabet[(alphabet.index(char) + alphabet.index(extended_key[i])) % len(alphabet)]
	if type == 'decrypt':
		for i, char in enumerate(plaintext):
			result_string += alphabet[(alphabet.index(char) - alphabet.index(extended_key[i])) % len(alphabet)]
	return result_string


@app.get("/vernam-cypher/{type}")
async def get_vernam_cypher(type, plaintext, key=None):
	if type == 'encrypt':
		generated_key = ''.join(random.choices(alphabet, k=len(plaintext))) if not key else key
		result_string = []
		for i, char in enumerate(plaintext):
			result_string.append(str(alphabet.index(char) ^ alphabet.index(generated_key[i])))
		if not key:
			return f'Key was generated. Key: {generated_key}, cyphertext: {" ".join(result_string)}'
		else:
			return " ".join(result_string)
	if type == 'decrypt':
		result_string = ''
		for i, char_code in enumerate(plaintext.split()):
			print(f"{int(char_code)} ^ {alphabet.index(key[i])} = {int(char_code) ^ alphabet.index(key[i])}")
			result_string += alphabet[int(char_code) ^ alphabet.index(key[i])]
		return result_string
