from string import ascii_lowercase as alphabet

from fastapi import FastAPI

app = FastAPI()


@app.get("/caesar-cypher/{type}")
async def get_caesar_cypher(type, plaintext, shift=1):
	if type == 'encrypt':
		return "".join(list(map(lambda char: alphabet[(alphabet.index(char) + int(shift)) % len(alphabet)], plaintext)))
	if type == 'decrypt':
		return "".join(list(map(lambda char: alphabet[(alphabet.index(char) - int(shift)) % len(alphabet)], plaintext)))


@app.get("/atbash-cypher/{type}")
async def get_caesar_cypher(type, plaintext):
	if type in ['encrypt', 'decrypt']:
		return "".join(list(map(lambda char: alphabet[len(alphabet) - 1 - (alphabet.index(char))], plaintext)))
