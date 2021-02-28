from PIL import Image, ImageOps
import os
import pandas as pd

def batch():
    output=dict()
    rootdir = '/Users/sneha/Desktop/mni/cp_images'
    paths=[]
    paths = os.listdir(rootdir)
    for path in paths:
        if path.endswith('.TIF'):
            full_path= rootdir + '/' + path
            get_avg(output, full_path)
    
    print(output)


def get_avg(output, file_path): # TODO fix these var names, they r dumb
    # TODO add in control or not col here
    im = Image.open(file_path)
    im2 = im.copy() 
    im3 = ImageOps.grayscale(im2)
    im3.thumbnail((1, 1))
    avg_color = im3.getpixel((0, 0))
    output[file_path] = avg_color

def put_dict_in_csv(output, csv_path):
    df = pd.DataFrame.from_dict(output)
    result = df.to_csv(path_or_buf=csv_path, header=["Image", "Avg Pixels"], index=False)

def main(): 
    batch()

if __name__ == "__main__":
    main()

