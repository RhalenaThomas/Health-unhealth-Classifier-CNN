#!/usr/bin/env python

from PIL import Image, ImageOps
import os
import pandas as pd
import sys 
import statistics as stats

def batch():
    rootdir = str(sys.argv[1])
    csv_path = str(sys.argv[2])
    name = str(sys.argv[3])
    #plate = str(sys.argv[4])
    #celltype = str(sys.argv[5])
    output=[]
    control_or_no = []
    channel = []
    paths=[]
    paths = os.listdir(rootdir)
    for path in paths:
        if path.endswith('.TIF'):
            full_path= rootdir + '/' + path
            print(full_path)
            print('sanity check')
            if 'A01' or 'A02' or 'A03' or 'A04' or 'A05' or 'A06' in path:
                control_or_no.append('Y')
            else:
                control_or_no.append('N')
            get_avg(output, full_path)

    put_dict_in_csv(output, control_or_no, name, csv_path)

def get_avg(output, file_path): 
    print(file_path)
    im = Image.open(file_path)
    imgray = ImageOps.grayscale(im)

    width, height = im.size
    print(width)
    print(height)
    total = []
    for i in range(0, width):
        for j in range(0, height):
            total.append(imgray.getpixel((i,j)))
    output.append([file_path, stats.mean(total), stats.median(total), max(total), min(total)])

def put_dict_in_csv(output, control_or_no, name, csv_path): 
    df = pd.DataFrame.from_dict(data=output)
    df['Control'] = control_or_no
    full_name=csv_path + '/AvgIntensity_' + name + '.csv'
    result = df.to_csv(path_or_buf=full_name, header=['Image', 'Mean Intensity', 'Median Intensity', 'Max Intensity', 'Min Intensity', 'Control'], index=False)

def main(): 
    if len(sys.argv) != 4:
        sys.exit('yo, those are some wack positional arguments. usage: avg_intensity.py global-path-dir-ims-are-in dir-csv-should-be name')
    batch()

if __name__ == "__main__":
    main()

