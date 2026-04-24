import os
from pathlib import Path

# Create directory
os.mkdir("test_dir")

# Create nested directories
os.makedirs("parent/child", exist_ok=True)

# Current directory
print("Current directory:", os.getcwd())

# List files
print("Directory content:", os.listdir())

# Remove directory
os.rmdir("test_dir")