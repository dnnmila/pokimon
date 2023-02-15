class Pokemon:
    def __init__(self, UID, pokedex, name, level, type1, type2, attack1, atk1Type, atk1Power, atk1Effect, atk1Dice, attack2, atk2Type, atk2Power, atk2Effect, atk2Dice, TmName, TmType, TmPower, TmEffect, TmDice):
        self.UID = UID
        self.pokedex = pokedex
        self.name = name
        self.level = level
        self.type1 = type1
        self.type2 = type2
        self.attack1 = attack1
        self.atk1Type = atk1Type
        self.atk1Power = atk1Power
        self.atk1Effect = atk1Effect
        self.atk1Dice = atk1Dice
        self.attack2 = attack2
        self.atk2Type = atk2Type
        self.atk2Power = atk2Power
        self.atk2Effect = atk2Effect
        self.atk2Dice = atk2Dice
        self.TmName = TmName
        self.TmType = TmType
        self.TmPower = TmPower
        self.TmEffect = TmEffect
        self.TmDice = TmDice


class Attack:
    def __init__(self, UID, name, power, type, effect, efecto, dice):
        self.UID = UID
        self.name = name
        self.power = power
        self.type = type
        self.effect = effect
        self.efecto = efecto
        self.dice = dice


class Item:
    def __init__(self, UID, name, type, TM_name, TM_level, TM_type,):
        self.UID = UID
        self.name = name
        self.type = type
        self.TM_name = TM_name
        self.TM_level = TM_level
        self.TM_type = TM_type


def printPokemons(Pokemons):
    for pokemon in Pokemons:
        print(pokemon.name)
        index = 0
        for index, attack in enumerate(pokemon.attacks, start=1):
            print(index, attack.name)


def selectPokemon(Pokemons):
    found = False
    while found == False:
        pokedex = input("Select #Pokedex de Pokemon ")
        for pokemon in Pokemons:
            if str(pokemon.pokedex) == str(pokedex):
                found = True
                return pokemon
                break
        if found == False:
            print("Pokemon not found , please try again ")


def addItem(item):
    print("0. TM1_Earthquake")
    print("1. Protect")
    i = int(input('Select Item: '))
    return item[i]


def selectAttack(Pokemon):
    i = int(input('Select Attack: '))


# Funcion para verificar ventaja o desventaja de ataque


def attack_VoD(Attack_type, PkmRival_type):
    if (Attack_type == "NORMAL") and (PkmRival_type == "STEAL" or PkmRival_type == "GHOST" or PkmRival_type == "ROCK"):
        status = "disadvantge"
        return status

    if (Attack_type == "GRASS"):
        if (PkmRival_type == "GROUND" or PkmRival_type == "WATER" or PkmRival_type == "ROCK"):
            status = "advantage"
            return status
        if (PkmRival_type == "POISON" or PkmRival_type == "BUG" or PkmRival_type == "GRASS" or PkmRival_type == "FIRE" or PkmRival_type == "DRAGON" or PkmRival_type == "FLY" or PkmRival_type == "STEAL"):
            status = "disadvantge"
            return status

    if (Attack_type == "FIRE"):
        if (PkmRival_type == "ICE" or PkmRival_type == "GRASS" or PkmRival_type == "BUG" or PkmRival_type == "STEAL"):
            status = "advantage"
            return status
        if (PkmRival_type == "ROCK" or PkmRival_type == "FIRE" or PkmRival_type == "WATER" or PkmRival_type == "DRAGON"):
            status = "disadvantge"
            return status

    if (Attack_type == "WATER"):
        if (PkmRival_type == "GROUND" or PkmRival_type == "ROCK" or PkmRival_type == "FIRE"):
            status = "advantage"
            return status
        if (PkmRival_type == "WATER" or PkmRival_type == "GRASS" or PkmRival_type == "DRAGON"):
            status = "disadvantge"
            return status

    if (Attack_type == "FIGHTING"):
        if (PkmRival_type == "NORMAL" or PkmRival_type == "ROCK" or PkmRival_type == "ICE" or PkmRival_type == "DARK" or PkmRival_type == "STEAL"):
            status = "advantage"
            return status
        if (PkmRival_type == "FLYING" or PkmRival_type == "POISON" or PkmRival_type == "BUG" or PkmRival_type == "PSYCHIC" or PkmRival_type == "GHOST" or PkmRival_type == "FAIRY"):
            status = "disadvantge"
            return status

    if (Attack_type == "FLYING"):
        if (PkmRival_type == "FIGHTING" or PkmRival_type == "BUG" or PkmRival_type == "GRASS"):
            status = "advantage"
            return status
        if (PkmRival_type == "ELECTRIC" or PkmRival_type == "ROCK" or PkmRival_type == "STEAL"):
            status = "disadvantge"
            return status

    if (Attack_type == "POISON"):
        if (PkmRival_type == "GRASS" or PkmRival_type == "FAIRY"):
            status = "advantage"
            return status
        if (PkmRival_type == "POISON" or PkmRival_type == "GROUND" or PkmRival_type == "ROCK" or PkmRival_type == "GHOST" or PkmRival_type == "STEAL"):
            status = "disadvantge"
            return status

    if (Attack_type == "GROUND"):
        if (PkmRival_type == "POISON" or PkmRival_type == "ROCK" or PkmRival_type == "FIRE" or PkmRival_type == "ELECTRIC" or PkmRival_type == "STEAL"):
            status = "advantage"
            return status
        if (PkmRival_type == "FLYING" or PkmRival_type == "BUG" or PkmRival_type == "GRASS"):
            status = "disadvantge"
            return status

    if (Attack_type == "ROCK"):
        if (PkmRival_type == "FLYING" or PkmRival_type == "BUG" or PkmRival_type == "FIRE" or PkmRival_type == "ICE"):
            status = "advantage"
            return status
        if (PkmRival_type == "FIGHTING" or PkmRival_type == "GROUND" or PkmRival_type == "STEAL"):
            status = "disadvantge"
            return status

    if (Attack_type == "BUG"):
        if (PkmRival_type == "GRASS" or PkmRival_type == "PSYCHIC" or PkmRival_type == "DARK"):
            status = "advantage"
            return status
        if (PkmRival_type == "FIGHTING" or PkmRival_type == "FLYING" or PkmRival_type == "GHOST" or PkmRival_type == "STEAL" or PkmRival_type == "POISON" or PkmRival_type == "FIRE" or PkmRival_type == "FAIRY"):
            status = "disadvantge"
            return status

    if (Attack_type == "GHOST"):
        if (PkmRival_type == "GHOST" or PkmRival_type == "PSYCHIC"):
            status = "advantage"
            return status
        if (PkmRival_type == "NORMAL" or PkmRival_type == "DARK"):
            status = "disadvantge"
            return status

    if (Attack_type == "ELECTRIC"):
        if (PkmRival_type == "FLYING" or PkmRival_type == "WATER"):
            status = "advantage"
            return status
        if (PkmRival_type == "GROUND" or PkmRival_type == "GRASS" or PkmRival_type == "ELECTRIC" or PkmRival_type == "DRAGON"):
            status = "disadvantge"
            return status

    if (Attack_type == "PSYCHIC"):
        if (PkmRival_type == "FIGHTING" or PkmRival_type == "POISON"):
            status = "advantage"
            return status
        if (PkmRival_type == "PSYCHIC" or PkmRival_type == "STEAL" or PkmRival_type == "DARK"):
            status = "disadvantge"
            return status

    if (Attack_type == "ICE"):
        if (PkmRival_type == "FLYING" or PkmRival_type == "GROUND" or PkmRival_type == "GRASS" or PkmRival_type == "DRAGON"):
            status = "advantage"
            return status
        if (PkmRival_type == "FIRE" or PkmRival_type == "WATER" or PkmRival_type == "ICE" or PkmRival_type == "STEAL"):
            status = "disadvantge"
            return status

    if (Attack_type == "DRAGON"):
        if (PkmRival_type == "DRAGON"):
            status = "advantage"
            return status
        if (PkmRival_type == "STEAL" or PkmRival_type == "FAIRY"):
            status = "disadvantge"
            return status

    if (Attack_type == "DARK"):
        if (PkmRival_type == "GHOST" or PkmRival_type == "PSYCHIC"):
            status = "advantage"
            return status
        if (PkmRival_type == "FIGHTING" or PkmRival_type == "DARK" or PkmRival_type == "FAIRY"):
            status = "disadvantge"
            return status

    if (Attack_type == "STEAL"):
        if (PkmRival_type == "ROCK" or PkmRival_type == "ICE" or PkmRival_type == "FAIRY"):
            status = "advantage"
            return status
        if (PkmRival_type == "FIRE" or PkmRival_type == "WATER" or PkmRival_type == "ELECTRIC" or PkmRival_type == "STEAL"):
            status = "disadvantge"
            return status

    if (Attack_type == "FAIRY"):
        if (PkmRival_type == "FIGHTING" or PkmRival_type == "DRAGON" or PkmRival_type == "DARK"):
            status = "advantage"
            return status
        if (PkmRival_type == "FIRE" or PkmRival_type == "POSION" or PkmRival_type == "STEAL"):
            status = "disadvantge"
            return status

    else:
        status = "neutro"
        return status
