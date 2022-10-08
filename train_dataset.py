import os
import re
import pandas as pd

folder_url = "https://raw.githubusercontent.com/arimatiur/tflite_train_dataset/main/images/"
folder_local = r"E:\Latihan\TFLite\tflite_train_dataset\images"
folder = os.path.abspath(folder_local)

txt_files = []
for file in os.listdir(folder):
    if file.endswith(".txt"):
        txt_files.append(os.path.join(folder, file))
img_files = []
for file in os.listdir(folder):
    if file.endswith(".jpg"):
        img_files.append(os.path.join(folder_url, file))

train_dataset = []
for txt, img in zip(txt_files, img_files):
    with open(txt) as f1:
        for line in f1:
            train_dataset.append(str(img) + "," + re.sub("\s+", ",", line.strip()).strip())

dataframe = pd.DataFrame(train_dataset)
dataframe.to_csv("train_dataset.csv")