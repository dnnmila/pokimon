import sqlite3
import GloVar
import BTFun
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
start = uic.loadUi("start.ui")
battle = uic.loadUi("battle.ui")


def hide_battle():
    battle.Pkm1.hide()
    battle.Pkm2.hide()
    battle.Level1.hide()
    battle.Level2.hide()
    battle.Type1.hide()
    battle.Type2.hide()
    battle.P1Atk1.hide()
    battle.P1Atk2.hide()
    battle.P1TM.hide()
    battle.P2Atk1.hide()
    battle.P2Atk2.hide()
    battle.P2TM.hide()
    battle.P1Atk1_B.hide()
    battle.P1Atk2_B.hide()
    battle.P1TM_B.hide()
    battle.P2Atk1_B.hide()
    battle.P2Atk2_B.hide()
    battle.P2TM_B.hide()
    battle.Extra1.hide()
    battle.Extra2.hide()
    battle.AtkSelected1.hide()
    battle.AtkSelected2.hide()
    battle.Effect1.hide()
    battle.Effect2.hide()
    battle.Status1.hide()
    battle.Status2.hide()
    battle.AtkPower1.hide()
    battle.AtkPower2.hide()


def showpkm(player):
    if player == "P1":
        battle.Pkm1.setText(GloVar.P1)
        battle.Level1.setText(str(GloVar.P1Level))
        battle.Extra1.setText("Extra: " + str(GloVar.P1Extra))
        battle.Type1.setText(GloVar.P1Type)
        battle.P1Atk1.setText(GloVar.P1Atk1[1] + ": " + str(GloVar.P1Atk1[3]))
        battle.P1Atk2.setText(GloVar.P1Atk2[1] + ": " + str(GloVar.P1Atk2[3]))
        battle.P1TM.setText(GloVar.P1TM[1])
        battle.total1.setText(str(GloVar.Total1))
        battle.Pkm1.show()
        battle.Level1.show()
        battle.Type1.show()

        if GloVar.P1Extra > 0:
            battle.Extra1.show()

    elif player == "P2":
        battle.Pkm2.setText(GloVar.P2)
        battle.Level2.setText(str(GloVar.P2Level))
        battle.Extra2.setText("Extra: " + str(GloVar.P2Extra))
        battle.Type2.setText(GloVar.P2Type)
        battle.P2Atk1.setText(GloVar.P2Atk1[1] + ": " + str(GloVar.P2Atk1[3]))
        battle.P2Atk2.setText(GloVar.P2Atk2[1] + ": " + str(GloVar.P2Atk2[3]))
        battle.P2TM.setText(GloVar.P2TM[1])
        battle.total2.setText(str(GloVar.Total2))
        battle.Pkm2.show()
        battle.Level2.show()
        battle.Type2.show()

        if GloVar.P2Extra > 0:
            battle.Extra2.show()


def showAttack(player):
    if player == "P1":
        battle.P1Atk1.hide()
        battle.P1Atk2.hide()
        battle.P1TM.hide()
        battle.P1Atk1_B.hide()
        battle.P1Atk2_B.hide()
        battle.P1TM_B.hide()
        battle.AtkSelected1.setText(GloVar.P1AtkSelected)
        battle.AtkPower1.setText(str(GloVar.P1AtkPower))
        battle.Effect1.setText(GloVar.P1AtkEffect)
        battle.AtkSelected1.show()
        battle.AtkPower1.show()
        battle.Effect1.show()
    elif player == "P2":
        battle.P2Atk1.hide()
        battle.P2Atk2.hide()
        battle.P2TM.hide()
        battle.P2Atk1_B.hide()
        battle.P2Atk2_B.hide()
        battle.P2TM_B.hide()
        battle.AtkSelected2.setText(GloVar.P2AtkSelected)
        battle.AtkPower2.setText(str(GloVar.P2AtkPower))
        battle.Effect2.setText(GloVar.P2AtkEffect)
        battle.AtkSelected2.show()
        battle.AtkPower2.show()
        battle.Effect2.show()


GloVar.init()
GloVar.Phase = 0

if __name__ == '__main__':

    while (GloVar.BattleFinish != True):
       # P1 select Pokemon
        if GloVar.Phase == 0:
            battle.show()

            Player = "P1"
            print("P1 Select")
            hide_battle()
            battle.steps.setText("Player 1 select a Pokemon")
            BTFun.selectPokemon(Player)
            print("Pokemon Selected: " + GloVar.P1)
            GloVar.Total1 = GloVar.P1Level + GloVar.P1Extra
            showpkm(Player)
            GloVar.Phase = 1

        # P2 select Pokemon
        elif GloVar.Phase == 1:
            Player = "P2"
            print("\nP2 Select")
            battle.steps.setText("Player 2 select a Pokemon")

            BTFun.selectPokemon(Player)
            print("Pokemon Selected: " + GloVar.P2)
            GloVar.Total2 = GloVar.P2Level + GloVar.P2Extra
            showpkm(Player)
            GloVar.Phase = 2

        # P1 add Battle Card
        elif GloVar.Phase == 2:
            Player = "P1"
            print("P1 add Battle card?")
            GloVar.Phase = 3

        # P2 add Battle Card
        elif GloVar.Phase == 3:
            Player = "P2"
            print("P2 add Battle card?")
            GloVar.Phase = 4

        # P1 select Attack
        elif GloVar.Phase == 4:
            print("\n Phase 4->")
            Player = "P1"
            BTFun.effectBeforeSelectAttack(Player)
            battle.steps.setText("Player 1 select Attack")
            BTFun.selectAttack(Player, battle)
            print(GloVar.P1AtkSelected)
            showAttack(Player)

            GloVar.Total1 = GloVar.Total1 + GloVar.P1AtkPower + GloVar.P1BonusType
            battle.total1.setText(str(GloVar.Total1))
            showAttack(Player)
            GloVar.Phase = 5

        # P2 select attack
        elif GloVar.Phase == 5:
            print("\n Phase 5->")
            battle.steps.setText("Player 2 select Attack")
            Player = "P2"
            BTFun.selectAttack(Player, battle)
            print(GloVar.P2AtkSelected)
            showAttack(Player)
            GloVar.Total2 = GloVar.Total2 + GloVar.P2AtkPower + GloVar.P2BonusType
            battle.total2.setText(str(GloVar.Total2))
            GloVar.Phase = 6

        # P1 effect
        elif GloVar.Phase == 6:
            print("\n Phase 6: ->Effect P1")
            Player = "P1"

            BTFun.activateEffect(Player, battle)
            if GloVar.P2Status != "Normal":
                battle.Status2.setText(GloVar.P2Status)
                battle.Status2.show()
            if GloVar.P2Status == "Frozen" or GloVar.P2Status == "Sleep" or GloVar.P2Status == "Paralized":
                GloVar.Phase = 7
            else:
                GloVar.Phase = 8

            # verify status P2 and attack
        elif GloVar.Phase == 7:
            Player = "P2"
            print("\n Phase 7: -> P2 affected")
            GloVar.P2Status = BTFun.removeStatus(Player, battle)
            if GloVar.P2Status == "Normal":
                battle.Status2.hide()
            # If no attack P2
            if GloVar.P2Status == "Frozen" or GloVar.P2Status == "Sleep" or GloVar.P2Status == "Paralized":
                GloVar.P2AtkPower = 0
                GloVar.P2BonusType = 0
                GloVar.Total2 = GloVar.P2Level + GloVar.P2Extra
                battle.total2.setText(str(GloVar.Total2))
                GloVar.Phase = 10
            else:
                GloVar.Phase = 8

        elif GloVar.Phase == 8:
            print("\n Phase 8: ->Effect P2")
            Player = "P2"
            BTFun.activateEffect(Player, battle)
            if GloVar.P1Status != "Normal":
                battle.Status1.setText(GloVar.P1Status)
                battle.Status1.show()
            if GloVar.P1Status == "Frozen" or GloVar.P1Status == "Sleep" or GloVar.P1Status == "Paralized":
                GloVar.Phase = 9
            else:
                GloVar.Phase = 10

        # Verify status P1
        elif GloVar.Phase == 9:
            BTFun.activateEffect(Player, battle)
            print("\n Phase 9: -> P1 affected")
            Player = "P1"
            GloVar.P1Status = BTFun.removeStatus(Player, battle)
            # if No attack P1
            if GloVar.P1Status == "Frozen" or GloVar.P1Status == "Sleep" or GloVar.P1Status == "Paralized":
                GloVar.P1AtkPower = 0
                GloVar.P1BonusType = 0
                GloVar.Total1 = GloVar.P1Level + GloVar.P1Extra
                battle.total1.setText(str(GloVar.Total1))
                GloVar.Phase = 10
            else:
                GloVar.Phase = 10

        elif GloVar.Phase == 10:
            # Check effect from advantage or disadvantages
            BTFun.advantages("P1")
            BTFun.advantages("P2")
            # Sum partial from atacks and effecs activated
            print("\n Phase 10: ->Total Parcial")
            print("Total Parcial ")
            BTFun.sumPartial()
            battle.total1.setText(str(GloVar.Total1))
            battle.total2.setText(str(GloVar.Total2))
            # BTFun.debugprint()
            GloVar.Phase = 11

        elif GloVar.Phase == 11:
            # P1 Throw Dice
            print("\n Phase 11: -> P1 Throw dice")
            battle.steps.setText("Player 1 Throw dice")

           # print("\n Player1 Status -> " + GloVar.P1Status +
            #      " Player1 Effect -> " + GloVar.P1Effect)
            Player = "P1"
            BTFun.rollDicesEffect(Player, battle)
            print(GloVar.P1Dice)
            battle.total1.setText(str(GloVar.Total1))
            battle.total2.setText(str(GloVar.Total2))
            GloVar.Phase = 12

        elif GloVar.Phase == 12:
            print("\n Phase 12: -> P2 Throw dice")
            battle.steps.setText("Player 2 Throw dice")

            # print("\n Player2 Status-> " + GloVar.P2Status +
            #      " Player2 Effect -> " + GloVar.P2Effect)
            Player = "P2"
            BTFun.rollDicesEffect(Player, battle)
            print(GloVar.P2Dice)
            battle.total1.setText(str(GloVar.Total1))
            battle.total2.setText(str(GloVar.Total2))

            GloVar.Phase = 13
        elif GloVar.Phase == 13:
            print("\nPhase 13 Activate card P1?")
            GloVar.TotalP1 = GloVar.TotalP1 + GloVar.P1Dice
            GloVar.Phase = 14

        elif GloVar.Phase == 14:
            print("\nPhase 14 Activate card P2?")
            GloVar.TotalP2 = GloVar.TotalP2 + GloVar.P2Dice
            GloVar.Phase = 15

        elif GloVar.Phase == 15:
            print("\n Phase 15: ->Total Final")
            battle.total1.setText(str(GloVar.TotalP1))
            battle.total2.setText(str(GloVar.TotalP2))
            print(GloVar.P1+" Total : " + str(GloVar.TotalP1))
            print(GloVar.P2 + "Total : " + str(GloVar.TotalP2))

            GloVar.Phase = 16

        elif GloVar.Phase == 16:
            print("\n Phase 16")
            if GloVar.TotalP1 > GloVar.TotalP2:
                battle.steps.setText(GloVar.P1 + " Win!!!")

            elif GloVar.TotalP1 < GloVar.TotalP2:
                battle.steps.setText(GloVar.P2 + " Win!!!")
            elif GloVar.TotalP1 == GloVar.TotalP2:
                battle.steps.setText(" DRAAAWWWW")

            # BTFun.debugprint()
            GloVar.Phase = 17
        elif GloVar.Phase == 17:
            pass
