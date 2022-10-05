from flask import Flask, request, render_template
import requests
import json
import random
from criptografar_decriptografar import cifra_cesar_criptografa
import mysql.connector

mydb = mysql.connector.connect(
    user="root", 
    password="hnqvvo84",
    host="127.0.0.1"
    )
mycursor = mydb.cursor()
mycursor.execute("create database if not exists cachorros;")
mycursor.execute("USE cachorros;")
mycursor.execute("CREATE TABLE IF NOT EXISTS `cachorros`.`fatos` (`Frase` VARCHAR(255) NOT NULL, UNIQUE INDEX `Frase_UNIQUE` (`Frase` ASC));;")
mycursor.execute("CREATE TABLE IF NOT EXISTS`cachorros`.`breeds` (`Id_Breed` INT NOT NULL AUTO_INCREMENT, `Raca` VARCHAR(100) NOT NULL, PRIMARY KEY (`Id_Breed`), UNIQUE INDEX `Id_Breed_UNIQUE` (`Id_Breed` ASC) VISIBLE, UNIQUE INDEX `Raca_UNIQUE` (`Raca` ASC) VISIBLE);")

app = Flask(__name__)

@app.route("/getraca", methods=["GET"])
def getraca():
    mydb = mysql.connector.connect(
    user="root", 
    password="hnqvvo84",
    host="127.0.0.1",
    database="cachorros"
    )
    mycursor = mydb.cursor()
    index = 0
    while (index < 172):
        response = requests.get("https://api.thedogapi.com/v1/breeds?&page=0")
        captura = json.loads(response.content)
        item = captura[index]['name']
        mycursor.execute("INSERT IGNORE INTO breeds (Raca) VALUES(%s)", (item, ))
        mydb.commit()
        print(mycursor)
        index += 1     
    mydb.close()
        
@app.route("/getfacts", methods=["GET"])
def getfacts():
    mydb = mysql.connector.connect(
    user="root", 
    password="XXXXXXXX",
    host="127.0.0.1",
    database="cachorros"
    )
    mycursor = mydb.cursor()
    index = 0
    while (index < 50):
        response = requests.get("https://dog-api.kinduff.com/api/facts")
        captura = json.loads(response.content)
        item = captura['facts'][0]
        mycursor.execute("INSERT IGNORE INTO fatos (Frase) VALUES(%s)", (item, ))
        mydb.commit()
        print(mycursor)
        index += 1     
    mydb.close()

@app.route("/getCifra", methods=["GET"])
def getcifra():
    chave = random.randint(1,47)
    requisicao = requests.get('https://dog-api.kinduff.com/api/facts')
    cifra = json.loads(requisicao.content)
    cifra_str = cifra['facts']
    print (cifra_str [0]) #apenas para verificar a frase recebida da API
    cifra_criptografa = cifra_cesar_criptografa(cifra_str[0],chave,1)
    return {
        'cifra criptografada': cifra_criptografa, 
        'chave para decriptografar': chave,
        }

@app.route("/resolveCifra", methods =["POST"])
def resolvecifra():
    parametros_teste = request.get_json()
    cifra_criptografa = parametros_teste['cifra criptografada']
    chave = parametros_teste['chave para decriptografar']
    cifra_resolvida = cifra_cesar_criptografa(cifra_criptografa,chave,2) #decriptografando
    return cifra_resolvida

    
if __name__=="__main__":
    app.run(debug=True)


