import os

def print_structure(path, level=0):
    for item in os.listdir(path):
        print("  " * level + f"- {item}")
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            print_structure(full_path, level + 1)

print_structure(".")
