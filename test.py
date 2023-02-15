import json
from mainFunctions import *

Pokemons = []
file = open("pokedata.json", "r")
datajson = file.read()
file.close()
pokemons = json.loads(datajson)
for pkm in pokemons:
    aux = Pokemon(pkm['UID'], pkm['ID'], pkm['NAME'], pkm['LEVEL'],
                  pkm['TYPE1'], pkm['TYPE2'], pkm['ATK1'], pkm['Atk1Type'], pkm['Atk1Power'], pkm['Atk1Effect'], pkm['Atk1Dice'], pkm['ATK2'], pkm['Atk2Type'], pkm['Atk2Power'], pkm['Atk2Effect'], pkm['Atk2Dice'], pkm['TmName'], pkm['TmType'], pkm['TmPower'], pkm['TmEffect'], pkm['TmDice'])
    Pokemons.append(aux)

status = "neutro"
modo = 0
VoD1 = 0
VoD2 = 0

# MAIN fUCTION
if __name__ == '__main__':

    if modo == 0:

        # printPokemons(Pokemons)

        modo = 1
    if modo == 1:
        print("P1 Select")
        Attacker = selectPokemon(Pokemons)
        print("Pokemon Selected :" + Attacker.name)
        modo = 2

    if modo == 2:
        print("\nP2 Select ")
        Defender = selectPokemon(Pokemons)
        print("Pokemon Selected :" + Defender.name)
        modo = 3

    if modo == 3:
        VoD1 = 0
        VoD2 = 0
        print("\nP1 " + Attacker.name + " Select an Attack:")
        status = attack_VoD(Attacker.atk1Type, Defender.type1)
        print("1.-" + Attacker.attack1 + "->" + status)
        if status == "advantage":
            VoD1 = 2
        if status == "disadvantge":
            VoD1 = -2

        status = attack_VoD(Attacker.atk2Type, Defender.type1)
        print("2.-" + Attacker.attack2 + "->" + status)
        if status == "advantage":
            VoD2 = 2
        if status == "disadvantge":
            VoD2 = -2

        i = int(input('Select Attack: '))
        if i == 1:
            P1attackSelected = Attacker.attack1
            P1AttackPower = Attacker.atk1Power
            P1AttackEffect = Attacker.atk1Effect
            P1VoD = VoD1
            print("Attack Selected " + P1attackSelected)
            modo = 4
        if i == 2:
            P1attackSelected = Attacker.attack2
            P1AttackPower = Attacker.atk2Power
            P1AttackEffect = Attacker.atk2Effect
            P1VoD = VoD2
            print("Attack Selected " + P1attackSelected)
            modo = 4

    if modo == 4:
        VoD1 = 0
        VoD2 = 0
        print("\nP2 " + Defender.name + " Select an Attack:")
        status = attack_VoD(Defender.atk1Type, Attacker.type1)
        print("1.-" + Defender.attack1 + "->" + status)
        if status == "advantage":
            VoD1 = 2
        if status == "disadvantge":
            VoD1 = -2

        status = attack_VoD(Defender.atk2Type, Attacker.type1)
        print("2.-" + Defender.attack2 + "->" + status)
        if status == "advantage":
            VoD2 = 2
        if status == "disadvantge":
            VoD2 = -2

        i = int(input('Select Attack: '))
        if i == 1:
            P2attackSelected = Defender.attack1
            P2AttackPower = Defender.atk1Power
            P2AttackEffect = Defender.atk1Effect
            P2VoD = VoD1
            print("P2.- Attack Selected " + P2attackSelected)
            modo = 5
        if i == 2:
            P2attackSelected = Defender .attack2
            P2AttackPower = Defender.atk2Power
            P2AttackEffect = Defender.atk2Effect
            P2VoD = VoD2
            print("P2.- Attack Selected " + P2attackSelected)
            modo = 5

    if modo == 5:
        if (P1AttackEffect != "NONE"):
            print("P1 effect is active? ")
            print(P1attackSelected)
            print(P1AttackEffect)
            i = int(input('1.Yes  /  2.-NO '))
            if i == 1:
                print("Activating effect")
                modo = 6
            if i == 2:
                print("No Effect activated")
                modo = 6
        else:
            modo = 6

    if modo == 6:
        if (P2AttackEffect != "NONE"):
            print("P2 effect is active? ")
            print(P2attackSelected)
            print(P2AttackEffect)
            i = int(input('1.Yes  /  2.-NO '))
            if i == 1:
                print("Activating effect")
                modo = 7
            if i == 2:
                print("No Effect activated")
                modo = 7
        else:
            modo = 7

    if modo == 7:
        print(Attacker.name + " Total Parcial:")
        print("Level:" + str(Attacker.level) + "+ Attack : " +
              str(P1AttackPower) + " + Ventaja/Desventaja : " + str(P1VoD))
        P1total = Attacker.level + P1AttackPower + P1VoD
        print("Total " + str(P1total))

        print(Defender.name + " Total Parcial:")
        print("Level:" + str(Defender.level) + "+ Attack : " +
              str(P2AttackPower) + " + Ventaja/Desventaja : " + str(P2VoD))
        P2total = Defender.level + P2AttackPower + P2VoD
        print("Total " + str(P2total))

        modo = 8

    if modo == 8:
        print("Total Dado Player 1")
        i = int(input('1-6 '))
        P1Dice = i
        P1total = P1total + P1Dice
        print("Total =" + str(P1total))
        modo = 9

    if modo == 9:
        print("Total Dado Player 2")
        i = int(input('1-6 '))
        P2Dice = i
        P2total = P2total + P2Dice
        print("Total =" + str(P2total))
        modo = 10

    if modo == 10:
        print("P1 active any card")
        i = int(input('1.Yes  /  2.-NO '))
        if i == 1:
            print("Activating Card")
            modo = 11
        if i == 2:
            print("No Card")
            modo = 11

    if modo == 11:
        print("2 active any card")
        i = int(input('1.Yes  /  2.-NO '))
        if i == 1:
            print("Activating Card")
            modo = 12
        if i == 2:
            print("No Card")
            modo = 12
    if modo == 12:
        if (P1total > P2total):
            print("Wiiner is P1 " + Attacker.name)
            print(Attacker.name + ":" + str(P1total))
            print(Defender.name + ":" + str(P2total))
        if (P1total < P2total):
            print("Wiiner is P2 " + Attacker.name)
            print(Attacker.name + ":" + str(P1total))
            print(Defender.name + ":" + str(P2total))
        if (P1total == P2total):
            print("DRAW ")
            print(Attacker.name + ":" + str(P1total))
            print(Defender.name + ":" + str(P2total))
            mode = 3
