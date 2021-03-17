import os
#path = os.getcwd()
#print("Current directory is: %s" %path)
path = "signDetection/Tensorflow/workspace/collectedImagesProbe"
try:
    os.makedirs(path)
except OSError:
    print("No se puede crear el directorio %s" %path)
else:
    print("Directorio creado satisfactoriamente %s" %path)