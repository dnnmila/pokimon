def init():
    global P1, P1Level, P1Type, P1Atk1, P1Atk2, P1TM, P1Extra, P1Attatch
    global P2, P2Level, P2Type, P2Atk1, P2Atk2, P2TM, P2Extra, P2Attatch
    global P1AtkSelID, P1AtkSelected, P1AtkType, P1AtkPower, P1AtkEffect, P1EffectActivate, P1DiceType, P1AtkChoosen
    global P2AtkSelID, P2AtkSelected, P2AtkType, P2AtkPower, P2AtkEffect, P2EffectActivate, P2DiceType, P2AtkChoosen
    global P1BonusType, P1Status, P1Effect, P1Dice, P1PreviousAtk, P2BonusType, P2Status, P2Effect, P2Dice, P2PreviousAtk
    global BattleFinish, Turn, Round, Phase
    global P1BattleCard, P2BattleCard
    Phase = 0
    BattleFinish = False
    Round = 0
    P1BonusType = 0
    P2BonusType = 0
    P1Status = "Normal"
    P2Status = "Normal"
    P1Effect = "None"
    P2Effect = "None"
    P1Dice = 0
    P2Dice = 0
    P1PreviousAtk = "000"
    P2PreviousAtk = "000"
    P1BattleCard = "000"
    P2BattleCard = "000"
    P1AtkEffect = "None"
    P2AtkEffect = "None"
    P1EffectActivate = "NONE"
    P1DiceType = "D6"
    P2EffectActivate = "NONE"
    P2DiceType = "D6"
    P2AtkPower = 0
    P1AtkChoosen = 0
    P2AtkChoosen = 0
