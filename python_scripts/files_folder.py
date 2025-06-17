import os

def list_files_and_folders():
    path = input("Enter folder path: ")
    try:
        for item in os.listdir(path):
            print(i)
    except FileNotFoundError:
        print("Path not found!")
    except PermissionError:
        print("Permission denied!")

if __name__ == "__main__":
    list_files_and_folders()

