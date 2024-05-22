"""
Programm-Loop

"""
# Mini-Programm (z.b. Taschenrechner)
while True:
    user_input = input("Please enter a word: ")
    print(user_input)

    if user_input in ["quit", "end", "q"]:
        print("Goodbye!")
        break


# Aufgabe: Fahrenheit Umrechner. User Gibt Grad Celsius ein. 
# Ausgabe soll Grad Fahrenheit sein
# fahrenheit = (celcius * 9 / 5) + 32

while True:
    user_input = input("Bitte geben Sie Grad Celsius ein : ")
    if user_input.replace(".", "").isdigit():
        user_input_fahrenheit = (float(user_input) * 9 / 5) + 32
        print("Grad Fahrenheit: ", user_input_fahrenheit)

    elif user_input in ["quit", "end", "q"]:
        print("Goodbye!")
        break
    else:
        print("Ungültige Eingabe")


# via Steffen

BREAK_WORDS = ["quit", "q", "end", "ende"]

print("Fahrenheit Umrechner.")
print("Beenden mit:", ", ".join(map(repr, BREAK_WORDS)))
while True:
    ui = input("Geben Sie einen Wert in Grad Celsius an: ")

    if ui in BREAK_WORDS:
        break

    try:
        celsius = float(ui)
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl an.")
        continue

    fahrenheit = (celsius * 9 / 5) + 32
    print( f"{celsius} °C entsprechen {fahrenheit} °F.\n" )

print("Auf Wiedersehen.")



