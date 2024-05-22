

def get_float() -> float:

    while True:
        ui = input("Bitte gebe ein Zahl ein: ")
        try:
            return float(ui)
        except ValueError as e:
            print(e)
    
print(get_float())