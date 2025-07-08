#V.1.0.0-Win11-Cu126-BetaMiMiLion-TrialCat
from ultralytics import YOLO
from multiprocessing import freeze_support

#Load a model
model = YOLO("./PT/Ominous.pt")

# Perform object detection on an image
results = model("tar.png")
results[0].show()