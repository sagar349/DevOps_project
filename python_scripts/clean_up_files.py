import os 

def cleanup_tmp_folders(path):
    try:
        if not os.path.exists(path):
            print("Path not found! ")
            return

         for i in os.listdir(path):
            i_path = os.path.join(path , i):
            try:
                if os.path.isfile(i_path) or os.path.islink(i_path):
                    os.remove(i_path)
                    print(f"File deleted")   
            except Exception as e:
                print(f"failed to delete") 
        except PermissionError:
            print("Permission deneid!")

if __name__ == "__main__":
    folders = input("Enter folder name")
    cleanup_tmp_folders()