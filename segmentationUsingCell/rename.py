from PIL import Image
import os

im_dir = "/Users/sneha/Desktop/mni/cell_bodiez_BIG"
file_ext = {'.png'}
file_list = [f for f in os.listdir(im_dir) if len(f) >= 4 and f[-4:] in file_ext]
save_dir = "/Users/sneha/Desktop/mni/cell_bodiez_standard_BIG"
fol_name = "fol1_"
def main():
    for file in file_list:
        im = Image.open(f'{im_dir}/{file}')
        cntrcrop(im, file, 64, 64)

def cntrcrop(im, file, dim1, dim2):
    file_name, file_ext = os.path.splitext(file)
    left = int(im.size[0]/2-dim1/2)
    upper = int(im.size[1]/2-dim2/2)
    right = left +dim1
    lower = upper + dim2

    im_cropped = im.crop((left, upper,right,lower))
    print(im_cropped.size)
    im_cropped.save(save_dir + "/" + fol_name + file_name + file_ext)

if __name__ == '__main__':
    main()
