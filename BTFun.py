import sqlite3
import GloVar
import effects
import serial


def resetNewBattle():
    GloVar.P1Dice = 0
    GloVar.P2Dice = 0
    GloVar.TotalP1 = 0
    GloVar.TotalP2 = 0
    GloVar.P1BonusType = 0
    GloVar.P2BonusType = 0
    GloVar.Round = 0
    GloVar.P1Status = "Normal"
    GloVar.P2Status = "Normal"
    GloVar.P1Effect = "None"
    GloVar.P2Effect = "None"


def resetNewRound():
    GloVar.P1Dice = 0
    GloVar.P2Dice = 0
    GloVar.TotalP1 = 0
    GloVar.TotalP2 = 0
    GloVar.P1BonusType = 0
    GloVar.P2BonusType = 0
    GloVar.P1Effect = "None"
    GloVar.P2Effect = "None"


def readSerialUntil(arduino):

    while True:
        if arduino.in_waiting:
            data = arduino.readline().decode('utf-8').rstrip('\n')
            return data


def sendToArduino(text, arduino):
    arduino.write((text + "\r").encode())


def buttons(arduino):
    arduino.write("OPTION\r".encode())
    data = readSerialUntil(arduino)
    i = int(data)
    return i


def dice(arduino):
    arduino.write("DICE\r".encode())
    data = readSerialUntil(arduino)
    i = int(data)
    return i


def addLevel(arduino):
    conn = sqlite3.connect('pokimon.sqlite')
    c = conn.cursor()
    found = False
    while found == False:
        print("Scan Pokemon")
        tag = readSerialUntil(arduino)
        newTAG = (tag[:-1])
        c.execute("SELECT * FROM pokemons WHERE UID = (?)", (newTAG,))
        pokemon = c.fetchone()
        if pokemon == None:
            print("Pokemon not found , please try again ")
            sendToArduino("READ", arduino)
        else:
            found = True
            Level = pokemon[9] + 1
            c.execute("UPDATE pokemons SET Extra=(?)  WHERE UID = (?)",
                      (Level, newTAG,))
            conn.commit()
            conn.close()
            print("Level updated Succesfully")


def selectPokemon(player, arduino):
    conn = sqlite3.connect('pokimon.sqlite')
    c = conn.cursor()
    found = False
    while found == False:
        tag = readSerialUntil(arduino)
        newTAG = (tag[:-1])
        c.execute("SELECT * FROM pokemons WHERE UID = (?)", (newTAG,))
        pokemon = c.fetchone()
        if pokemon == None:
            print("Pokemon not found , please try again ")
            sendToArduino("READ", arduino)

        else:
            found = True
            conn.commit()
            conn.close()
            if player == "P1":
                GloVar.P1 = pokemon[2]
                GloVar.P1Level = pokemon[3]
                GloVar.P1Type = pokemon[4]
                GloVar.P1Atk1 = getAttack(pokemon[5])
                GloVar.P1Atk2 = getAttack(pokemon[6])
                GloVar.P1TM = pokemon[7]
                GloVar.P1Extra = pokemon[9]
                GloVar.P1Attatch = pokemon[10]
            elif player == "P2":
                GloVar.P2 = pokemon[2]
                GloVar.P2Level = pokemon[3]
                GloVar.P2Type = pokemon[4]
                GloVar.P2Atk1 = getAttack(pokemon[5])
                GloVar.P2Atk2 = getAttack(pokemon[6])
                GloVar.P2TM = pokemon[7]
                GloVar.P2Extra = pokemon[9]
                GloVar.P2Attatch = pokemon[10]


def getAttack(Attack):
    conn = sqlite3.connect('pokimon.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM Attacks WHERE IdAtk = (?)", (Attack,))
    attackfound = c.fetchone()
    if attackfound == None:
        print("Attack Not Found")

    else:
        conn.commit()
        conn.close()
        return attackfound


def attack_Bonus(Attack_type, PkmRival_type):
    if (Attack_type == "NORMAL") and (PkmRival_type == "STEAL" or PkmRival_type == "GHOST" or PkmRival_type == "ROCK"):
        status = -2
        return status

    if (Attack_type == "GRASS"):
        if (PkmRival_type == "GROUND" or PkmRival_type == "WATER" or PkmRival_type == "ROCK"):
            status = 2
            return status
        if (PkmRival_type == "POISON" or PkmRival_type == "BUG" or PkmRival_type == "GRASS" or PkmRival_type == "FIRE" or PkmRival_type == "DRAGON" or PkmRival_type == "FLY" or PkmRival_type == "STEAL"):
            status = -2
            return status

    if (Attack_type == "FIRE"):
        if (PkmRival_type == "ICE" or PkmRival_type == "GRASS" or PkmRival_type == "BUG" or PkmRival_type == "STEAL"):
            status = 2
            return status
        if (PkmRival_type == "ROCK" or PkmRival_type == "FIRE" or PkmRival_type == "WATER" or PkmRival_type == "DRAGON"):
            status = -2
            return status

    if (Attack_type == "WATER"):
        if (PkmRival_type == "GROUND" or PkmRival_type == "ROCK" or PkmRival_type == "FIRE"):
            status = 2
            return status
        if (PkmRival_type == "WATER" or PkmRival_type == "GRASS" or PkmRival_type == "DRAGON"):
            status = -2
            return status

    if (Attack_type == "FIGHTING"):
        if (PkmRival_type == "NORMAL" or PkmRival_type == "ROCK" or PkmRival_type == "ICE" or PkmRival_type == "DARK" or PkmRival_type == "STEAL"):
            status = 2
            return status
        if (PkmRival_type == "FLYING" or PkmRival_type == "POISON" or PkmRival_type == "BUG" or PkmRival_type == "PSYCHIC" or PkmRival_type == "GHOST" or PkmRival_type == "FAIRY"):
            status = -2
            return status

    if (Attack_type == "FLYING"):
        if (PkmRival_type == "FIGHTING" or PkmRival_type == "BUG" or PkmRival_type == "GRASS"):
            status = 2
            return status
        if (PkmRival_type == "ELECTRIC" or PkmRival_type == "ROCK" or PkmRival_type == "STEAL"):
            status = -2
            return status

    if (Attack_type == "POISON"):
        if (PkmRival_type == "GRASS" or PkmRival_type == "FAIRY"):
            status = 2
            return status
        if (PkmRival_type == "POISON" or PkmRival_type == "GROUND" or PkmRival_type == "ROCK" or PkmRival_type == "GHOST" or PkmRival_type == "STEAL"):
            status = -2
            return status

    if (Attack_type == "GROUND"):
        if (PkmRival_type == "POISON" or PkmRival_type == "ROCK" or PkmRival_type == "FIRE" or PkmRival_type == "ELECTRIC" or PkmRival_type == "STEAL"):
            status = 2
            return status
        if (PkmRival_type == "FLYING" or PkmRival_type == "BUG" or PkmRival_type == "GRASS"):
            status = -2
            return status

    if (Attack_type == "ROCK"):
        if (PkmRival_type == "FLYING" or PkmRival_type == "BUG" or PkmRival_type == "FIRE" or PkmRival_type == "ICE"):
            status = 2
            return status
        if (PkmRival_type == "FIGHTING" or PkmRival_type == "GROUND" or PkmRival_type == "STEAL"):
            status = -2
            return status

    if (Attack_type == "BUG"):
        if (PkmRival_type == "GRASS" or PkmRival_type == "PSYCHIC" or PkmRival_type == "DARK"):
            status = 2
            return status
        if (PkmRival_type == "FIGHTING" or PkmRival_type == "FLYING" or PkmRival_type == "GHOST" or PkmRival_type == "STEAL" or PkmRival_type == "POISON" or PkmRival_type == "FIRE" or PkmRival_type == "FAIRY"):
            status = -2
            return status

    if (Attack_type == "GHOST"):
        if (PkmRival_type == "GHOST" or PkmRival_type == "PSYCHIC"):
            status = 2
            return status
        if (PkmRival_type == "NORMAL" or PkmRival_type == "DARK"):
            status = -2
            return status

    if (Attack_type == "ELECTRIC"):
        if (PkmRival_type == "FLYING" or PkmRival_type == "WATER"):
            status = 2
            return status
        if (PkmRival_type == "GROUND" or PkmRival_type == "GRASS" or PkmRival_type == "ELECTRIC" or PkmRival_type == "DRAGON"):
            status = -2
            return status

    if (Attack_type == "PSYCHIC"):
        if (PkmRival_type == "FIGHTING" or PkmRival_type == "POISON"):
            status = 2
            return status
        if (PkmRival_type == "PSYCHIC" or PkmRival_type == "STEAL" or PkmRival_type == "DARK"):
            status = -2
            return status

    if (Attack_type == "ICE"):
        if (PkmRival_type == "FLYING" or PkmRival_type == "GROUND" or PkmRival_type == "GRASS" or PkmRival_type == "DRAGON"):
            status = 2
            return status
        if (PkmRival_type == "FIRE" or PkmRival_type == "WATER" or PkmRival_type == "ICE" or PkmRival_type == "STEAL"):
            status = -2
            return status

    if (Attack_type == "DRAGON"):
        if (PkmRival_type == "DRAGON"):
            status = 2
            return status
        if (PkmRival_type == "STEAL" or PkmRival_type == "FAIRY"):
            status = -2
            return status

    if (Attack_type == "DARK"):
        if (PkmRival_type == "GHOST" or PkmRival_type == "PSYCHIC"):
            status = 2
            return status
        if (PkmRival_type == "FIGHTING" or PkmRival_type == "DARK" or PkmRival_type == "FAIRY"):
            status = -2
            return status

    if (Attack_type == "STEAL"):
        if (PkmRival_type == "ROCK" or PkmRival_type == "ICE" or PkmRival_type == "FAIRY"):
            status = 2
            return status
        if (PkmRival_type == "FIRE" or PkmRival_type == "WATER" or PkmRival_type == "ELECTRIC" or PkmRival_type == "STEAL"):
            status = -2
            return status

    if (Attack_type == "FAIRY"):
        if (PkmRival_type == "FIGHTING" or PkmRival_type == "DRAGON" or PkmRival_type == "DARK"):
            status = 2
            return status
        if (PkmRival_type == "FIRE" or PkmRival_type == "POSION" or PkmRival_type == "STEAL"):
            status = -2
            return status

    else:
        status = 0
        return status


def passAttack(Player, atk, bonusType, atkChoosen):

    if Player == "P1":
        GloVar.P1AtkSelID = atk[0]
        GloVar.P1AtkSelected = atk[1]
        GloVar.P1AtkType = atk[2]
        GloVar.P1AtkPower = atk[3]
        GloVar.P1AtkEffect = atk[4]
        GloVar.P1EffectActivate = atk[5]
        GloVar.P1DiceType = atk[6]
        GloVar.P1BonusType = bonusType
        GloVar.P1AtkChoosen = atkChoosen
    elif Player == "P2":
        GloVar.P2AtkSelID = atk[0]
        GloVar.P2AtkSelected = atk[1]
        GloVar.P2AtkType = atk[2]
        GloVar.P2AtkPower = atk[3]
        GloVar.P2AtkEffect = atk[4]
        GloVar.P2EffectActivate = atk[5]
        GloVar.P2DiceType = atk[6]
        GloVar.P2BonusType = bonusType
        GloVar.P2AtkChoosen = atkChoosen


def selectAttack(player, arduino):

    if player == "P1":
        Pokemon = GloVar.P1
        atk1 = GloVar.P1Atk1
        atk2 = GloVar.P1Atk2
        TM = GloVar.P1TM
        rivalType = GloVar.P2Type
    elif player == "P2":
        Pokemon = GloVar.P2
        atk1 = GloVar.P2Atk1
        atk2 = GloVar.P2Atk2
        TM = GloVar.P2TM
        rivalType = GloVar.P1Type

    bonusType1 = 0
    bonusType2 = 0
    bonusTypeTM = 0

    if (TM == "000"):
        # No TM - with ATK2
        if (atk2[0] != "000"):
            print("\n" + Pokemon + " select Attack: ")
            bonusType1 = attack_Bonus(atk1[2], rivalType)
            print("1.-" + atk1[1] + ":" +
                  str(atk1[3]) + "->" + "Bonus:" + str(bonusType1))

            bonusType2 = attack_Bonus(atk2[2], rivalType)
            print("2.-" + atk2[1] + ":" +
                  str(atk2[3]) + "->" + "Bonus:" + str(bonusType2))

            i = buttons(arduino)
            if i == 1:
                print("Attack selected:")
                passAttack(player, atk1, bonusType1, 1)

            elif i == 2:
                print("Attack selected:")
                passAttack(player, atk2, bonusType2, 2)
            else:
                print("Error attack not selected")
        else:
            # No TM and NO Atk2
            print("Attack selected:")
            bonusType1 = attack_Bonus(atk1[2], rivalType)
            print("1.-" + atk1[1] + ":" +
                  str(atk1[3]) + "->" + "Bonus:" + str(bonusType1))
            passAttack(player, atk1, bonusType1, 1)
    else:
        # With TM and with ATK2
        if (atk2[0] != "000"):
            print("\n" + Pokemon + " select an Attack: ")
            bonusType1 = attack_Bonus(atk1[2], rivalType)
            print("1.-" + atk1[1] + ":" +
                  str(atk1[3]) + "->" + "Bonus:" + str(bonusType1))

            bonusType2 = attack_Bonus(atk2[2], rivalType)
            print("2.-" + atk2[1] + ":" +
                  str(atk2[3]) + "->" + "Bonus:" + str(bonusType2))

            bonusTypeTM = attack_Bonus(TM[2], rivalType)
            print("3.-" + TM[1] + ":" +
                  str(TM[3]) + "->" + str(bonusTypeTM))
            i = buttons(arduino)
            if i == 1:
                print("Attack selected:")
                passAttack(player, atk1, bonusType1, 1)

            elif i == 2:
                print("Attack selected:")
                passAttack(player, atk2, bonusType2, 2)

            elif i == 3:
                print("Attack selected:")
                passAttack(player, TM, bonusTypeTM, 3)
            else:
                print("Error attack not selected")
        else:
            print("\n" + Pokemon + "Seelect Attack: ")
            bonusType1 = attack_Bonus(atk1[2], rivalType)
            print("1.-" + atk1[1] + ":" +
                  str(atk1[3]) + "->" + "Bonus:" + str(bonusType1))

            bonusTypeTM = attack_Bonus(TM[2], rivalType)
            print("3.-" + TM[1] + ":" +
                  str(TM[3]) + "->" + "Bonus:" + str(bonusTypeTM))

            i = buttons(arduino)
            if i == 1:
                print("Attack selected:")
                passAttack(player, atk1, bonusType1, 1)

            elif i == 3:
                print("Attack selected:")
                passAttack(player, TM, bonusTypeTM, 3)
            else:
                print("Error attack not selected")


def instantEffect(player, effect, attackerStatus, defenderStatus, attackerEffect, defenderEffect):
    print("Looking for effect ->")
    print(effect)
    if effect == "Advantage":
        attackerEffect = "Advantage"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "DoubleAdvantage":
        attackerEffect = "DoubleAdvantage"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Disadvantage":
        attackerEffect = "Disadvantage"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "DoubleDisadvantage":
        attackerEffect = "DoubleDisadvantage"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Faint":
        attackerEffect = "Faint"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Switch":
        print("Effect no ready ")
        attackerEffect = "Switch"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "OwnConfusion":
        attackerStatus = "Confused"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "QuickAttack":
        attackerEffect = "Quick"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Neutro":
        attackerEffect = "Neutro"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Once":
        attackerEffect = "Once"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "DoubleDice":
        attackerEffect = "DoubleDice"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Kill":
        attackerEffect = "Kill"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Confusion":
        defenderStatus = "Confused"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Burn":
        defenderStatus = "Burned"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Frozen":
        defenderStatus = "Frozen"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Paralize":
        defenderStatus = "Paralized"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Poison":
        defenderStatus = "Poisoned"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Sleep":
        defenderStatus = "Sleep"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Snore":
        attackerEffect = "Snore"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "SleepTalk":
        attackerEffect = "SleepTalk"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "SmellingSalts":
        attackerStatus = "SmellingSalts"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Facade":
        attackerStatus = "Facade"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "StatusUp":
        attackerStatus = "StatusUp"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Neutro":
        attackerStatus = "Neutro"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Protect":
        attackerStatus = "Protect"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Detect":
        attackerStatus = "Detect"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect

    elif effect == "DreamEater":
        effects.DreamEater(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "LevelUp":
        effects.LevelUp(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "LevelDown":
        effects.LevelDown(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "StatusUp":
        attackerEffect = "StatusUp"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "WinTie":
        attackerEffect = "WinTie"
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Brine":
        effects.Brine(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "PayBack":
        effects.PayBack(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "MirrorCoat":
        effects.MirrorCoat(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "LevelUp":
        effects.LevelUp(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Counter":
        effects.Counter(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "MeFirst":
        effects.MeFirst(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "MetalBurst":
        effects.MetalBurst(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Mimic":
        effects.Mimic(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "LevelDown":
        effects.LevelDown(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "PlusRound":
        effects.PlusRound(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "RollOut":
        effects.RolloOut(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "FuryCutter":
        effects.FuryCutter(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "FuryCutter":
        effects.FuryCutter(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "StealthRock":
        effects.StealthRock(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Metronome":
        effects.Metronome(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "HiddenPower":
        effects.HiddenPower(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Judgement":
        effects.Judgement(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Tranform":
        effects.Transform(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Sketch":
        effects.Sketch(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "KnockOff":
        effects.KnockOff(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "MirrorMove":
        effects.MirrorMove(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "MirrorMove":
        effects.MirrorMove(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "FireFang":
        effects.FireFang(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "IceFang":
        effects.IceFang(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "ThunderFang":
        effects.ThunderFang(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect

    elif effect == "Conversion":
        effects.Conversion(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Conversion2":
        effects.Conversion2(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "NoItems":
        effects.NoItems(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Embargo":
        effects.Embargo(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "MagicCoat":
        effects.MagicCoat(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Safeguard":
        effects.SafeGuard(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Thief":
        effects.Thief(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "Covet":
        effects.Covet(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "MeanLook":
        effects.MeanLook(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    elif effect == "TriAttack":
        effects.TriAttack(player)
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect
    else:
        print("effect no found ")
        return attackerStatus, defenderStatus, attackerEffect, defenderEffect


def activateEffect(player, arduino):

    if player == "P1":
        pokemon = GloVar.P1
        effect = GloVar.P1AtkEffect
        activate = GloVar.P1EffectActivate
        statusPlayer = GloVar.P1Status
        statusRival = GloVar.P2Status
        playerEffect = GloVar.P1Effect
        rivalEffect = GloVar.P2Effect
    elif player == "P2":
        pokemon = GloVar.P2
        effect = GloVar.P2AtkEffect
        activate = GloVar.P2EffectActivate
        statusPlayer = GloVar.P2Status
        statusRival = GloVar.P1Status
        playerEffect = GloVar.P2Effect
        rivalEffect = GloVar.P1Effect

    if effect != "NONE":
        if activate != "Automatic":
            print("\n" + pokemon + ":  effect Activated ?")
            i = buttons(arduino)
            if i == 1:
                print("Effect Activated!!!!")
                status = instantEffect(
                    player, effect, statusPlayer, statusRival, playerEffect, rivalEffect)
                if player == "P1":
                    GloVar.P1Status = status[0]
                    GloVar.P2Status = status[1]
                    GloVar.P1Effect = status[2]
                    GloVar.P2Effect = status[3]
                    return
                elif player == "P2":
                    GloVar.P2Status = status[0]
                    GloVar.P1Status = status[1]
                    GloVar.P2Effect = status[2]
                    GloVar.P1Effect = status[3]

                    return

            if i == 2:
                print("Effect NO activated!!!! ")
        elif activate == "Automatic":
            print("Effect Activated Automatically!!!!")
            status = instantEffect(
                player, effect, statusPlayer, statusRival, playerEffect, rivalEffect)
            if player == "P1":
                GloVar.P1Status = status[0]
                GloVar.P2Status = status[1]
                GloVar.P1Effect = status[2]
                GloVar.P2Effect = status[3]
                return
            elif player == "P2":
                GloVar.P2Status = status[0]
                GloVar.P1Status = status[1]
                GloVar.P2Effect = status[2]
                GloVar.P1Effect = status[3]
                return

    else:
        print("Attack with no Effect")
        return


def rollDicesEffect(player, arduino):
    if player == "P1":
        if GloVar.P1Effect == "Advantage":
            print(GloVar.P1 + "Roll 2 dices and discard the lowest")
            throwDice(player, arduino)
        elif GloVar.P1Effect == "DoubleAdvantage":
            print(GloVar.P1 + "Roll 3 dices and discard the 2 lowest")
            throwDice(player, arduino)
        elif GloVar.P1Effect == "Upto3":
            effects.upto3(player, arduino)

        elif GloVar.P1Effect == "DoubleDice":
            effects.doubleDice(player, arduino)
        elif GloVar.P2Effect == "Disadvantage":
            print(GloVar.P1 + "Roll 2 dices and discard the Highest")
            throwDice(player, arduino)
        elif GloVar.P2Effect == "DoubleDisadvantage":
            print(GloVar.P1 + "Roll 3 dices and discard the 2 Highest")
            throwDice(player, arduino)
        else:
            throwDice(player, arduino)
    elif player == "P2":
        if GloVar.P2Effect == "Advantage":
            print(GloVar.P2 + "Roll 2 dices and discard the lowest")
            throwDice(player, arduino)
        elif GloVar.P2Effect == "DoubleAdvantage":
            print(GloVar.P2 + "Roll 3 dices and discard the 2 lowest")
            throwDice(player, arduino)
        elif GloVar.P2Effect == "Upto3":
            effects.upto3(player, arduino)

        elif GloVar.P2Effect == "DoubleDice":
            effects.doubleDice(player, arduino)
        elif GloVar.P1Effect == "Disadvantage":
            print(GloVar.P2 + "Roll 2 dices and discard the Highest")
            throwDice(player, arduino)
        elif GloVar.P1Effect == "DoubleDisadvantage":
            print(GloVar.P2 + "Roll 3 dices and discard the 2 Highest")
            throwDice(player, arduino)
        else:
            throwDice(player, arduino)


def removeStatus(player, arduino):
    if player == "P1":
        pokemon = GloVar.P1
        status = GloVar.P1Status
    elif player == "P2":
        pokemon = GloVar.P2
        status = GloVar.P2Status

    if status == "Frozen":
        print(pokemon + " is Frozen, need 4 to use attack:")
        print("/n Roll D4 Dice ?")
        i = dice(arduino)
        if i == 4:
            print("Status Removed")
            status = "Normal"
            return status
        else:
            print("Status not Removed ")
            print("Use item to remove status ? \n 1.Yes / 2.NO")
            i = buttons(arduino)
            if i == 1:
                print("Status Removed with Item")
                status = "Normal"
                return status
            elif i == 2:
                print("Status not Removed ")
                return status
    if status == "Paralized":
        print(pokemon + " is Parallized, need 1 to use attack:")
        print("/n Roll D4 Dice ?")
        i = dice(arduino)
        if i == 1:
            print("Status Removed")
            status = "Normal"
            return status
        else:
            print("Status not Removed ")
            print("Use item to remove status ? \n 1.Yes / 2.NO")
            i = buttons(arduino)
            if i == 1:
                print("Status Removed with Item")
                status = "Normal"
                return status
            elif i == 2:
                print("Status not Removed ")
                return status
    if status == "Sleep":
        print(pokemon + " is Sleeping, Unable to use attack:")
        print("Use item to remove status ? \n 1.Yes / 2.NO")
        i = buttons(arduino)
        if i == 1:
            print("Status Removed with Item")
            status = "Normal"
            return status
        elif i == 2:
            print("Status not Removed ")
            return status
    else:
        return status


def throwDice(player, arduino):

    if player == "P1":
        if GloVar.P1Status == "Confused":
            print(GloVar.P1 + " is confused !")
            print(GloVar.P1 + " Roll Dice = ")
            i = dice(arduino)
            GloVar.P1Dice = GloVar.P1Dice + i
            if GloVar.P1Status == "Confused":
                if i == 1 or i == 3 or i == 5:
                    GloVar.P2Dice = GloVar.P2Dice + i
        else:
            print(GloVar.P1 + " Roll Dice = ")
            i = dice(arduino)
            GloVar.P1Dice = GloVar.P1Dice + i

    elif player == "P2":
        if GloVar.P2Status == "Confused":
            print(GloVar.P2 + " is confused !")
            print(GloVar.P2 + " Roll Dice =")
            i = dice(arduino)
            GloVar.P2Dice = GloVar.P2Dice + i
            if i == 1 or i == 3 or i == 5:
                GloVar.P1Dice = GloVar.P1Dice + i
        else:
            print(GloVar.P2 + " Roll Dice = ")
            i = dice(arduino)
            GloVar.P2Dice = GloVar.P2Dice + i


def getAttackWithID(player, ID):
    atk = getAttack(ID)
    if player == "P1":
        GloVar.P1AtkSelID = atk[0]
        GloVar.P1AtkSelected = atk[1]
        GloVar.P1AtkType = atk[2]
        GloVar.P1AtkPower = atk[3]
        GloVar.P1AtkEffect = atk[4]
        GloVar.P1EffectActivate = atk[5]
        GloVar.P1DiceType = atk[6]
        GloVar.P1BonusType = attack_Bonus(GloVar.P1AtkType, GloVar.P2Type)
    elif player == "P2":
        GloVar.P2AtkSelID = atk[0]
        GloVar.P2AtkSelected = atk[1]
        GloVar.P2AtkType = atk[2]
        GloVar.P2AtkPower = atk[3]
        GloVar.P2AtkEffect = atk[4]
        GloVar.P2EffectActivate = atk[5]
        GloVar.P2DiceType = atk[6]
        GloVar.P2BonusType = attack_Bonus(GloVar.P2AtkType, GloVar.P1Type)


def debugprint():
    print("\n-------------Debug-------------------")
    print("Pokemon Selected : " + GloVar.P1 + " Level: " +
          str(GloVar.P1Level) + " Extra: " + str(GloVar.P1Extra))
    print("Attack Selected :" + GloVar.P1AtkSelected + " Power:" +
          str(GloVar.P1AtkPower) + " Effect:" + GloVar.P1Effect + " Dice:" + GloVar.P1DiceType)
    print("Status:" + GloVar.P1Status + " Bonus:" + str(GloVar.P1BonusType))
    print("--------------------------------")
    print("Pokemon Selected : " + GloVar.P2 + " Level: " +
          str(GloVar.P2Level) + " Extra: " + str(GloVar.P2Extra))
    print("Attack Selected :" + GloVar.P2AtkSelected + " Power:" +
          str(GloVar.P2AtkPower) + " Effect:" + GloVar.P2Effect + " Dice:" + GloVar.P2DiceType)
    print("Status:" + GloVar.P2Status + " Bonus:" + str(GloVar.P2BonusType))
    print("--------------------------------")


def advantages(player):
    if player == "P1":
        if GloVar.P1Effect == "Advantage":
            if GloVar.P2Effect == "Disadvantage":
                GloVar.P1Effect = "NONE"
                GloVar.P2Effect = "NONE"
            elif GloVar.P2Effect == "DoubleDisadvantage":
                GloVar.P1Effect = "NONE"
                GloVar.P2Effect = "Disadvantage"
            elif GloVar.P2Effect == "Snatch":
                GloVar.P1Effect = "NONE"
                GloVar.P2Effect = "Advantage"
            else:
                GloVar.P1Effect = "Advantage"

        elif GloVar.P1Effect == "Disadvantage":
            if GloVar.P2Effect == "Advantage":
                GloVar.P1Effect = "NONE"
                GloVar.P2Effect = "NONE"
            elif GloVar.P2Effect == "DoubleAdavantage":
                GloVar.P1Effect = "NONE"
                GloVar.P2Effect = "Advantage"
            elif GloVar.P2Effect == "BrickBreak":
                GloVar.P1Effect = "NONE"
                GloVar.P2Effect = "NONE"
            elif GloVar.P2Effect == "Mist":
                GloVar.P1Effect = "NONE"
                GloVar.P1Effect = "NONE"
            else:
                GloVar.P1Effect = "Disadvantage"

        elif GloVar.P1Effect == "DoubleAdvantage":
            if GloVar.P2Effect == "Disadvantage":
                GloVar.P1Effect = "Advantage"
                GloVar.P2Effect = "NONE"
            elif GloVar.P2Effect == "DoubleDisadvantage":
                GloVar.P1Effect = "NONE"
                GloVar.P2Effect = "NONE"
            else:
                GloVar.P1Effect = "DoubleAdvantage"

        elif GloVar.P1Effect == "DoubleDisadvantage":
            if GloVar.P2Effect == "Advantage":
                GloVar.P1Effect = "Disadvantage"
                GloVar.P2Effect = "NONE"
            elif GloVar.P2Effect == "DoubleAdvantage":
                GloVar.P1Effect = "NONE"
                GloVar.P2Effect = "NONE"
            else:
                GloVar.P1Effect = "DoubleDisadvantage"

    elif player == "P2":
        if GloVar.P2Effect == "Advantage":
            if GloVar.P1Effect == "Disadvantage":
                GloVar.P1Effect = "NONE"
                GloVar.P2Effect = "NONE"
            elif GloVar.P1Effect == "DoubleDisadvantage":
                GloVar.P2Effect = "NONE"
                GloVar.P1Effect = "Disadvantage"
            elif GloVar.P1Effect == "Snatch":
                GloVar.P2Effect = "NONE"
                GloVar.P1Effect = "Advantage"
            else:
                GloVar.P2Effect = "Advantage"

        elif GloVar.P2Effect == "Disadvantage":
            if GloVar.P1Effect == "Advantage":
                GloVar.P1Effect = "NONE"
                GloVar.P2Effect = "NONE"
            elif GloVar.P1Effect == "DoubleAdavantage":
                GloVar.P2Effect = "NONE"
                GloVar.P1Effect = "Advantage"
            elif GloVar.P1Effect == "BrickBreak":
                GloVar.P2Effect = "NONE"
                GloVar.P2Effect = "NONE"
            elif GloVar.P1Effect == "Mist":
                GloVar.P2Effect = "NONE"
                GloVar.P2Effect = "NONE"
            else:
                GloVar.P2Effect = "Disadvantage"

        elif GloVar.P2Effect == "DoubleAdvantage":
            if GloVar.P1Effect == "Disadvantage":
                GloVar.P2Effect = "Advantage"
                GloVar.P1Effect = "NONE"
            elif GloVar.P1Effect == "DoubleDisadvantage":
                GloVar.P1Effect = "NONE"
                GloVar.P2Effect = "NONE"
            else:
                GloVar.P2Effect = "DoubleAdvantage"

        elif GloVar.P2Effect == "DoubleDisadvantage":
            if GloVar.P1Effect == "Advantage":
                GloVar.P2Effect = "Disadvantage"
                GloVar.P1Effect = "NONE"
            elif GloVar.P1Effect == "DoubleAdvantage":
                GloVar.P1Effect = "NONE"
                GloVar.P2Effect = "NONE"
            else:
                GloVar.P2Effect = "DoubleDisadvantage"


def sumPartial():
    GloVar.TotalP1 = GloVar.P1Level + GloVar.P1AtkPower + \
        GloVar.P1Extra + GloVar.P1BonusType
    GloVar.TotalP2 = GloVar.P2Level + GloVar.P2AtkPower + \
        GloVar.P2Extra + GloVar.P2BonusType
    print(GloVar.P1 + ":" + " L:" + str(GloVar.P1Level + GloVar.P1Extra) + " + A:" +
          str(GloVar.P1AtkPower) + " + B:" + str(GloVar.P1BonusType) + "->Total:" + str(GloVar.TotalP1))
    print(GloVar.P2 + ":" + " L:" + str(GloVar.P2Level + GloVar.P2Extra) + " + A:" +
          str(GloVar.P2AtkPower) + " + B:" + str(GloVar.P2BonusType) + "->Total:" + str(GloVar.TotalP2))


def disableBeforeSelectAttack(player):
    if player == "P1":
        if GloVar.P1Atk1[0] == "033" or GloVar.P1Atk2[0] == "033":
            return
        else:
            if GloVar.P2Atk1[0] == "033" or GloVar.P2Atk2[0] == "033":
                i = int(input("P2 will use Disable ?"))
                if i == 1:
                    GloVar.P2AtkEffect = "Disable"
                    effects.Disable("P2")
                else:
                    return

        if GloVar.P2Atk1 == "186" or GloVar.P2Atk2 == "186":
            i = int(input("P2 will use Taunt ?"))
            if i == 1:
                effects.Taunt("P2")
            else:
                return
