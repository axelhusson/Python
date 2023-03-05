# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pathlib import Path

def print_hi(name):
    """
    The print_hi function prints the message 'Hi, NAME' in
    the terminal where NAME is passed into the function as an argument.


    :param name: Pass the name of the person to be greeted
    :return: The string 'hi, name'
    :doc-author: Trelent
    """
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}, how are you?')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print_hi('PyCharm')

dirs = {".png" : "Images",
        ".jpg" : "Images",
        ".jpeg" : "Images",
        ".pdf" : "Documents",
        ".txt" : "Documents",
        ".csv" : "Documents",
        ".exe" : "Executable",
        ".zip" : "archive"}

p = Path.home() / "Downloads"
files = [f for f in p.iterdir() if f.is_file()]
for f in files:
    output_dir = p / dirs.get(f.suffix, 'Autres')
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
