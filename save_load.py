# Import modules from other subfolders
import os

# Config:
import config as c

# Save system:
def save_data():
    # Path of the file:
    path = "resources/data/file.txt"

    # Make sure the file exists:
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Save function:
    with open(path, "w") as file:
        file.write(f"Music={c.VOLUME_MUSIC}\n")
        file.write(f"SFX={c.VOLUME_SFX}\n")

# Load system:
def load_data():
    # Path of the file:
    path = "resources/data/file.txt"
    
    # Load function:
    if not os.path.exists(path):
        return 0.75, 0.75
    else:
        with open(path, "r") as file:
            file = archivo.readlines()

        # Read the data:
        data = {}
        for line in contenido:
            key, value = line.strip().split("=")
            data[key] = value

        c.VOLUME_MUSIC = data.get("Music", 0.75)
        c.VOLUME_SFX = data.get("SFX", 0.75)
