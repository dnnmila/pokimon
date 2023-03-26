
import GloVar
import BTFun
import time
import serial

arduino = serial.Serial(port="COM3", baudrate=9600)
time.sleep(2)
GloVar.init()


basura = BTFun.readSerialUntil(arduino)
print(basura)
basura = BTFun.readSerialUntil(arduino)
print(basura)

if __name__ == '__main__':

    while (GloVar.BattleFinish != True):
       # P1 select Pokemon
        if GloVar.Phase == 0:
            BTFun.resetNewBattle()
            Player = "P1"
            print("P1 Select")
            BTFun.sendToArduino("READ", arduino)
            BTFun.selectPokemon(Player, arduino)
            print("Pokemon Selected: " + GloVar.P1)
            GloVar.Phase = 1

        # P2 select Pokemon
        elif GloVar.Phase == 1:
            Player = "P2"
            print("\nP2 Select")
            BTFun.sendToArduino("READ", arduino)
            BTFun.selectPokemon(Player, arduino)
            print("Pokemon Selected: " + GloVar.P2)
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
            BTFun.disableBeforeSelectAttack(Player)
            if GloVar.Phase == 6:
                pass
            else:

                BTFun.selectAttack(Player, arduino)
                print(GloVar.P1AtkSelected)
                time.sleep(.100)
                GloVar.Phase = 5

        # P2 select attack
        elif GloVar.Phase == 5:
            print("\n Phase 5->")
            Player = "P2"
            BTFun.selectAttack(Player, arduino)
            print(GloVar.P2AtkSelected)
            time.sleep(.100)
            GloVar.Phase = 6

        # P1 effect
        elif GloVar.Phase == 6:

            print("\n Phase 6: ->Effect P1")
            Player = "P1"
            BTFun.activateEffect(Player, arduino)
            if GloVar.P2Status == "Frozen" or GloVar.P2Status == "Sleep" or GloVar.P2Status == "Paralized":
                GloVar.Phase = 7
            else:
                GloVar.Phase = 8

            # verify status P2 and attack
        elif GloVar.Phase == 7:
            Player = "P2"
            print("\n Phase 7: -> P2 affected")
            GloVar.P2Status = BTFun.removeStatus(Player, arduino)
            # If no attack P2
            if GloVar.P2Status == "Frozen" or GloVar.P2Status == "Sleep" or GloVar.P2Status == "Paralized":
                GloVar.P2AtkPower = 0
                GloVar.P2BonusType = 0
                GloVar.Phase = 10
            else:
                GloVar.Phase = 8

        elif GloVar.Phase == 8:
            print("Efecto 2: " + GloVar.P2AtkEffect)
            print("\n Phase 8: ->Effect P2")
            Player = "P2"
            if GloVar.P2AtkEffect != "Disable":
                BTFun.activateEffect(Player, arduino)
                if GloVar.P1Status == "Frozen" or GloVar.P1Status == "Sleep" or GloVar.P1Status == "Paralized":
                    GloVar.Phase = 9
                else:
                    GloVar.Phase = 10
            else:
                GloVar.Phase = 10

        # Verify status P1
        elif GloVar.Phase == 9:
            BTFun.activateEffect(Player, arduino)
            print("\n Phase 9: -> P1 affected")
            Player = "P1"
            GloVar.P1Status = BTFun.removeStatus(Player, arduino)
            # if No attack P1
            if GloVar.P1Status == "Frozen" or GloVar.P1Status == "Sleep" or GloVar.P1Status == "Paralized":
                GloVar.P1AtkPower = 0
                GloVar.P1BonusType = 0
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
            time.sleep(.100)
            # BTFun.debugprint()
            GloVar.Phase = 11

        elif GloVar.Phase == 11:
            # P1 Throw Dice
            print("\n Phase 11: -> P1 Throw dice")
           # print("\n Player1 Status -> " + GloVar.P1Status +
            #      " Player1 Effect -> " + GloVar.P1Effect)
            Player = "P1"
            BTFun.rollDicesEffect(Player, arduino)
            print(GloVar.P1Dice)
            time.sleep(.100)

            GloVar.Phase = 12

        elif GloVar.Phase == 12:
            print("\n Phase 12: -> P2 Throw dice")
            # print("\n Player2 Status-> " + GloVar.P2Status +
            #      " Player2 Effect -> " + GloVar.P2Effect)
            Player = "P2"
            BTFun.rollDicesEffect(Player, arduino)
            print(GloVar.P2Dice)
            time.sleep(.100)

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
            print(GloVar.P1+" Total : " + str(GloVar.TotalP1))
            print(GloVar.P2 + "Total : " + str(GloVar.TotalP2))
            GloVar.Phase = 16

        elif GloVar.Phase == 16:
            print("\n Phase 16")
            if GloVar.TotalP1 > GloVar.TotalP2:
                print("Winner is :" + GloVar.P1)
                time.sleep(2)
                GloVar.Phase = 17
            elif GloVar.TotalP1 < GloVar.TotalP2:
                print("Winner is :" + GloVar.P2)
                time.sleep(2)
                GloVar.Phase = 17
            elif GloVar.TotalP1 == GloVar.TotalP2:
                GloVar.Round = GloVar.Round + 1
                print("DRAW!, Ready for round " + str(GloVar.Round))
                BTFun.resetNewRound()
                time.sleep(2)
                GloVar.Phase = 4

        elif GloVar.Phase == 17:
            print("Done!")
            # BTFun.sendToArduino("READ", arduino)
            # BTFun.addLevel(arduino)
            GloVar.Phase = 0
