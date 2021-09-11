print('Cargando...')
import setup
setup.setup()
import random
from spellchecker import SpellChecker
import time
import sys
import pycountry
import os
import os.path
import wikipedia
import re
import requests
import wolframalpha
import webbrowser
import glob
from PyDictionary import PyDictionary
import tmdbsimple as tmdb
import nltk
from nltk.corpus import wordnet
spell = SpellChecker()
st1=[]
hi = []
thanks=[]
yes=[]
for syn in wordnet.synsets("hi"):
    for l in syn.lemmas():
        hi.append(l.name())      
app_id='XPAQWX-W5LAG5ELYL'
client=wolframalpha.Client(app_id)
tmdb.API_KEY = '60222ace6396c345f94cc42eaac5dae5'
doss = os.getcwd()
i=0
n=0
flag=0
dictionary=PyDictionary()
ameye=("artificial intelligence")
my = []
tco = ()
iam=[]
lnames=[]
info = []
add1=()
add2=()
infa = []
lstn=()
ups = ()
clear = lambda: os.system('cls')
nxt = (0)
nxts =(4)
nogt = (0)
noot = (1)
myname = ("Jarvis")
commands = []
action = []
os.system('cls')
print ("Hola")
name = input ("¿Cual es tu nombre? >>> ")
print ("Hola, " + name)
while 1==1:
    response = input("Escribe un comando >>> ")
    st1=response.split()
    for x in range(len(st1)):
        st1[x]=(spell.correction(st1[x]))
    response=" ".join(str(x) for x in st1)
    if response == "Que hora es" or response=='Que hora es ahorita':
        print(time.strftime("%I")+':'+time.strftime('%M %p'))
    elif response == "cual es la fecha":
        print (time.strftime (" %A, %B %e, %Y"))
    elif ('quien eres') in response:
        print("Soy Jarvis, tu asistente personal")
    elif ('que eres') in response:
        print("Soy una Inteligencia Artificial")
    elif ('asombroso') in response:
        print("Así es")
    elif ('cual es tu color favorito') in response:
        print("Amarillo como el sol")
    elif ('te amo') in response:
        print("y yo a ti, ", name)
    elif ('que puedes hacer') in response:
        print("Puedo hacer tareas como reproducir música, videos, abrir cualquier archivo, sitios web, búsqueda de Google, y algunos easter eggs.")
    elif ('adios')  in response:
        print('ok, adios.')
        break
    elif ('chao')  in response:
        print('ok, chao.')
        break
    elif ('gracias') in response or ('muchas gracias') in response:
        print('De nada.')
    elif response == ('Jarvis'):
        print('Mande, ¿En que le puedo servir?')
    elif response=='Salir' or response=='salir':
        sys.exit('Saliendo...')
    elif('como estas') in response or ('y tu') in response or ('estas bien') in response:
        print('Estoy bien, gracias')
    elif ('cual es tu nombre') in response:
        print("Mi nombre es Jarvis")
    elif ('que comes') in response:
        print("Como poca Memoria RAM")
    elif ('google search') in response :
        query = response
        stopwords = ['google', 'search']
        querywords = query.split()
        resultwords  = [word for word in querywords if word.lower() not in stopwords]
        result = ' '.join(resultwords)
        Edge = ("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s")
        webbrowser.get(Edge).open('https://www.google.com/search?sourceid=chrome&ie=utf-8&oe=utf-8&aq=t&hl=&q='+result)
    elif ('google maps') in response:
        query = response
        stopwords = ['google', 'maps']
        querywords = query.split()
        resultwords  = [word for word in querywords if word.lower() not in stopwords]
        result = ' '.join(resultwords)
        Edge = ("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s")
        webbrowser.get(Edge).open("https://www.google.be/maps/place/"+result+"/")
    elif response == "tu nombre":
        print(myname)
    elif response == "limpiar":
        clear()
    elif response == "mi nombre":
        print(name)
    elif response == "numero random":
        print (random.randint(1,100))
    elif response == "calculator":
        def add(x, y):
            return x + y
        def subtract(x, y):
            return x - y
        def multiply(x, y):
            return x * y
        def divide(x, y):
            return x / y
        print("Selecciona una operación.")
        print("1.Sumar")
        print("2.Restar")
        print("3.Multiplicar")
        print("4.Dividir")
        choice = input("Elección >>> ")
        num1 = int(input("calculadora (Número 1)>>> "))
        num2 = int(input("calculadora (Número 2)>>> "))
        if choice == '1':
            print(num1,"+",num2,"=", add(num1,num2))
        elif choice == '2':
            print(num1,"-",num2,"=", subtract(num1,num2))
        elif choice == '3':
            print(num1,"*",num2,"=", multiply(num1,num2))
        elif choice == '4':
            print(num1,"/",num2,"=", divide(num1,num2))
        else:
            print("Entrada inválida...")
    elif "hola" in response:
        print ("Holaaaa :3")
    elif response == ("hola "+ myname):
        print("Hola, " + name)
    elif response == ("hola " + myname):
        print ("Hola, " + name)
    elif commands.count (response) == 1:
        spot = commands.index (response)
        print(action[spot])
    elif "info on" in response:
        try:
            response = response[(response.find("info on")+8):len(response)]
            res=client.query(response)
            print(next(res.results).text)
        except:
            print (wikipedia.summary(response, sentences=2))
            print("Más?")
            cont=input("Wikipedia >>> ")
            if "y" in cont and not "no" in cont:
                print (wikipedia.summary(response))
    elif "what is" in response and not commands.count (response) == 1:
        try:
            response = response[(response.find("what is")+8):len(response)]
            res=client.query(response)
            print(next(res.results).text)
        except:
            print (wikipedia.summary(response, sentences=2))
            print("More?")
            cont=input("Wiki>>> ")
            if "y" in cont and not "no" in cont:
                print (wikipedia.summary(response))
    elif "who is" in response:
        response = response[(response.find("who is")+7):len(response)]
        try:
            res=client.query(response)
            print(next(res.results).text)
        except:
            print (wikipedia.summary(response, sentences=2))
            print(response)
            print("More?")
            cont=input("Wiki>>> ")
            if "y" in cont and not "no" in cont:
                print (wikipedia.summary(response))
    elif "who was" in response:
        response = response[(response.find("who was")+8):len(response)]
        try:
            res=client.query(response)
            print(next(res.results).text)
        except:
            print (wikipedia.summary(response, sentences=2))
            print(response)
            print("More?")
            cont=input("Wiki>>> ")
            if "y" in cont and not "no" in cont:
                print (wikipedia.summary(response))
    elif "what are" in response:
        try:
            response = response[(response.find("what are")+9):len(response)]
            res=client.query(response)
            print(next(res.results).text)
        except:
            print (wikipedia.summary(response, sentences=2))
            print("More?")
            cont=input("Wiki>>> ")
            if "y" in cont and not "no" in cont:
                print (wikipedia.summary(response))
    elif "what was" in response:
        try:
            response = response[(response.find("what is")+9):len(response)]
            res=client.query(response)
            print(next(res.results).text)
        except:
            print (wikipedia.summary(response, sentences=2))
            print("More?")
            cont=input("Wiki>>> ")
            if "y" in cont and not "no" in cont:
                print (wikipedia.summary(response))
    elif "information on" in response or 'information about' in response or 'info on' in response or 'info about' in response:
        try:
            response = response[(response.find("information on")+15):len(response)]
            res=client.query(response)
            print(next(res.results).text)
        except:

            print (wikipedia.summary(response, sentences=2))
            print("More?")
            cont=input("Wiki>>> ")
            if "y" in cont and not "no" in cont:
                print (wikipedia.summary(response))
    else:
        command = response
        response = input("No entiendo lo que dices, ¿te gustaría registrar este comando? >>> ")

        if "y" in response and not "no" in response:
            commands.append(command)
            actionk = input("¿Que debería responder? >>> ")
            action.append(actionk)
        else:
            print("ok")












