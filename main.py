import sqlite3
import numpy as np
# conn = sqlite3.connect('pokimon.sqlite')
# c = conn.cursor()
# conn.commit()
# # Close Connection
# conn.close()

conn = sqlite3.connect('pokimon.sqlite')


global BattleFinish, phase, P1, P1Level, P1Type, P1AtkSelected, P1TM, P1Extra, P2, P2Level, P2Type, P2AtkSelected, P2TM, P2Extra, P1Bonus, P2Bonus


P1TM = "000"
P2TM = "000"
P1BonusType = 0
P2BonusType = 0
phase = 0


def selectPokemon():
    conn = sqlite3.connect('pokimon.sqlite')
    c = conn.cursor()
    global BattleFinish
    found = False
    while found == False:
        pokedex = input("Select #Pokedex de Pokemon ")
        c.execute("SELECT * FROM pokemons WHERE POKEDEX = (?)", (pokedex,))
        Pokemon = c.fetchone()

        if Pokemon == None:
            print("Pokemon not found , please try again ")

        else:
            found = True
            conn.commit()
            conn.close()
            return Pokemon


def getAttack(Attack):
    conn = sqlite3.connect('pokimon.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM attacks WHERE ATKID = (?)", (Attack,))
    attackfound = c.fetchone()
    if attackfound == None:
        print("Attack Not Found")

    else:
        conn.commit()
        conn.close()
        return attackfound


def attack_Bonus(Attack_type, PkmRival_type):
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


def selectAttack(Pokemon, atk1, atk2, TM, rivalType):
    bonusType1 = 0
    bonusType2 = 0
    bonusTypeTM = 0
    status = "neutro"
    if (TM == "000"):
        # No TM - with ATK2
        if (atk2[0] != "000"):
            print("\n" + Pokemon + " select Attack: ")
            status = attack_Bonus(atk1[2], rivalType)
            if status == "advantage":
                print("1.-" + atk1[1] + ":" + str(atk1[3]) + "-> +2")
                bonusType1 = 2
            elif status == "disadvantge":
                print("1.-" + atk1[1] + ":" + str(atk1[3]) + "-> -2")
                bonusType1 = -2
            elif status == "neutro":
                print("1.-" + atk1[1] + ":" + str(atk1[3]) + "-> 0")
                bonusType1 = 0

            status = attack_Bonus(atk2[2], rivalType)
            if status == "advantage":
                print("2.-" + atk2[1] + ":" + str(atk2[3]) + "-> +2")
                bonusType2 = 2
            if status == "disadvantge":
                print("2.-" + atk2[1] + ":" + str(atk2[3]) + "-> -2")
                bonusType2 = -2
            elif status == "neutro":
                print("2.-" + atk2[1] + ":" + str(atk2[3]) + "-> 0")
                bonusType2 = 0

            i = int(input())
            if i == 1:
                print("Attack " + atk1[1] + " selected")
                return atk1[1], atk1[2], atk1[3], atk1[4], atk1[5], atk1[6], bonusType1

            elif i == 2:
                print("Attack " + atk2[1] + " selected")
                return atk2[1], atk2[2], atk2[3], atk2[4], atk2[5], atk2[6], bonusType2
            else:
                print("Error attack not selected")
        else:
            # No TM and NO Atk2
            print("Attack  selected")
            status = attack_Bonus(atk1[2], rivalType)
            if status == "advantage":
                print("1.-" + atk1[1] + ":" + str(atk1[3]) + "-> +2")
                bonusType1 = 2
            elif status == "disadvantge":
                print("1.-" + atk1[1] + ":" + str(atk1[3]) + "-> -2")
                bonusType1 = -2
            elif status == "neutro":
                print("1.-" + atk1[1] + ":" + str(atk1[3]) + "-> 0")
                bonusType1 = 0
            return atk1[1], atk1[2], atk1[3], atk1[4], atk1[5], atk1[6], bonusType1
    else:
        # With TM and with ATK2
        if (atk2[0] != "000"):
            print("\n" + Pokemon + " select an Attack: ")
            status = attack_Bonus(atk1[2], rivalType)
            if status == "advantage":
                print("1.-" + atk1[1] + ":" + str(atk1[3]) + "-> +2")
                bonusType1 = 2
            elif status == "disadvantge":
                print("1.-" + atk1[1] + ":" + str(atk1[3]) + "-> -2")
                bonusType1 = -2
            elif status == "neutro":
                print("1.-" + atk1[1] + ":" + str(atk1[3]) + "-> 0")
                bonusType1 = 0

            status = attack_Bonus(atk2[2], rivalType)
            if status == "advantage":
                print("2.-" + atk2[1] + ":" + str(atk2[3]) + "-> +2")
                bonusType2 = 2
            if status == "disadvantge":
                print("2.-" + atk2[1] + ":" + str(atk2[3]) + "-> -2")
                bonusType2 = -2
            elif status == "neutro":
                print("2.-" + atk2[1] + ":" + str(atk2[3]) + "-> 0")
                bonusType2 = 0

            status = attack_Bonus(TM[2], rivalType)
            if status == "advantage":
                print("3.-" + TM[1] + ":" + str(TM[3]) + "-> +2")
                bonusTypeTM = 2
            if status == "disadvantge":
                print("3.-" + TM[1] + ":" + str(TM[3]) + "-> -2")
                bonusTypeTM = -2
            elif status == "neutro":
                print("3.-" + TM[1] + ":" + str(TM[3]) + "-> 0")
                bonusTypeTM = 0
            i = int(input())
            if i == 1:
                print("Attack " + atk1[1] + " selected")
                return atk1[1], atk1[2], atk1[3], atk1[4], atk1[5], atk1[6], bonusType1

            elif i == 2:
                print("Attack " + atk2[1] + " selected")
                return atk2[1], atk2[2], atk2[3], atk2[4], atk2[5], atk2[6], bonusType2

            elif i == 3:
                print("Attack " + TM[1] + " selected")
                return TM[1], TM[2], TM[3], TM[4], TM[5], TM[6], bonusTypeTM
            else:
                print("Error attack not selected")
        else:
            print("\n" + Pokemon + "Seelect Attack: ")
            status = attack_Bonus(atk1[2], rivalType)
            if status == "advantage":
                print("1.-" + atk1[1] + ":" + str(atk1[3]) + "-> +2")
                bonusType1 = 2
            elif status == "disadvantge":
                print("1.-" + atk1[1] + ":" + str(atk1[3]) + "-> -2")
                bonusType1 = -2
            elif status == "neutro":
                print("1.-" + atk1[1] + ":" + str(atk1[3]) + "-> 0")
                bonusType1 = 0

            status = attack_Bonus(TM[2], rivalType)
            if status == "advantage":
                print("3.-" + TM[1] + ":" + str(TM[3]) + "-> +2")
                bonusTypeTM = 2
            if status == "disadvantge":
                print("3.-" + TM[1] + ":" + str(TM[3]) + "-> -2")
                bonusTypeTM = -2
            elif status == "neutro":
                print("3.-" + TM[1] + ":" + str(TM[3]) + "-> 0")
                bonusTypeTM = 0
            i = int(input())
            if i == 1:
                print("Attack " + atk1[1] + " selected")
                return atk1[1], atk1[2], atk1[3], atk1[4], atk1[5], atk1[6], bonusType1

            elif i == 3:
                print("Attack " + TM[1] + " selected")
                return TM[1], TM[2], TM[3], TM[4], TM[5], TM[6], bonusTypeTM
            else:
                print("Error attack not selected")


def statusEffect(effect):
    attacker = "Normal"
    defender = "Normal"
    if effect == "Advantage":
        attacker = "Advantage"
        return attacker, defender
    elif effect == "Burn":
        defender = "Burned"
        return attacker, defender
    elif effect == "Confusion":
        defender = "Confused"
        return attacker, defender
    elif effect == "Disadvantage":
        defender = "Disadvantage"
        return attacker, defender
    elif effect == "DoubleDice":
        attacker = "DoubleDice"
        return attacker, defender
    elif effect == "Faint":
        attacker = "Killed"
        return attacker, defender
    elif effect == "Frozen":
        defender = "Frozen"
        return attacker, defender
    elif effect == "Kill":
        defender = "Killed"
        return attacker, defender
    elif effect == "Once":
        attacker = "Once"
        return attacker, defender
    elif effect == "OwnConfusion":
        attacker = "Confused"
        return attacker, defender
    elif effect == "Paralize":
        defender = "Paralized"
        return attacker, defender
    elif effect == "Poison":
        defender = "Poisoned"
        return attacker, defender
    elif effect == "QuickAttack":
        attacker = "Quick"
        return attacker, defender
    elif effect == "Sleep":
        defender = "Sleep"
        return attacker, defender
    else:
        print("effect no found ")


def activateEffect(pokemon, effect, activate):

    if effect != "NONE":
        if activate != "Automatic":
            i = int(input("\n" + pokemon + ":  effect Activated ?"))
            if i == 1:
                print("Effect Activated!!!!")
                status = statusEffect(effect)
                print("status:")
                print(status)
                return status

            if i == 2:
                print("Effect NO activated!!!! ")
        else:
            print("Effect Activated Automatically!!!!")
            status = statusEffect(effect)
            return status

    else:
        print("Attack with no Effect")


def checkStatusP2(pokemon, status):
    if status == "Frozen":
        print(pokemon + " is Frozen, need 4 to use attack:")
        i = int(input("/n Roll D4 Dice ?"))
        if i == 4:
            print("Status Removed")
            status = "Normal"
            return status
        else:
            print("Status not Removed ")
            return status
    if status == "Paralized":
        print(pokemon + " is Parallized, need 1 to use attack:")
        i = int(input("/n Roll D4 Dice ?"))
        if i == 1:
            print("Status Removed")
            status = "Normal"
            return status
        else:
            print("Status not Removed ")
            return status
    if status == "Sleep":
        print(pokemon + " is Sleeping, Unable to use attack:")
        return status


BattleFinish = False
if __name__ == '__main__':

    while (BattleFinish != True):
        # P1 select Pokemon
        if phase == 0:
            print("\n Phase 0: ->")
            print("P1 Select")
            pokemon = selectPokemon()
            P1 = pokemon[2]
            P1Level = pokemon[3]
            P1Type = pokemon[4]
            P1Atk1 = getAttack(pokemon[5])
            P1Atk2 = getAttack(pokemon[6])
            print("Pokemon Selected: " + P1)
            phase = 1
        # P2 select Pokemon
        elif phase == 1:
            print("\n Phase 1: ->")
            print("P2 Select")
            pokemon = selectPokemon()
            P2 = pokemon[2]
            P2Level = pokemon[3]
            P2Type = pokemon[4]
            P2Atk1 = getAttack(pokemon[5])
            P2Atk2 = getAttack(pokemon[6])
            print("Pokemon Selected: " + P2)
            phase = 2
        # P1 select Attack
        elif phase == 2:
            print("\n Phase 2: ->")
            tuplaAttack = selectAttack(
                P1, P1Atk1, P1Atk2, P1TM, P2Type)
            P1AtkSelected = tuplaAttack[0]
            P1AtkType = tuplaAttack[1]
            P1AtkPower = tuplaAttack[2]
            P1AtkEffect = tuplaAttack[3]
            P1AtkActivate = tuplaAttack[4]
            P1AtkDice = tuplaAttack[5]
            P1BonusType = tuplaAttack[6]
            phase = 3
        # P2 select attack
        elif phase == 3:
            print("\n Phase 3: ->")
            tuplaAttack = selectAttack(
                P2, P2Atk1, P2Atk2, P2TM, P1Type)
            P2AtkSelected = tuplaAttack[0]
            P2AtkType = tuplaAttack[1]
            P2AtkPower = tuplaAttack[2]
            P2AtkEffect = tuplaAttack[3]
            P2AtkActivate = tuplaAttack[4]
            P2AtkDice = tuplaAttack[5]
            P2BonusType = tuplaAttack[6]
            phase = 4
        # P1 effect
        elif phase == 4:
            print("\n Phase 4: ->")
            tupleEffect = activateEffect(P1, P1AtkEffect, P1AtkActivate)
            print("TuplaEffect:")
            print(tupleEffect)
            P1status = tupleEffect[0]
            P2status = tupleEffect[1]
            print("P1Status:" + P1status)
            print("P2Status:" + P2status)

            phase = 5
        elif phase == 5:
            print("\n Phase 5: ->")
            P2status = checkStatusP2(P2, P2status)
            if P2status == "Frozen" or P2status == "Sleep" or P2status == "Paralized":
                P2AtkPower = 0
                P2BonusType = 0
                phase = 6
            else:
                tupleEffect = activateEffect(P2, P2AtkEffect, P2AtkActivate)
                print("TuplaEffect:")
                print(tupleEffect)
                P1status = tupleEffect[1]
                P2status = tupleEffect[0]
                print("P1Status:" + P1status)
                print("P2Status:" + P2status)
                phase = 6

        elif phase == 6:
            print("\n Phase 6: ->")
            P1status = checkStatusP2(P1, P1status)
            if P1status == "Frozen" or P1status == "Sleep" or P1status == "Paralized":
                P1AtkPower = 0
                P1BonusType = 0
                phase = 7
            else:
                phase = 7
        elif phase == 7:
            pass
