from PIL import Image, ImageOps
import os
import pandas as pd
import sys 

# TODO Make control measurements valid

def batch():
    rootdir = str(sys.argv[1])
    csv_path = str(sys.argv[2])
    batch = str(sys.argv[3])
    plate = str(sys.argv[4])
    output=dict()
    control_or_no = []
    paths=[]
    paths = os.listdir(rootdir)
    for path in paths:
        if path.endswith('.TIF'):
            full_path= rootdir + '/' + path
            if 'd1' in path:
                control_or_no.append('Y')
            else:
                control_or_no.append('N')
            get_avg(output, full_path)

    put_dict_in_csv(output, control_or_no, batch, plate, csv_path)

def get_avg(output, file_path): 

    im = Image.open(file_path)
    imcp = im.copy() 
    imgraycp = ImageOps.grayscale(imcp)
    imgraycp.thumbnail((1, 1))
    avg_color = imgraycp.getpixel((0, 0))
    output[file_path] = avg_color

def put_dict_in_csv(output, control_or_no, batch, plate, csv_path): 
    df = pd.DataFrame.from_dict(data=output, orient='index', columns=['Intensity'])
    df['Control'] = control_or_no
    name=csv_path + '/AvgIntensity_Batch_' + batch + '_Plate_' + plate + '.csv'
    result = df.to_csv(path_or_buf=name, index_label='Image')

def main(): 
    if len(sys.argv) != 5:
        sys.exit('yo, those are some wack positional arguments. usage: avg_intensity.py global-path-dir-ims-are-in where-and-what-csv-should-be')
    batch()

if __name__ == "__main__":
    main()

