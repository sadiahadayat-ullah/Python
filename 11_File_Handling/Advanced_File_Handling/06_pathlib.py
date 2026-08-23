from pathlib import Path

print("Current Directory:", Path.cwd())

file_path = Path("students.txt")

print("File Name:", file_path.name)
print("File Suffix:", file_path.suffix)
print("File Exists:", file_path.exists())
print("Is file:", file_path.is_file())
print("Is directory:", file_path.is_dir())