import sys

# 3 vordefinierte Streams
sys.stdout.write("hallo welt")  # STandard-out
sys.stderr.write("das ist ein fehler")  # Stanard-Error
sys.stdin.read()  # Standard-Input

# Text-Datei öffnen
with open("readme.md", mode="r") as f:
    f.read()

# Bild-Datei öffnen
with open("image.png", mode="rb") as f:
    f.read()
