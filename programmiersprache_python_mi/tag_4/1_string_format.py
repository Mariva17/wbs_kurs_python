

"""
String Formatierung

https://peps.python.org/pep-0008/
"""

x = 3
y = 9
# unschöne Formatierung
print("Peter hat", x, "Äpfel")
print("Peter hat " + str(x) + " Äpfel")

# besser mit Format-String
temp = f"Peter hat {x} Äpfel und {y} Fahrräder" # f steht für Formatierung
print(temp)

# öder mit format-Methode
temp = "Peter hat {} Äpfel und {} Fahrräder".format(x, y)
print(temp)

# mehrzeiliger String
m = """hallo
welt
xyz"""
print(m)


name = "Anna"
alter = 25
stadt = "Berlin"
familienstand ="Geschieden"
kinder = 2
template = "Mein Name ist {}, und ich bin {} Jahre alt. Ich wohne in {}."\
            "Ich bin {}. Ich habe {} Kinder."

template = (
    "Mein Name ist {}, und ich bin {} Jahre alt. Ich wohne in {}."\
    "Ich bin {}. Ich habe {} Kinder."
)

print(template.format(name,
                      alter,
                      stadt,
                      familienstand,
                      kinder))