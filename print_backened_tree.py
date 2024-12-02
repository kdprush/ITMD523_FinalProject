import os

def print_structure(path, level=0):
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        print("  " * level + f"- {item}")
        if os.path.isdir(full_path):
            print_structure(full_path, level + 1)

# Correct path to the backend folder inside Vagrant
backend_path = "/vagrant/backend"
print_structure(backend_path)

