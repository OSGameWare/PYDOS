import os
from datetime import date, datetime

import boot
import InfCmd
import readme
from DiskDrive import disk
from System32 import drive

print(boot.bootloader)
dir_path = drive.dir_path

DiskName = disk.DiskName

cmd = input("C:/>")

while cmd != "exit":
  if cmd == "help":
    print(InfCmd.SysCmds)
    print("")

  elif cmd == "cls":
    print("\033c")

  elif cmd == "info":
    print(readme.readme)

  elif cmd == "date":
    print("Today is: " + date.today().strftime("%B %d, %Y"))
    print("")

  elif cmd == "time":
    print("The current time is: " + datetime.now().strftime("%H:%M:%S"))
    print("")

  elif cmd == "make":
    file_name = input("Enter file name: ")
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, 'w') as f:
      print("File created successfully!")

  elif cmd == "rename":
    old_name = input("Enter file name: ")
    new_name = input("Enter new name: ")
    os.rename(old_name, new_name)

  elif cmd == "makedir":
    dir_name = input("Enter directory name: ")
    dir_path = os.path.join(dir_path, dir_name)
    os.makedirs(dir_path, exist_ok=True)
    print(f"Directory '{dir_name}' created successfully!")

  elif cmd == "type":
    file_name = input("Enter file name: ")
    file_path = os.path.join(dir_path, file_name)
    try:
      with open(file_path, 'r') as f:
        print(f.read())
    except FileNotFoundError:
      print("File not found.")

  elif cmd == "del":
    file_name = input("Enter file name to delete: ")
    file_path = os.path.join(dir_path, file_name)
    try:
      os.remove(file_path)
      print(f"File '{file_name}' deleted successfully!")
    except FileNotFoundError:
      print("File not found.")

  elif cmd == "deldir":
    dir_name = input("Enter directory name to delete: ")
    dir_path = os.path.join(dir_path, dir_name)
    try:
      os.rmdir(dir_path)
      print(f"Directory '{dir_name}' deleted successfully!")
    except FileNotFoundError:
      print("Directory not found.")
    except OSError:
      print("Directory is not empty. Cannot delete.")

  elif cmd == "cd":
    new_dir = input("Enter directory name: ")
    new_path = os.path.join(dir_path, new_dir)
    try:
      os.chdir(new_path)
      dir_path = new_path
      print(f"Current directory changed to: {dir_path}")
    except FileNotFoundError:
      print("Directory not found.")

  elif cmd == "cd ..":
    try:
      os.chdir(os.path.dirname(dir_path))
      dir_path = os.path.dirname(dir_path)
      print(f"Current directory changed to: {dir_path}")
    except FileNotFoundError:
      print("Directory not found.")

  elif cmd == "dir":
    print(*os.listdir(dir_path), sep="\n")

  elif cmd == "run":
    DiskName = input("Enter file name: ")
    try:
      with open(DiskName, 'r') as f:
        print("\033c")
        exec(f.read())
    except FileNotFoundError:
      print("Disk not found.")
  
  else:
    print("Invalid command")
  cmd = input("C:/>")
  print("")
