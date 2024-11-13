from pathlib import Path

path = Path('List')

if path.exists():
    for file in path.iterdir():
        if file.is_file():
            print(file)
else:
    print("Invalid Path..")

