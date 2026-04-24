# File modes: w, a, x

# Write file (overwrite if exists)
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Hello World\n")
    f.write("Python Practice 6\n")

# Append to file
with open("sample.txt", "a", encoding="utf-8") as f:
    f.write("Appended line\n")

# Create new file (error if exists)
# with open("new_file.txt", "x") as f:
#     f.write("Created with x mode")