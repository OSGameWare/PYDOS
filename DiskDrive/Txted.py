import os
import sys
import time


def clear_screen():
    print("\033c")


def text_editor():
    clear_screen()
    print("Txted Terminal Text Editor")

    while True:
        opt = input("""
[1] Open File
[2] Create New File
[3] Rename File
[4] Edit File
[5] Exit
Opt: """)

        if opt == "1":
            file = input("Enter file name: ")
            try:
                with open(file, 'r') as f:
                    print("\033c")
                    print("\n--- File Content ---")
                    print(f.read())
                    print("--- End of File ---\n")
            except FileNotFoundError:
                print("File not found.")

        elif opt == "2":
            print("\033c")
            file = input("Enter file name: ")
            try:
                content = input(
                    "Enter content (press Enter on empty line to finish):\n")
                with open(file, 'w') as f:
                    f.write(content)
                print(f"File '{file}' created successfully!")
            except Exception as e:
                print(f"File creation error: {e}")

        elif opt == "3":
            print("\033c")
            file = input("Enter file name: ")
            try:
                old_name = input("Enter file name: ")
                new_name = input("Enter new name: ")
                os.rename(old_name, new_name)
                print(f"File '{file}' renamed successfully!")
            except FileNotFoundError:
                print("File not found.")
            except Exception as e:
                print(f"Error renaming file: {e}")

        elif opt == "4":
            print("\033c")
            file = input("Enter file name: ")
            try:
                if os.path.exists(file):
                    # First show current content
                    with open(file, 'r') as f:
                        current_content = f.read()
                        print("\n--- Current Content ---")
                        print(current_content)
                        print("--- End of Current Content ---\n")

                    # Now get new content
                    new_content = input(
                        "Enter new content (press Enter on empty line to finish):\n"
                    )

                    # Write the new content
                    with open(file, 'w') as f:
                        f.write(new_content)
                    print(f"File '{file}' updated successfully!")
                else:
                    print("File not found.")
            except Exception as e:
                print(f"Error editing file: {e}")

        elif opt == "5":
            print("\033c")
            print("Exiting Text Editor...")
            break

        else:
            print("\033c")
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    text_editor()
