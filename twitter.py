#!/usr/bin/python3
creditos = ("Daniel Torres", "DTorres", 2017)
tweet = None
likes = 0
retweets = 0
infotweet = {}
print("Bienvenidos a la aplicacion")
usuario = input("Cual es tu usuario? ")
tweet = input("¿Que esta pasando? ")
likes = input("Cuantos likes? ")
retweets = input("Cuantos retweets? ")
infotweet = {"Autor": usuario, "Mensaje": tweet, "Likes": likes, "Retweets": retweets}
print(str(infotweet))