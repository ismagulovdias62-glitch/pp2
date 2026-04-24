import shutil
from pathlib import Path

# Create folder if not exists
Path("moved_files").mkdir(exist_ok=True)

# Move file
shutil.move("sample.txt", "moved_files/sample.txt")

# Find files by extension
for file in Path(".").rglob("*.txt"):
    print("Found txt file:", file)