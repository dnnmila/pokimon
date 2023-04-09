import sqlite3
import GloVar
import BTFun


class Trainner ():
    def __init__(self, name):
        self.name = name
        self.Pokemons = []

    def addPokemon(self):
        conn = sqlite3.connect('pokimon.sqlite')
        c = conn.cursor()
        found = False
        while found == False:
            pokedexN = input("Pokemon  from " + self.name + "? ")
            c.execute("SELECT * FROM pokemons WHERE ID = (?)", (pokedexN,))
            pokemon = c.fetchone()
            if pokemon == None:
                print("Pokemon not found , please try again ")

            else:
                found = True
                conn.commit()
                conn.close()
                newPokemon = Pokemon(pokemon[0], pokemon[1], pokemon[2], pokemon[4],
                                     pokemon[5], pokemon[6], pokemon[3], pokemon[7], pokemon[9])
                self.Pokemons.append(newPokemon)

        self.showPokemons()

    def showPokemons(self):
        index = 1
        print("\n Trainner:" + self.name)
        for p in self.Pokemons:
            print(str(index) + "." + p.name + "-> Level:"+str(p.level) +
                  " -> Status:" + p.status + "-> Alive:" + str(p.isAlive))
            index = index+1

    def removePokemon(self):
        self.showPokemons()
        i = int(input("Select pokemon to remove"))
        del self.Pokemons[i-1]
        self.showPokemons()

    def addLevel(self):
        self.showPokemons()
        i = int(input("Select pokemon to add Level"))
        self.Pokemons[i-1].addLevel()
        print("New Level :" + str(self.Pokemons[i-1].level))
        self.showPokemons()


trainners = []


class Pokemon():
    def __init__(self, id, pokedex, name, type, attack1, attack2, level, tm, attach):
        self.id = id
        self.pokedex = pokedex
        self.name = name
        self.type = type
        self.attack1 = attack1
        self.attack2 = attack2
        self.level = level
        self.tm = tm
        self.attach = attach
        self.status = ""
        self.isAlive = True

    def getPokemon(self):
        return self.name

    def addLevel(self):
        self.level = self.level + 1

    def addTM(self, TM):
        self.tm = TM

    def addAttach(self, Attach):
        self.attach = Attach


class Game ():
    def __init__(self, round, turn, players):
        self.round = round
        self.turn = turn
        self.players = players

    def nextTurn(self):
        self.turn = self.turn + 1
        if self.turn > self.players:
            self.turn = 1
            self.round = self.round + 1

    def showRound(self):
        print("Round" + str(self.round))
        print("Turn" + str(self.turn))


def showMenu(turn):
    print("\nRound : " + str(game.round) +
          " -> Turn :" + trainners[turn-1].name)
    print("-----------------------")
    print("MAIN MENU")
    print("1.show Pokemons ")
    print("2.Battle Trainner")
    print("3.Battle Gym")
    print("4.Wild Pokemon")
    print("5.End turn ")
    print("6.Trainers")
    option = int(input("select Option?"))
    if option == 1:
        trainnerMenu(trainners[turn-1])
    elif option == 2:
        print("Lets Fight")
    elif option == 3:
        print("Gym Battle")
    elif option == 4:
        print("Wild Pokemon")
    elif option == 5:
        game.nextTurn()
        showMenu(game.turn)
    elif option == 6:
        index = 1
        for t in trainners:
            print("P" + str(index) + "." + t.name)
            index = index+1
        option = int(input("select Trainner?"))
        trainnerMenu(trainners[option-1])
    else:
        print("No option found")
        showMenu(turn)


def trainnerMenu(Trainner):
    print("\n-----" + Trainner.name + "-----")
    print("1.Show Pokemons")
    print("2.Add Pokemon")
    print("3.Remove Pokemon")
    print("4.Add Level to Pokemon")
    print("5.Return to Main Menu")

    option = int(input("select Option?"))
    if option == 1:
        Trainner.showPokemons()
        option = int(input("Return to trainner Menu? "))
        if option == 1:
            trainnerMenu(Trainner)
    elif option == 2:
        Trainner.addPokemon()
        trainnerMenu(Trainner)
    elif option == 3:
        Trainner.removePokemon()
        trainnerMenu(Trainner)
    elif option == 4:
        Trainner.addLevel()
        trainnerMenu(Trainner)
    elif option == 5:
        showMenu(game.turn)
    else:
        print("No option found")
        trainnerMenu(Trainner)


if __name__ == '__main__':
    i = int(input("Press 1 to Start"))
    if i == 1:
        print("Starting .....")
        i = int(input("How many Players?"))
        for p in range(i):
            player = input("Name of player " + str(p+1) + "? ")
            trainner = Trainner(player)
            trainners.append(trainner)
        for t in trainners:
            t.addPokemon()
        game = Game(1, 1, i)
        game.showRound()
        showMenu(game.turn)
