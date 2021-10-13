# 1 - créer une liste des pokémons, incluant une chance de spawn (0% - 100%) 
# 2 - créer une méthode spwan, qui, en fonction de la chance de spawn, fait spawn un pokémon (affiche son nom)
# 3 - faire spawn 10000 pokémons, calculer le % de chaque pokémon spawn
# 4 - comparer le % de spawn avec la chance de spawn du pokémon. Afficher pour chaque pokémon spawn,
# s'il y en a eu + ou - que la proba de spawn initiale

# 5 - Créer les pokeball (30%), superball (50%), hyperball (70%), masterball (100%). Mettre un % de chance d'attraper le pokemon pour chacune.

# 6 - Ajouter une "résistance" à chaque pokemon, entre 0 et 50%. La résistance est la diminution de la proba d'attraper les pokémons.
# Attention, la masterball de ne prend pas en compte la resistance.

# 7 - Mettre en place un inventaire des objets obtenus :
#       -> 1 inventaire pokemon
#       -> 1 inventaire pokeballs

# 8 - Ajouter des stats par pokémon (attaque / défense)
# 9 - Mettre en place les combats (pokemon_1 vs pokemon_2) :
#       - ratio1 = attaque_pokemon_1 / defense_pokemon_1
#       - ratio2 = attaque_pokemon_2 / defense_pokemon_2
#       - gagnant = random de 0 à somme(ratio1, ratio2). (meme principe que % spawn)

# 10 - Mettre en place les pokedollars ($). Chaque combat gagné rapporte entre 1 et 2000 pokedollars

# 11 - Ajouter un shop, avec les prix suivants : 
#       -> pokeball : 200$
#       -> superball : 600$
#       -> hyperball : 1 200$
#       -> masterball : 50 000$

# 12 - Mettre en place le tout dans un programme en CLI, avec un menu : 
#       -> shop
#       -> spawn (entraine capture OU combat (combat entraine le choix d'un de vos pokémon qui va combattre) )
#       -> inventaire objets
#       -> inventaire pokemon 


import random, string, time, pypokedex

class Pokemon():
    max = 0

    def __init__(self, id):
        self.timeStart = time.time_ns()           
        self.pokemon = pypokedex.get(dex = id)
        self.spawnrate = random.randint(0,100)
        self.startSpawn = self.__class__.max
        self.__class__.max += self.spawnrate
        self.endSpawn = self.__class__.max

    def __repr__(self):
        return self.pokemon.name
    

if __name__ == "__main__" :
    sum = 0
    test = {}
    result = {}
    for i in range (1, 10):
        test[i] = Pokemon(i)
        print(test[i].pokemon.name)
        sum += test[i].spawnrate
        result[test[i].pokemon.name] = 0
    
    for i in test:
         print("le pokémon : ", test[i].pokemon.name, "  a une chance de spawn de : ", "{:.2f}".format(test[i].spawnrate/(test[i].max/100)), "%")

    for i in range(10000):
        spawn = random.randint(1, test[1].max)
        for i in test:
            if spawn >= test[i].startSpawn and spawn < test[i].endSpawn:
                # print("le pokemon est spawn: ", test[i].pokemon.name, "   et son taux de spawn est:  ", test[i].spawnrate, "%")
                result[test[i].pokemon.name] += 1
                break
    
    for i in result:
        print("pokémon: ", i, "  quantité:  ", result[i], "pourcentage: ", "{:.2f}".format(result[i]/100))

Pokeball =[
 
    {
        "name" : "Pokeball",
        "percent" : 30,
        "total" : 80

    },
     {
        "name" : "Superball",
        "percent" : 50,
        "total" : 50
    },
     {
        "name" : "Hyperball",
        "percent" : 70,
        "total" : 30
    },
    {   "name" : "Masterball",
        "percent" : 100,
        "total" : 1
    },
    {
        "name" : "PokeDollars",
        "total" : 5000
    }
]


def lePokemonSpawn(name): 
    print("****************************************")
    print("                                        ")
    print("    Un ",name," sauvage est apparu !    ")
    print("                                        ")
    print("    1- Capturer  2- Fuir  3- Attaquer   ")
    print("                                        ")
    print("****************************************")

    while True:
            input1 = int(input())
            if  input1 == 1:
                capture(name)
                break
            elif input1 == 2:
                print("***********************************")
                print("                                  -")
                print("     Vous avez pris la fuite !    -")
                print("                                  -")
                print("***********************************")
                break

def capture(name):
      
        print("***********************************")
        print("-                                 -")
        print("-   1- Pokeball    2- Superball   -")
        print("-                                 -")
        print("-   3- Hyperball   4- Masterball  -")
        print("-                                 -")
        print("***********************************")

        while True:
            input3 = int(input())
            poke = Pokemon(1)
            a = random.randint(1, 100)
            if input3 == 4:
                Pokeball[input3-1]["total"]-=1
                print(Pokeball)
                print("***********************************")
                print("-                                 -")
                print("-    Vous avez capturé",name,"!   -")
                print("-                                 -")
                print("***********************************")
                break
            if (Pokeball[input3-1]['percent']/(1+(poke.resistancerate/100))) >= a:
                Pokeball[input3-1]["total"]-=1
                print(Pokeball)
                print("***********************************")
                print("-                                 -")
                print("-    Vous avez capturé",name,"!   -")
                print("-                                 -")
                print("***********************************")
                break
            else:
                print("Raté ! ")
                Pokeball[input3-1]["total"]-=1
                print(Pokeball)
                capture(name)
            
            
class Pokemon():
    max = 0

    def __init__(self, id):
        self.timeStart = time.time_ns()           
        self.pokemon = pypokedex.get(dex = id)
        self.spawnrate = random.randint(0,100)
        self.resistancerate = random.randint(0,50)
        self.startSpawn = self.__class__.max
        self.__class__.max += self.spawnrate
        self.endSpawn = self.__class__.max

    def __repr__(self):
        return self.pokemon.name


if __name__ == "__main__" :
    sum = 0
    test = {}
    result = {}
    for i in range (1, 10):
        test[i] = Pokemon(i)
        print(test[i].pokemon.name)
        sum += test[i].spawnrate
        result[test[i].pokemon.name] = 0
    
    for i in test:
         print("le pokémon : ", test[i].pokemon.name, "  a une chance de spawn de : ", "{:.2f}".format(test[i].spawnrate/(test[i].max/10)), "%")

    for i in range(1):
        spawn = random.randint(1, test[1].max)
        for i in test:
            if spawn >= test[i].startSpawn and spawn < test[i].endSpawn:
                # print("le pokemon est spawn: ", test[i].pokemon.name, "   et son taux de spawn est:  ", test[i].spawnrate, "%")
                result[test[i].pokemon.name] += 1
                break
        for i in result:
            if result[i] != 0:
                #print("pokémon: ", i, "  quantité:  ", result[i], "pourcentage: ", "{:.2f}".format(result[i]/100))
                lePokemonSpawn(i)


