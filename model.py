from os import listdir
from os.path import isfile, join
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class Antialiasing:
    def __init__(self, path, method):
        self.path = path
        self.method = method
        self.files = [f for f in listdir(path) if isfile(join(path, f))]
    
    def get_directorys(self):
        return self.files
        

    def convert(self):
        print(self.method)
        for index in range(len(self.files)):
            image_path = f'{self.path}/{self.files[index]}'
            print(image_path)
            img = Image.open(image_path)
            plt.figure()
            plt.imshow(img, interpolation=self.method, cmap='RdBu_r')
        plt.show()
        
        

