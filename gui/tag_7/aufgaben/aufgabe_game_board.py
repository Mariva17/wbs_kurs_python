"""
Aufgabe: Board Game (schwer)

Erstelle ein 10 x 10 Grid mit Cell-Objekten.
Bei Klick auf ein Cell-Objekt wechselt die Farbe von schwarz nach rot und
umgekehrt (toggle). Die Initialfarbe einer Zelle ist grau. Der Wechsel von Grau
nach Schwarz findet am Anfang und genau einmal statt.

Erstelle dafür eine Klasse Cell, die in einem der folgenden Zustände sein kann:
- grey (initial)
- rot
- schwarz

Die Matrix ist immer eine Quadratmatrix, kann allerdings in der Größe
variieren. Die Gestaltung des Programms muss das berücksichtigen.

Tipp:
Um die Klicks auf die Zellen zu implementieren, nutze bind(), z.b. mit
LabelWidgets.

for row i / for column j:
element.bind(
     "<Button-1>",
     lambda event, i=i, j=j: self.on_click_cell(i, j, event),
)


Die Logik muss von der Darstellung getrennt sein, d.h. das Erstellen des Boards
und der Zugriff auf die Zellobjekte muss unabhängig von der GUI möglich sein.

# Toggle Test
test_board = create_board(size=4)
cell = test_board[0][0]
print(cell.state)  # grey (initial state)
cell.toggle_state() # change from grey to black
print(cell.state) # black
cell.toggle_state() # toggle from black to red
print(cell.state) # red
cell.toggle_state() # toggle from red to black

(siehe Bild game_board.png)
"""
