from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
start = uic.loadUi("start.ui")
battle = uic.loadUi("battle.ui")


def star_game():
    start.hide()
    battle.show()


start.startButton.clicked.connect(star_game)

battle.steps.setText("Player 1 select a Pokemon")
battle.Pkm1.setText("Rapidash!!!")
battle.Pkm2.setText("Charizard")
app.exec()
