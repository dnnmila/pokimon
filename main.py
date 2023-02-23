import sqlite3

global P1, P1Level, P1Type, P1Atk1, P1Atk2, P1TM, P1Extra, P1Attatch, P2, P2Level, P2Type, P2Atk1, P2Atk2, P2TM, P2Extra, P2Attatch
global BattleFinish, Turn, Round
global P1AtkSelID, P1AtkSelected, P1AtkType, P1AtkPower, P1Effect, P1EffectActivate, P1DiceType, P1BonusType
global P2AtkSelID, P2AtkSelected, P2AtkType, P2AtkPower, P2Effect, P2EffectActivate, P2DiceType, P2BonusType


def selectPokemon(player):
    global P1, P1Level, P1Type, P1Atk1, P1Atk2, P1TM, P1Extra, P1Attatch, P2, P2Level, P2Type, P2Atk1, P2Atk2, P2TM, P2Extra, P2Attatch
    conn = sqlite3.connect('pokimon.sqlite')
    c = conn.cursor()
    found = False
    while found == False:
        pokedex = input("Select #Pokedex de Pokemon ")
        c.execute("SELECT * FROM pokemons WHERE ID = (?)", (pokedex,))
        pokemon = c.fetchone()

        if pokemon == None:
            print("Pokemon not found , please try again ")

        else:
            found = True
            conn.commit()
            conn.close()
            if player == "P1":
                P1 = pokemon[2]
                P1Level = pokemon[3]
                P1Type = pokemon[4]
                P1Atk1 = getAttack(pokemon[5])
                P1Atk2 = getAttack(pokemon[6])
                P1TM = pokemon[7]
                P1Extra = pokemon[8]
                P1Attatch = pokemon[9]
            elif player == "P2":
                P2 = pokemon[2]
                P2Level = pokemon[3]
                P2Type = pokemon[4]
                P2Atk1 = getAttack(pokemon[5])
                P2Atk2 = getAttack(pokemon[6])
                P2TM = pokemon[7]
                P2Extra = pokemon[8]
                P2Attatch = pokemon[9]


def getAttack(Attack):
    conn = sqlite3.connect('pokimon.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM attacks WHERE ID = (?)", (Attack,))
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


def passAttack(Player, atk, bonusType):
    global P1AtkSelID, P1AtkSelected, P1AtkType, P1AtkPower, P1Effect, P1EffectActivate, P1DiceType, P1BonusType
    global P2AtkSelID, P2AtkSelected, P2AtkType, P2AtkPower, P2Effect, P2EffectActivate, P2DiceType, P2BonusType
    if Player == "P1":
        P1AtkSelID = atk[0]
        P1AtkSelected = atk[1]
        P1AtkType = atk[2]
        P1AtkPower = atk[3]
        P1Effect = atk[4]
        P1EffectActivate = atk[5]
        P1DiceType = atk[6]
        P1BonusType = bonusType
    elif Player == "P2":
        P2AtkSelID = atk[0]
        P2AtkSelected = atk[1]
        P2AtkType = atk[2]
        P2AtkPower = atk[3]
        P2Effect = atk[4]
        P2EffectActivate = atk[5]
        P2DiceType = atk[6]
        P1BonusType = bonusType


def selectAttack(player):
    global P1, P1Atk1, P1Atk2, P1TM, P1Type, P2, P2Atk1, P2Atk2, P2TM, P2Type

    if player == "P1":
        Pokemon = P1
        atk1 = P1Atk1
        atk2 = P1Atk2
        TM = P1TM
        rivalType = P2Type
    elif player == "P2":
        Pokemon = P2
        atk1 = P2Atk1
        atk2 = P2Atk2
        TM = P2TM
        rivalType = P1Type

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
                print("Attack selected:")
                passAttack(player, atk1, bonusType1)

            elif i == 2:
                print("Attack selected:")
                passAttack(player, atk2, bonusType2)
            else:
                print("Error attack not selected")
        else:
            # No TM and NO Atk2
            print("Attack selected:")
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
            # Pasar Valores
            passAttack(player, atk1, bonusType1)
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
                print("Attack selected:")
                passAttack(player, atk1, bonusType1)

            elif i == 2:
                print("Attack selected:")
                passAttack(player, atk2, bonusType2)

            elif i == 3:
                print("Attack selected:")
                passAttack(player, TM, bonusTypeTM)
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
                print("Attack selected:")
                passAttack(player, atk1, bonusType1)

            elif i == 3:
                print("Attack selected:")
                passAttack(player, TM, bonusTypeTM)
            else:
                print("Error attack not selected")


def statusEffect(effect, attacker, defender):

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


def activateEffect(pokemon, effect, activate, statusP1, statusP2):

    if effect != "NONE":
        if activate != "Automatic":
            i = int(input("\n" + pokemon + ":  effect Activated ?"))
            if i == 1:
                print("Effect Activated!!!!")
                status = statusEffect(effect, statusP1, statusP2)
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
    else:
        return status


# Function from effects
def BrickBreak(status):
    if status == "Disdadvantage":
        status = "Normal"
        return status


def Brine(AttackPower):
    AttackPower = +1
    return AttackPower


def Conversion(Type, RivalType):
    Type = RivalType
    return Type


def Conversion2(Type, AttackType):
    if AttackType == "NORMAL" or AttackType == "GRASS" or AttackType == "FLYING" or AttackType == "POISON" or AttackType == "ROCK" or AttackType == "BUG" or AttackType == "PSYCHIC" or AttackType == "ICE" or AttackType == "DRAGON" or AttackType == "STEEL" or AttackType == "FAIRY":
        Type = "STEEL"
        return Type
    elif AttackType == "GRASS" or AttackType == "WATER" or AttackType == "GROUND" or AttackType == "ELECTRIC":
        Type = "GRASS"
        return Type
    elif AttackType == "GHOST" or AttackType == "DARK":
        Type = "DARK"
        return Type
    elif AttackType == "FIRE":
        Type = "WATER"
        return Type
    elif AttackType == "FIGHTING":
        Type = "FLYING"
        return Type
    else:
        print("Error on Effect Conversion 2")


def Counter(AttackPower, RivalAttack):
    AttackPower = RivalAttack
    return AttackPower


def Covet(RivalAttatch):
    if RivalAttatch != None:
        PlayerAttach = RivalAttatch
        RivalAttatch = None
        return PlayerAttach, RivalAttatch
    else:
        print("No attatch Item on Player")


def protect(Attack, Effect, Bonus):
    Attack = 0
    Effect = 0
    Bonus = 0
    return Attack, Effect, Bonus


def Disable(Atk1, Atk2, TM, Rival, AttackSelected):
    # No atk2 and NO tm
    if Atk2 == "000" and TM == "000":
        print("Unable to active effect , user only have 1 attack")
    # No atk 2 but Yes TM
    elif Atk2 == "000" and TM != "000":
        print("Select one attack to remove")
        print("1.-" + Atk1)
        print("2.-" + TM)
        i = int(input())
        if i == 1:
            if AttackSelected == Atk1:
                AttackSelected == TM
                Atk1 = "000"
                return Atk1, Atk2, TM, AttackSelected
            else:
                Atk1 = "000"
                return Atk1, Atk2, TM, AttackSelected

        if i == 2:
            if AttackSelected == TM:
                AttackSelected == Atk1
                TM = "000"
                return Atk1, Atk2, TM, AttackSelected
            else:
                TM = "000"
                return Atk1, Atk2, TM, AttackSelected
    # Atk2 Yes TM Yes
    else:
        if TM == "000":
            print("Select one attack to remove")
            print("1.-" + Atk1)
            print("2.-" + Atk2)
            print("3.-" + TM)
            i = int(input())
            if i == 1:
                if AttackSelected == Atk1:
                    x = int(input("Select  a new Attack"))
                    AttackSelected == Atk2
                    Atk1 = "000"
                    return Atk1, Atk2, AttackSelected
                else:
                    Atk1 = "000"
                    return Atk1, Atk2, AttackSelected

            if i == 2:
                if AttackSelected == Atk2:
                    AttackSelected == Atk1
                    Atk2 = None
                    return Atk1, Atk2, AttackSelected
                else:
                    Atk2 = "000"
                    return Atk1, Atk2, AttackSelected
        else:
            print("Select one attack to remove")
            print("1.-" + Atk1)
            print("2.-" + Atk2)
            print("3.-" + TM)


Round = 0
BattleFinish = False
Player = "P1"
phase = 0
if __name__ == '__main__':

    while (BattleFinish != True):
       # P1 select Pokemon
        if phase == 0:
            Player = "P1"
            print("P1 Select")
            selectPokemon(Player)
            print("Pokemon Selected: " + P1)
            print(P1Atk1)
            phase = 1
        # P2 select Pokemon
        elif phase == 1:
            Player = "P2"
            print("\nP2 Select")
            selectPokemon(Player)
            print("Pokemon Selected: " + P2)
            phase = 2
        # P1 select Attack
        elif phase == 2:
            Player = "P1"
            selectAttack(Player)
            print(P1AtkSelected)
            phase = 3
        # P2 select attack
        elif phase == 3:
            Player = "P2"
            selectAttack(Player)
            print(P2AtkSelected)
            phase = 4
        # P1 effect
        elif phase == 4:
            print("\n Phase 4: ->")
            P1status = "Normal"
            P2status = "Normal"
            tupleEffect = activateEffect(
                P1, P1AtkEffect, P1AtkActivate, P1status, P2status)

            P1status = tupleEffect[0]
            P2status = tupleEffect[1]
            print("P1Status:" + P1status)
            print("P2Status:" + P2status)

            phase = 5
            # verify status P2 and attack
        elif phase == 5:
            print("\n Phase 5: ->")
            P2status = checkStatusP2(P2, P2status)

            # If no attack P2
            if P2status == "Frozen" or P2status == "Sleep" or P2status == "Paralized":
                P2AtkPower = 0
                P2BonusType = 0
                phase = 7
            else:
                tupleEffect = activateEffect(
                    P2, P2AtkEffect, P2AtkActivate, P2status, P1status)
                P1status = tupleEffect[1]
                P2status = tupleEffect[0]
                phase = 6
        # Verify status P1
        elif phase == 6:
            print("\n Phase 6: ->")
            P1status = checkStatusP2(P1, P1status)

            # if No attack P1
            if P1status == "Frozen" or P1status == "Sleep" or P1status == "Paralized":
                P1AtkPower = 0
                P1BonusType = 0
                phase = 7
            else:
                phase = 7
        elif phase == 7:
            print("\n Phase 7: ->")
            print("P1Status:" + P1status)
            print("P2Status:" + P2status)

            phase = 8
        elif phase == 8:
            pass
