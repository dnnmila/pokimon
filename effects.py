import GloVar
import BTFun
import sqlite3
from random import *
# Function from effects
import math

# Fuente: https://stackoverflow.com/a/52617883/2116607


def upto3(player, arduino):
    if player == "P1":
        if GloVar.P2Effect != "Disadvantage" and GloVar.P2Effect != "DoubleDisadvantage":
            print("Effected Activated, Minimun Dice = 3")
            BTFun.throwDice(player, arduino)
        elif GloVar.P2Effect == "Disadvantage":
            print("User has Disadvantage , discard the highest from 2 dices")
            print("Effected Activated, Minimun Dice = 3")
            BTFun.throwDice(player, arduino)
        elif GloVar.P2Effect == "DoubleDisadvantage":
            print("User has Double Disadvantage , discard the 2 highest from 3 dices")
            print("Effected Activated, Minimun Dice = 3")
            BTFun.throwDice(player, arduino)
    elif player == "P2":
        if GloVar.P1Effect != "Disadvantage" and GloVar.P1Effect != "DoubleDisadvantage":
            print("Effected Activated, Minimun Dice = 3")
            BTFun.throwDice(player, arduino)
        elif GloVar.P1Effect == "Disadvantage":
            print("User has Disadvantage , discard the highest from 2 dices")
            print("Effected Activated, Minimun Dice = 3")
            BTFun.throwDice(player, arduino)
        elif GloVar.P1Effect == "DoubleDisadvantage":
            print("User has Double Disadvantage , discard the 2 highest from 3 dices")
            print("Effected Activated, Minimun Dice = 3")
            BTFun.throwDice(player, arduino)


def doubleDice(player, arduino):
    if player == "P1":
        if GloVar.P2Effect != "Disadvantage" and GloVar.P2Effect != "DoubleDisadvantage":
            print("Effected Activated, Sum 2 Dices")
            print("First dice:")
            BTFun.throwDice(player, arduino)
            print("Second dice:")
            BTFun.throwDice(player, arduino)
        elif GloVar.P2Effect == "Disadvantage":
            print("User has Disadvantage , discard the highest from 3 dices")
            print("Effected Activated, Sum 2 lowest Dices")
            print("First dice:")
            BTFun.throwDice(player, arduino)
            print("Second dice:")
            BTFun.throwDice(player, arduino)
        elif GloVar.P2Effect == "DoubleDisadvantage":
            print("User has Double Disadvantage , discard the 2 highest from 4 dices")
            print("Effected Activated, Sum 2 lowest Dices")
            print("First dice:")
            BTFun.throwDice(player, arduino)
            print("Second dice:")
            BTFun.throwDice(player, arduino)
    elif player == "P2":
        if GloVar.P1Effect != "Disadvantage" and GloVar.P1Effect != "DoubleDisadvantage":
            print("Effected Activated, Sum 2 Dices")
            print("First dice:")
            BTFun.throwDice(player, arduino)
            print("Second dice:")
            BTFun.throwDice(player, arduino)
        elif GloVar.P1Effect == "Disadvantage":
            print("User has Disadvantage , discard the highest from 3 dices")
            print("Effected Activated, Sum 2 lowest Dices")
            print("First dice:")
            BTFun.throwDice(player, arduino)
            print("Second dice:")
            BTFun.throwDice(player, arduino)
        elif GloVar.P1Effect == "DoubleDisadvantage":
            print("User has Double Disadvantage , discard the 2 highest from 4 dices")
            print("Effected Activated, Sum 2 lowest Dices")
            print("First dice:")
            BTFun.throwDice(player, arduino)
            print("Second dice:")
            BTFun.throwDice(player, arduino)


def redondear(n: float, decimals: int = 0) -> float:
    expoN = n * 10 ** decimals
    if abs(expoN) - abs(math.floor(expoN)) < 0.5:
        return math.floor(expoN) / 10 ** decimals
    return math.ceil(expoN) / 10 ** decimals


def LevelUp(player):
    print("Atk Strenght = Level / 2 ")
    if player == "P1":
        GloVar.P1AtkPower = redondear((GloVar.P1Level + GloVar.P1Extra) / 2)
        print(GloVar.P1 + " Atk Strenght = " + GloVar.P1AtkPower)
    elif player == "P2":
        GloVar.P2AtkPower = redondear((GloVar.P2Level + GloVar.P2Extra) / 2)
        print(GloVar.P2 + "Atk Strenght = " + GloVar.P2AtkPower)


def LevelDown(player):
    print("Atk Strenght = Rival Level / 2 ")
    if player == "P1":
        GloVar.P1AtkPower = round((GloVar.P2Level + GloVar.P2Extra) / 2)
        print(GloVar.P1 + " Atk Strenght = " + GloVar.P1AtkPower)
    elif player == "P2":
        GloVar.P2AtkPower = round((GloVar.P1Level + GloVar.P1Extra) / 2)
        print(GloVar.P2 + "Atk Strenght = " + GloVar.P2AtkPower)


def StatusUp(player):
    print("If rival has status condition , player Atk + 1")
    if player == "P1":
        if GloVar.P2Status == "Confused" or GloVar.P2Status == "Frozen" or GloVar.P2Status == "Asleep" or GloVar.P2Status == "Burned" or GloVar.P2Status == "Poisoned" or GloVar.P2Status == "Paralized":
            GloVar.P1AtkPower = GloVar.P1AtkPower + 1
            print(GloVar.P1 + "Atk Strenght = " + GloVar.P1AtkPower)
        else:
            print("No status condition on Rival ")
    elif player == "P2":
        if GloVar.P1Status == "Confused" or GloVar.P1Status == "Frozen" or GloVar.P1Status == "Asleep" or GloVar.P1Status == "Burned" or GloVar.P1Status == "Poisoned" or GloVar.P1Status == "Paralized":
            GloVar.P2AtkPower = GloVar.P2AtkPower + 1
            print(GloVar.P2 + "Atk Strenght = " + GloVar.P2AtkPower)
        else:
            print("No status condition on Rival ")


def BrickBreak(player):
    print("Brick Break Effect -> ")
    if player == "P1":
        if GloVar.P2AtkEffect == "Disadvantage":
            print(GloVar.P1 + "Immune to disadvantage")
            GloVar.P2Effect = "None"
        else:
            GloVar.P1Effect = "None"
    elif player == "P2":
        if GloVar.P1AtkEffect == "Disadvantage":
            print(GloVar.P2 + "Immune to disadvantage")
            GloVar.P1Effect = "None"
        else:
            GloVar.P2Effect = "None"


def Brine(player):
    print("Brine Effect -> ")

    if player == "P1":
        print(GloVar.P1 + "Attack Strength + 1")
        GloVar.P1AtkPower = GloVar.P1AtkPower + 1
    elif player == "P2":
        print(GloVar.P2 + "Attack Strength + 1")
        GloVar.P2AtkPower = GloVar.P2AtkPower + 1


def Conversion(player):
    print("Conversion Effect -> ")
    print("Changing Pokemon type to Rival Atk Type ->")
    if player == "P1":
        GloVar.P1Type = GloVar.P2AtkType
        GloVar.P2BonusType = BTFun.attack_Bonus(
            GloVar.P2AtkType, GloVar.P1Type)

    elif player == "P2":
        GloVar.P2Type = GloVar.P1AtkType
        GloVar.P1BonusType = BTFun.attack_Bonus(
            GloVar.P1AtkType, GloVar.P2Type)


def Conversion2(player):
    print("Conversion2 Effect -> ")
    print("Changing Pokemon type to resist Rival ATk Type ->")
    if player == "P1":
        if GloVar.P2AtkType == "NORMAL" or GloVar.P2AtkType == "GRASS" or GloVar.P2AtkType == "FLYING" or GloVar.P2AtkType == "POISON" or GloVar.P2AtkType == "ROCK" or GloVar.P2AtkType == "BUG" or GloVar.P2AtkType == "PSYCHIC" or GloVar.P2AtkType == "ICE" or GloVar.P2AtkType == "DRAGON" or GloVar.P2AtkType == "STEEL" or GloVar.P2AtkType == "FAIRY":
            GloVar.P1Type = "STEEL"
            GloVar.P2BonusType = BTFun.attack_Bonus(
                GloVar.P2AtkType, GloVar.P1Type)

        elif GloVar.P2AtkType == "GRASS" or GloVar.P2AtkType == "WATER" or GloVar.P2AtkType == "GROUND" or GloVar.P2AtkType == "ELECTRIC":
            GloVar.P1Type = "STEEL"
            GloVar.P2BonusType = BTFun.attack_Bonus(
                GloVar.P2AtkType, GloVar.P1Type)
        elif GloVar.P2AtkType == "GHOST" or GloVar.P2AtkType == "DARK":
            GloVar.P1Type = "DARK"
            GloVar.P2BonusType = BTFun.attack_Bonus(
                GloVar.P2AtkType, GloVar.P1Type)
        elif GloVar.P2AtkType == "FIRE":
            GloVar.P1Type = "WATER"
            GloVar.P2BonusType = BTFun.attack_Bonus(
                GloVar.P2AtkType, GloVar.P1Type)
        elif GloVar.P2AtkType == "FIGHTING":
            GloVar.P1Type = "FLYING"
            GloVar.P2BonusType = BTFun.attack_Bonus(
                GloVar.P2AtkType, GloVar.P1Type)
    elif player == "P2":
        if GloVar.P1AtkType == "NORMAL" or GloVar.P1AtkType == "GRASS" or GloVar.P1AtkType == "FLYING" or GloVar.P1AtkType == "POISON" or GloVar.P1AtkType == "ROCK" or GloVar.P1AtkType == "BUG" or GloVar.P1AtkType == "PSYCHIC" or GloVar.P1AtkType == "ICE" or GloVar.P1AtkType == "DRAGON" or GloVar.P1AtkType == "STEEL" or GloVar.P1AtkType == "FAIRY":
            GloVar.P2Type = "STEEL"
            GloVar.P1BonusType = BTFun.attack_Bonus(
                GloVar.P1AtkType, GloVar.P2Type)

        elif GloVar.P1AtkType == "GRASS" or GloVar.P1AtkType == "WATER" or GloVar.P1AtkType == "GROUND" or GloVar.P1AtkType == "ELECTRIC":
            GloVar.P2Type = "STEEL"
            GloVar.P1BonusType = BTFun.attack_Bonus(
                GloVar.P1AtkType, GloVar.P2Type)
        elif GloVar.P1AtkType == "GHOST" or GloVar.P1AtkType == "DARK":
            GloVar.P2Type = "DARK"
            GloVar.P1BonusType = BTFun.attack_Bonus(
                GloVar.P1AtkType, GloVar.P2Type)
        elif GloVar.P1AtkType == "FIRE":
            GloVar.P2Type = "WATER"
            GloVar.P1BonusType = BTFun.attack_Bonus(
                GloVar.P1AtkType, GloVar.P2Type)
        elif GloVar.P1AtkType == "FIGHTING":
            GloVar.P1Type = "FLYING"
            GloVar.P1BonusType = BTFun.attack_Bonus(
                GloVar.P1AtkType, GloVar.P2Type)


def Counter(player):
    print("Counter effect ->")
    print("Atk Strenght = Rival Atk Strenght")
    if player == "P1":
        GloVar.P1AtkPower = GloVar.P2AtkPower
    elif player == "P2":
        GloVar.P2AtkPower = GloVar.P1AtkPower


def Covet(player):
    print("Covet Effect ->")
    print("Steal Rival attatch card")
    if player == "P1":
        if GloVar.P2Attatch != "000":
            GloVar.P1Attatch = GloVar.P2Attatch
            GloVar.P2Attatch = "000"
        else:
            print("Rival has not an AttachCard")
    elif player == "P2":
        if GloVar.P1Attatch != "000":
            GloVar.P2Attatch = GloVar.P1Attatch
            GloVar.P1Attatch = "000"
        else:
            print("Rival has not an AttachCard")


def Detect(player):
    print("Detect effect ->")
    print("Rival Atk Strenght = 0 , Rival has not effect")
    if player == "P1":
        GloVar.P2AtkPower = 0
        GloVar.P2AtkEffect = "NONE"
        GloVar. P2BonusType = 0
        GloVar.P1Status = "Normal"

    elif player == "P2":
        GloVar.P1AtkPower = 0
        GloVar.P1AtkEffect = "NONE"
        GloVar. P1BonusType = 0
        GloVar.P2Status = "Normal"


def Disable(player):
    print("Disable effect ->")
    if player == "P1":
        print("Disable Activated!!!")
        print("1.-" + GloVar.P2Atk1[1])
        print("2.-" + GloVar.P2Atk2[1])
        if GloVar.P2TM[0] != "000":
            print("3.-" + GloVar.P2TM[1])

        i = int(input("Select One move to disable :"))
        if i == 1:
            GloVar.P2Atk1 = GloVar.P2Atk2
            GloVar.P2Atk2[0] = "000"
        elif i == 2:
            GloVar.P2Atk2[0] = "000"
        elif i == 3:
            GloVar.P2TM[0] = "000"
    elif player == "P2":
        print("Disable Activated!!!")
        print("1.-" + GloVar.P1Atk1[1])
        print("2.-" + GloVar.P1Atk2[1])
        if GloVar.P1TM[0] != "000":
            print("3.-" + GloVar.P1TM[1])

        i = int(input("Select One move to disable :"))
        if i == 1:
            GloVar.P1Atk1 = GloVar.P1Atk2
            GloVar.P1Atk2 = ("000", "NULL", "NULL", 0, "NULL", "NONE", "D6")
            BTFun.selectAttack("P1")
            GloVar.Phase = 6
            return
        elif i == 2:
            GloVar.P1Atk2 = ("000", "NULL", "NULL", 0, "NULL", "NONE", "D6")
            BTFun.selectAttack("P1")
            GloVar.Phase = 6
            return
        elif i == 3:
            GloVar.P1TM = ("000", "NULL", "NULL", 0, "NULL", "NONE", "D6")
            BTFun.selectAttack("P1")
            GloVar.Phase = 6
            return


def DreamEater(player):
    print("Dream Eater Effect->")
    if player == "P1":
        if GloVar.P2Status == "Sleep":
            print("Rival is  Asleep , effect Activated + 2 ")
            GloVar.P1AtkPower = GloVar.P1AtkPower + 2
        else:
            print("Rival is not Asleep , effect Not Activated")
    elif player == "P2":
        if GloVar.P1Status == "Sleep":
            print("Rival is  Asleep , effect Activated + 2 ")
            GloVar.P2AtkPower = GloVar.P2AtkPower + 2
        else:
            print("Rival is not Asleep , effect Not Activated")


def Embargo(player):
    print("Embargo effect ->")
    print("Rival unable to use Battler and Attatch Cards")
    if player == "P1":
        GloVar.P2BattleCard = "000"
        GloVar.P2Attatch = "000"
        GloVar.P2TM = "000"
    elif player == "P2":
        GloVar.P1BattleCard = "000"
        GloVar.P1Attatch = "000"
        GloVar.P1TM = "000"


def Encore(player):
    print("Encore effect ->")
    print("Rival can only select same move during battle")
    if GloVar.Round > 0:
        print("Encore Effect Activated")
        if player == "P1":
            GloVar.P2AtkSelected = GloVar.P2PreviousAtk
        elif player == "P2":
            GloVar.P1AtkSelected = GloVar.P1PreviousAtk
    else:
        print("Encore Effect Not Activated First Round")


def Fascade(player):
    print("Fascade effect ->")
    print("If Rival has a status condition , Atk Strenght + 1")
    if player == "P1":
        if GloVar.P2Status != "Normal":
            print("Rival is" + GloVar.P2Status + " , effect Activated + 1 ")
            GloVar.P1AtkPower = GloVar.P1AtkPower + 1
        else:
            print("Rival has not staus condition, effect Not Activated")
    elif player == "P2":
        if GloVar.P1Status != "Normal":
            print("Rival is" + GloVar.P2Status + " , effect Activated + 1 ")
            GloVar.P2AtkPower = GloVar.P2AtkPower + 1
        else:
            print("Rival has not staus condition, effect Not Activated")


def FakeOut(player):
    print("FakeOut Effect->")
    if player == "P1":
        if GloVar.Round == 0:
            print("Effect Activated , rival has Disadvantage")
            GloVar.P1Effect = "Disadvantage"
        else:
            print("Effect can be activated only in first Round ")

    elif player == "P2":
        if GloVar.Round == 0:
            print("Effect Activated , rival has Disadvantage")
            GloVar.P2Effect = "Disadvantage"
        else:
            print("Effect can be activated only in first Round ")


def FireFang(player):
    print("FireFang Effect ->")
    if player == "P1":
        i = int(input("Roll Dice  Odd = Burned  , Even = Disadvantage"))
        if i == 1 or i == 3 or i == 5:
            print("Rival Burned ")
            GloVar.P2Status = "Burned"
        elif i == 2 or i == 4 or i == 6:
            print("Rival Disadvantage")
            GloVar.P1Effect = "Disadvantage"
    elif player == "P2":
        i = int(input("Roll Dice  Odd = Burned  , Even = Disadvantage"))
        if i == 1 or i == 3 or i == 5:
            print("Rival Burned ")
            GloVar.P1Status = "Burned"
        elif i == 2 or i == 4 or i == 6:
            print("Rival Disadvantage")
            GloVar.P2Effect = "Disadvantage"


def FuryCutter(player):
    print("FuryCutter Effect ->")
    print("Atk Strenght + 1 every round until the end of battle")
    if player == "P1":
        if GloVar.Round > 0:
            print("Effect ACtivated  + " + str(GloVar.Round))
            GloVar.P1AtkPower = GloVar.P1AtkPower + GloVar.Round
        else:
            print("Effect is activated after first round")

    elif player == "P2":
        if GloVar.Round > 0:
            print("Effect ACtivated  + " + str(GloVar.Round))
            GloVar.P2AtkPower = GloVar.P2AtkPower + GloVar.Round
        else:
            print("Effect is activated after first round")


def HealBell():
    print("HellBell Effect ->")
    print("Remove all status from your Pokemons")


def HiddenPower(player):
    print("Hidden Power Effect ->")

    listTypes = ["NORMAL", "GRASS", "FIRE", "WATER", "FIGHTING", "FLYING", "POISON", "GROUND",
                 "ROCK", "BUG", "GHOST", "ELECTRIC", "PSYCHIC", "ICE", "DRAGON", "DARK", "STEEL", "FAIRY"]
    N = random.randint(0, 17)
    if player == "P1":
        print("Effect Activated , Attack Type is select randomly")
        print("New type :" + listTypes[N])
        GloVar.P1AtkType = listTypes[N]
        GloVar.P1BonusType = BTFun.attack_Bonus(
            GloVar.P1AtkType, GloVar.P2Type)

    elif player == "P2":
        print("Effect ACtivated , Attack Type is select randomly")
        print("New type :" + listTypes[N])
        GloVar.P2AtkType = listTypes[N]
        GloVar.P2BonusType = BTFun.attack_Bonus(
            GloVar.P2AtkType, GloVar.P1Type)


def IceFang(player):
    print("IceFang effect ->")
    if player == "P1":
        i = int(input("Roll Dice  Odd = Frozen , Even = Disadvantage"))
        if i == 1 or i == 3 or i == 5:
            print("Rival Frozen ")
            GloVar.P2Status = "Frozen"
        elif i == 2 or i == 4 or i == 6:
            print("Rival Disadvantage")
            GloVar.P1Effect = "Disadvantage"
    elif player == "P2":
        i = int(input("Roll Dice  Odd = Frozen  , Even = Disadvantage"))
        if i == 1 or i == 3 or i == 5:
            print("Rival Frozen ")
            GloVar.P1Status = "Frozen"
        elif i == 2 or i == 4 or i == 6:
            print("Rival Disadvantage")
            GloVar.P2Effect = "Disadvantage"


def Judgement(player):
    print("Judgement effect ->")
    listTypes = ["NORMAL", "GRASS", "FIRE", "WATER", "FIGHTING", "FLYING", "POISON", "GROUND",
                 "ROCK", "BUG", "GHOST", "ELECTRIC", "PSYCHIC", "ICE", "DRAGON", "DARK", "STEEL", "FAIRY"]
    N = random.randint(0, 17)
    if player == "P1":
        i = int(input("Select one option to change Attack Type "))
        print("1.Use Same type as TM if attached")
        print("2.Roll the Type Dice")
        print("3.Choose Normal Type")
        if i == 1:
            if GloVar.P1TM != "000":
                ("Same Type as attached TM")
            else:
                ("Error ,no TM attached ")
        elif i == 2:
            print("Type select randomly ...")
            print("New type : " + listTypes[N])
            GloVar.P1AtkType = listTypes[N]
            GloVar.P1BonusType = BTFun.attack_Bonus(
                GloVar.P1AtkType, GloVar.P2Type)
        elif i == 3:
            print("Type change to Normal ")
            GloVar.P1AtkType = "Normal"
            GloVar.P1BonusType = BTFun.attack_Bonus(
                GloVar.P1AtkType, GloVar.P2Type)
    elif player == "P2":
        i = int(input("Select one option to change Attack Type "))
        print("1.Use Same type as TM if attached")
        print("2.Roll the Type Dice")
        print("3.Choose Normal Type")
        if i == 1:
            if GloVar.P2TM != "000":
                ("Same Type as attached TM")
            else:
                ("Error ,no TM attached ")
        elif i == 2:
            print("Type select randomly ...")
            print("New type : " + listTypes[N])
            GloVar.P2AtkType = listTypes[N]
            GloVar.P2BonusType = BTFun.attack_Bonus(
                GloVar.P2AtkType, GloVar.P1Type)
        elif i == 3:
            print("Type change to Normal ")
            GloVar.P2AtkType = "NORMAL"
            GloVar.P2BonusType = BTFun.attack_Bonus(
                GloVar.P2AtkType, GloVar.P1Type)


def KnockOff(player):
    print("Knock Off Effect ->")
    print("Disable Opponent Attach Cards")

    if player == "P1":
        GloVar.P2TM = "000"
        GloVar.P2Attatch = "000"

    elif player == "P2":
        GloVar.P1TM = "000"
        GloVar.P1Attatch = "000"


def MagicCoat(player):
    print("Magic Coat effect ->")
    print("Same Effect as Rival")
    if player == "P1":
        GloVar.P1AtkEffect = GloVar.P2AtkEffect

    elif player == "P2":
        GloVar.P2AtkEffect = GloVar.P1AtkEffect


def MeFirst(player):
    print("Me First effect ->")
    print("Atk Strenght = Rival Atk Strenght +1 ->")
    if player == "P1":
        GloVar.P1AtkPower = GloVar.P2AtkPower + 1

    elif player == "P2":
        GloVar.P2AtkPower = GloVar.P1AtkPower + 1


def MeanLook(player):
    print("Mean Look Effect ->")
    print("Rival can not Switch Pokemon")
    if player == "P1":
        if GloVar.P2AtkEffect == "Switch":
            GloVar.P2AtkEffect = "NONE"
    elif player == "P2":
        if GloVar.P1AtkEffect == "Switch":
            GloVar.P1AtkEffect = "NONE"


def MetalBurst(player):
    print("Metal Burst Effect ->")
    print("Atk Strenght = Rival Atk Strenght +1 ->")
    if player == "P1":
        GloVar.P1AtkPower = GloVar.P2AtkPower + 1

    elif player == "P2":
        GloVar.P2AtkPower = GloVar.P1AtkPower + 1


def Metronome(player):
    print("Metronome effect ->")
    print("First attack from random pokemon with same color")
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
            atk = BTFun.getAttack(pokemon[5])
            if player == "P1":
                GloVar.P1AtkSelID = atk[0]
                GloVar.P1AtkSelected = atk[1]
                GloVar.P1AtkType = atk[2]
                GloVar.P1AtkPower = atk[3]
                GloVar.P1AtkEffect = atk[4]
                GloVar.P1EffectActivate = atk[5]
                GloVar.P1DiceType = atk[6]
                GloVar.P1BonusType = BTFun.attack_Bonus(
                    GloVar.P1AtkType, GloVar.P2Type)
                print("Attack Selected :" + GloVar.P1AtkSelected)
            elif player == "P2":
                GloVar.P2AtkSelID = atk[0]
                GloVar.P2AtkSelected = atk[1]
                GloVar.P2AtkType = atk[2]
                GloVar.P2AtkPower = atk[3]
                GloVar.P2AtkEffect = atk[4]
                GloVar.P2EffectActivate = atk[5]
                GloVar.P2DiceType = atk[6]
                GloVar.P2BonusType = BTFun.attack_Bonus(
                    GloVar.P2AtkType, GloVar.P1Type)
                print("Attack Selected :" + GloVar.P2AtkSelected)


def Mimic(player):
    print("Mimic Effect ->")
    print("Same move as previous Rival Move")
    if player == "P1":
        if GloVar.P2PreviousAtk != "000":
            BTFun.getAttackWithID(player, GloVar.P2PreviousAtk)
        else:
            print("Attack With not effect")
    elif player == "P2":
        if GloVar.P1PreviousAtk != "000":
            BTFun.getAttackWithID(player, GloVar.P1PreviousAtk)
        else:
            print("Attack With not effect")


def MirrorCoat(player):
    print("Mirror Coat")
    print("Atk Strenght = Rival Atk Strenght ")
    if player == "P1":
        GloVar.P1AtkPower = GloVar.P2AtkPower
    elif player == "P2":
        GloVar.P2AtkPower = GloVar.P1AtkPower


def MirrorMove(player):
    print("Mirror Move Effect ->")
    print("Atk Effect and Type   = Rival Atk Effect and Type ")
    if player == "P1":
        if GloVar.P2AtkEffect != "MirrorMove":
            BTFun.getAttackWithID(player, GloVar.P2AtkSelID)
            print("Attack P1 = " + GloVar.P1AtkSelected)
        else:
            print("Unable to use Mirror move if Rival use Mirror Move")
    elif player == "P2":
        if GloVar.P1AtkEffect != "MirrorMove":
            BTFun.getAttackWithID(player, GloVar.P1AtkSelID)
            print("Attack P2 = " + GloVar.P2AtkSelected)
        else:
            print("Unable to use Mirror move if Rival use Mirror Move")


def Mist(player):
    print("Mist Effect")
    print("Unnafected by Disadvantage")
    if player == "P1":
        if GloVar.P2AtkEffect == "Disadvantage" or GloVar.P2AtkEffect == "DoubleDisadvantage":
            GloVar.P2AtkEffect == "NONE"
    elif player == "P2":
        if GloVar.P1AtkEffect == "Disadvantage" or GloVar.P1AtkEffect == "DoubleDisadvantage":
            GloVar.P1AtkEffect == "NONE"


def PayDay():
    print("Pay Day Effect ->")
    print("Take one Item Card")


def PayBack(player):
    print("PayBack Effect ->")
    print("Atk Strength +1 for each Rival Battle Card or Attach Card")
    if player == "P1":
        if GloVar.P2BattleCard != "000":
            print(" Atk +1 due to Battle Card")
            GloVar.P1AtkPower = GloVar.P1AtkPower + 1
        if GloVar.P2Attatch != "000":
            print(" Atk +1 due to Attach Card")
            GloVar.P1AtkPower = GloVar.P1AtkPower + 1
    if player == "P2":
        if GloVar.P1BattleCard != "000":
            print(" Atk +1 due to Battle Card")
            GloVar.P2AtkPower = GloVar.P2AtkPower + 1
        if GloVar.P1Attatch != "000":
            print(" Atk +1 due to Attach Card")
            GloVar.P2AtkPower = GloVar.P2AtkPower + 1


def Protect(player):
    print("Protect Effect ->")
    print("Rival Attack Strenght =0  and Rival has not Effect")
    if player == "P1":
        GloVar.P2AtkPower = 0
        GloVar.P2AtkEffect = "NONE"
        GloVar.P2BonusType = 0
        GloVar.P2DiceType = "D6"
    if player == "P2":
        GloVar.P1AtkPower = 0
        GloVar.P1AtkEffect = "NONE"
        GloVar.P1BonusType = 0
        GloVar.P1DiceType = "D6"


def RolloOut(player):
    print("RollOut Effect ->")
    print("Atk +1 for each round")
    if player == "P1":
        GloVar.P1AtkPower = GloVar.P1AtkPower + GloVar.Round
    elif player == "P2":
        GloVar.P2AtkPower = GloVar.P2AtkPower + GloVar.Round


def PlusRound(player):
    print("PlusRound Effect ->")
    print("Atk +1 for each round")
    if player == "P1":
        GloVar.P1AtkPower = GloVar.P1AtkPower + GloVar.Round
    elif player == "P2":
        GloVar.P2AtkPower = GloVar.P2AtkPower + GloVar.Round


def SafeGuard(player):
    print("SafeGuard Effect -> ")
    print("Pokemon can not gaint any status ")
    if player == "P1":
        GloVar.P1Status = "Normal"
    elif player == "P1":
        GloVar.P1Status = "Normal"


def QuickAttack(player):
    print("Quick Attack -> ")
    print("Pokemon can not gain any status ")
    if player == "P1":
        GloVar.P1Status = "Normal"
    elif player == "P1":
        GloVar.P1Status = "Normal"


def SecretPower(player):
    print("Secret Power Effect")
    print("Roll Dice Again")
    if player == "P1":
        i = int(input("# Dice : "))
        if i == 1:
            print("Rival is now Paralyzed")
            GloVar.P2Status = "Paralyzed"
        elif i == 2:
            print("Rival gains  Disadvantage")
            GloVar.P1Effect = "Disadvantage"
        if i == 3:
            print("Rival is now Confused")
            GloVar.P2Status = "Confused"
        if i == 4:
            print("Rival is now Poisoned")
            GloVar.P2Status = "Poisoned"
        if i == 1:
            print("Rival is now Asleep")
            GloVar.P2Status = "Asleep"
        if i == 1:
            print("User gain Advantage")
            GloVar.P1Effect = "Paralyzed"
    elif player == "P2":
        i = int(input("# Dice : "))
        if i == 1:
            print("Rival is now Paralyzed")
            GloVar.P1Status = "Paralyzed"
        elif i == 2:
            print("Rival gains  Disadvantage")
            GloVar.P2Effect = "Disadvantage"
        if i == 3:
            print("Rival is now Confused")
            GloVar.P1Status = "Confused"
        if i == 4:
            print("Rival is now Poisoned")
            GloVar.P1Status = "Poisoned"
        if i == 1:
            print("Rival is now Asleep")
            GloVar.P1Status = "Asleep"
        if i == 1:
            print("User gain Advantage")
            GloVar.P2Effect = "Paralyzed"


def Taunt(player):
    print("Taunt effect activated")


def StealthRock(player):
    print("Effect not ready")


def Transform(player):
    print("Pending")


def Sketch(player):
    print("Pending")


def NoItems(player):
    print("pending")


def Thief(player):
    print("pending")


def TriAttack(player):
    print("Pending")


def ThunderFang(player):
    print("ThunderFang Effect ->")
    if player == "P1":
        i = int(input("Roll Dice  Odd = Paralized  , Even = Disadvantage"))
        if i == 1 or i == 3 or i == 5:
            print("Rival Paralized ")
            GloVar.P2Status = "Paralized"
        elif i == 2 or i == 4 or i == 6:
            print("Rival Disadvantage")
            GloVar.P1Effect = "Disadvantage"
    elif player == "P2":
        i = int(input("Roll Dice  Odd = Paralized  , Even = Disadvantage"))
        if i == 1 or i == 3 or i == 5:
            print("Rival Paralized ")
            GloVar.P1Status = "Paralized"
        elif i == 2 or i == 4 or i == 6:
            print("Rival Disadvantage")
            GloVar.P2Effect = "Disadvantage"
