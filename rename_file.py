import os

print(os.getcwd())

FOLDER_PATH = f'/Users/ericjulianto/Desktop/WaterMeter/images/val/'
OUTPUT_PATH = f'/Users/ericjulianto/Desktop/WaterMeter/images/val/'

for i, filename in enumerate(os.listdir(FOLDER_PATH)):
    os.rename(os.path.join(FOLDER_PATH, filename),
              os.path.join(OUTPUT_PATH) + str(i) + '.jpg')
