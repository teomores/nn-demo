import subprocess
import os
import csv

test_dir = './test_images'
directory = os.fsencode(test_dir)

# saves results in a .csv file
with open("testResults.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Document Type", "Score", "Time"])

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(("jpg","jpeg","png")):
        os.system('python -m label_image --image={}/{}'.format(test_dir,filename))
