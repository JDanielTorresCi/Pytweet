#!/usr/bin/python3
creditos = ("Daniel Torres", "DTorres", 2017)
tweet = None
likes = 0
retweets = 0
infotweet = {}
print("Bienvenidos a la aplicacion")
usuario = input("Cual es tu usuario? ")
tweet = input("¿Que esta pasando? ")
likes = int(input("Cuantos likes? "))
retweets = int(input("Cuantos retweets? "))
infotweet = {"Autor": usuario, "Mensaje": tweet, "Likes": likes, "Retweets": retweets}
print(str(infotweet))
if likes > 2:
	print("Su tweet tiene 'me gustas'")
elif likes == 1:
   	print("Su tweet solo tiene un me gusta")
elif likes == 2:
    print("Su tweet solo tienes dos me gustas")
else:
	print("Su tweet no tiene me gustas")
if(retweets > 0): print("Su tweet tiene retweets")