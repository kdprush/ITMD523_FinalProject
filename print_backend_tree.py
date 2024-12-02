import os

def print_structure(path, level=0):
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        print("  " * level + f"- {item}")
        if os.path.isdir(full_path):
            print_structure(full_path, level + 1)

# Replace with your backend folder path
backend_path = r"C:\Users\Test\Desktop\Desk\IIT\Fall_2024\itmd-523\Final Project\ITMD523_FinalProject\backend"
print_structure(backend_path)
