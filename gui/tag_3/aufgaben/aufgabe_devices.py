"""schwer

Aufgabe: Entwicklung eines Steuerungssystems für Elektrogeräte

Ziel:
Implementiere ein Python-Programm, das verschiedene Elektrogeräte
durch Vererbung verwaltet und die Interaktion mit diesen Geräten
ermöglicht.

Anforderungen:
1. Basisklasse:
   - Definiere eine Basisklasse `ElectronicDevice` mit den Attributen
     `power_status` (an/aus) und Methoden zum Einschalten (`turn_on`)
     und Ausschalten (`turn_off`).

2. Abgeleitete Klassen:
   - Entwickle zwei abgeleitete Klassen: `Television` und `Radio`.
   - `Television` hat zusätzliche Methoden zum Wechseln des Kanals
     (`change_channel`) und zur Anpassung der Lautstärke (`adjust_volume`).
   - `Radio` hat Methoden zum Wechseln der Frequenz (`tune_frequency`)
     und zur Anpassung der Lautstärke, ähnlich wie beim Fernseher.

3. Interaktives Script:
   - Erstelle ein interaktives Python-Script, das den Benutzer die
     Geräte einschalten, Einstellungen anpassen und wieder ausschalten
     lässt.
   - Benutze die Konsole zur Eingabe der Befehle und zur Ausgabe der
     Gerätestatus.
Enter your choice (enter help for options): help

    Options:
    1. Turn on TV
    2. Turn off TV
    3. Change TV channel
    4. Adjust TV volume
    5. Turn on Radio
    6. Turn off Radio
    7. Tune Radio frequency
    8. Adjust Radio volume
    9. Exit

Enter your choice (enter help for options): 3
Please turn on the TV first.
Enter your choice (enter help for options): 1
Television is now on.
Enter your choice (enter help for options): 3
Enter the volume level: 23
Volume is set to 23.
Enter your choice (enter help for options): 5
Radio is now on.
Enter your choice (enter help for options): 7
Enter the frequency (MHz): 78.2
Frequency tuned to 78.2 MHz.
Enter your choice (enter help for options): 9
Exiting the controller. All devices are shut down.

"""
import enum  



class PowerStatus(enum.StrEnum):
  ON = "on"
  OFF = "off"



class ElectronicDevice:
  def __init__(self):
    self.power_status = PowerStatus.OFF
  
  def turn_on(self):
    self.power_status = PowerStatus.ON
    print(f"{self.__class__.__name__} is now {self.power_status}")

  def turn_off(self):
    self.power_status = PowerStatus.OFF
    print(f"{self.__class__.__name__} is now {self.power_status}")

 

class Television(ElectronicDevice):

  def __init__(self):
    super().__init__()
    self.channel = 1
    self.volume = 10

  
  def change_channel(self, channel):
    if self.power_status == PowerStatus.ON:
      self.channel = channel
      print(f"Channel has been changed to {self.channel}.")
    else:
      print("Please turn on the TV first.")

  def adjust_volume(self, volume):
    if self.power_status == PowerStatus.ON:
      self.volume = volume
      print(f"Volume is set to {self.volume}.")
    else:
      print("Please turn on the TV first.")


class Radio(ElectronicDevice):
  def __init__(self):
    super().__init__()
    self.frequency = 98.2  # MHz

  def tune_frequency(self, frequency):
    if self.power_status == PowerStatus.ON:
      self.frequency = frequency
      print(f"Frequency tuned to {self.frequency} MHz.")
    else:
      print("Please turn on the radio first.")

  def adjust_volume(self, volume):
    if self.power_status == PowerStatus.ON:
      self.volume = volume
      print(f"Volume is set to {self.volume}.")
    else:
      print("Please turn on the radio first.")


def controller(options_menu, devices):
  """The main controller function."""

  tv = devices["tv"]
  radio = devices["radio"]

  while True:
    choice = input("Enter your choice (enter help for options): ").lower()

    match choice:
      case "help":
        print(options_menu)
      case "1":
        tv.turn_on()
      case "2":
        tv.turn_off()
      case "3" | "4":
        if tv.power_status == PowerStatus.OFF:
          print("Please turn on the TV first.")
        elif choice == "3":
          channel = int(input("Enter the channel number: "))
          tv.change_channel(channel)
        elif choice =="4":
          volume = int(input("Enter the volume level: "))
          tv.adjust_volume(volume)
      case "5":
        radio.turn_on()
      case "6":
        radio.turn_off()
      case "7" | "8":
        if radio.power_status == PowerStatus.OFF:
          print("Please turn on the radio first.")
        elif choice == "7":
          frequency = float(input("Enter the frequency (MHz): "))
          radio.tune_frequency(frequency)
        elif choice == "8":
          volume = int(input("Enter the volume level: "))
          radio.adjust_volume(volume)
      case "9":
        print("Exit!")
        exit(0)
      case _:
        print("Invalid choice. Please choose again.")



def main():
  tv = Television()
  radio = Radio()

  options_menu = """Options:
    1. Turn on TV
    2. Turn off TV
    3. Change TV channel
    4. Adjust TV volume
    5. Turn on Radio
    6. Turn off Radio
    7. Tune Radio frequency
    8. Adjust Radio volume
    9. Exit
    """ 
  controller(options_menu, devices={"tv": tv, "radio": radio})


if __name__ == "__main__":
  main()
