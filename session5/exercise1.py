mynamelist = ["Jacqueline", "Diana", "Yulima", "Amaira", "Michael", "Edward", "Florence","Magdalena", "Iris"]
pokemon = mynamelist
print(pokemon)

mynamelist.append("Diego")
print(pokemon)

mynamelist.pop(0)
print(pokemon)

mynamelist.remove("Diana")
print(pokemon)

print(mynamelist[3])


#1b
myteam = ["Landorus", "Weedle", "Spearow", "Pidgey", "Gardevoir"]
pokedex = myteam + mynamelist
print(pokedex)

#1d
pokedex.insert(3, "Wild Rattata")
print(pokedex)

#1e
pokedex_len = len(pokedex)
print(pokedex_len)