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
        file.write(f"EDGE_X={c.EDGE_X}\n")
        file.write(f"EDGE_Y={c.EDGE_Y}\n")

# Load system:
def load_data():
    # Path of the file:
    path = "resources/data/file.txt"
    
    # Load function:
    if not os.path.exists(path):
        c.VOLUME_MUSIC = 0.75
        c.VOLUME_SFX = 0.75
        c.EDGE_X = 4
        c.EDGE_Y = 2
    else:
        with open(path, "r") as file:
            content = file.readlines()

        # Read the data:
        data = {}
        for line in content:
            key, value = line.strip().split("=")
            data[key] = value

        c.VOLUME_MUSIC = float(data.get("Music", 0.75))
        c.VOLUME_SFX = float(data.get("SFX", 0.75))
        c.EDGE_X = int(data.get("EDGE_X", 4))
        c.EDGE_Y = int(data.get("EDGE_Y", 2))
