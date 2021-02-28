from PIL import Image, ImageOps
import os
import pandas as pd
import sys 

# TODO Make batch, plate, control measurements valid

def batch():
    input_paths = str(sys.argv)
    rootdir = str(sys.argv[1])
    csv_path = str(sys.argv[2])
    output=dict()
    control_or_no = []
    batch=[]
    plate=[]
    paths=[]
    paths = os.listdir(rootdir)
    for path in paths:
        if path.endswith('.TIF'):
            full_path= rootdir + '/' + path
            if 'd1' in path:
                control_or_no.append('Y')
            else:
                control_or_no.append('N')
            if 'd2' in path:
                batch.append(1)
            else:
                batch.append(0)
            if 'd0' in path:
                plate.append('idk')
            else:
                plate.append('proof of concept')
            get_avg(output, full_path)

    put_dict_in_csv(output, csv_path, control_or_no, batch, plate)

def get_avg(output, file_path): 

    im = Image.open(file_path)
    imcp = im.copy() 
    imgraycp = ImageOps.grayscale(imcp)
    imgraycp.thumbnail((1, 1))
    avg_color = imgraycp.getpixel((0, 0))
    output[file_path] = avg_color

def put_dict_in_csv(output, csv_path, control_or_no, batch, plate): 
    df = pd.DataFrame.from_dict(data=output, orient='index', columns=['Intensity'])
    df['Control'] = control_or_no
    df['Batch'] = batch
    df['Plate'] = plate
    result = df.to_csv(path_or_buf=csv_path)

def main(): 
    if len(sys.argv) != 3:
        sys.exit('yo, those are some wack positional arguments. usage: avg_intensity.py global-path-dir-ims-are-in where-and-what-csv-should-be')
    batch()

if __name__ == "__main__":
    main()

