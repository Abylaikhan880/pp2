import shutil
import os

os.makedirs("destination", exist_ok=True)

shutil.copy("sample.txt", "destination/sample.txt")

shutil.move("sample_backup.txt", "destination/sample_backup.txt")

print("Files copied and moved successfully.")