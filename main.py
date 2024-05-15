from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/ping")
def pong():
	return "pong"

@app.get("/55")
def busqueda():
	response = requests.get("https://www.simcompanies.com/api/v4/es/0/encyclopedia/resources/1/50/")
	response = response.json
	print(response)
	return response