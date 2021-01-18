from PIL import Image
import os

im_dir = "C:/Users/sneha/Downloads/images (1)/images/2w"
file_ext = {'.png', '.tif'}
file_list = [f for f in os.listdir(im_dir) if len(f) >= 4 and f[-4:] in file_ext]
save_dir = "C:/Users/sneha/Downloads/images (1)/images/2w/output"


start_pos = start_x, start_y = (0, 0)
cropped_image_size = w, h = (500, 500)

def main():
    for file in file_list:
        img = Image.open(f'{im_dir}/{file}')
        imgcrop(img, file, 17, 17)


def imgcrop(im, file, x_split, y_split):
    file_name, file_ext = os.path.splitext(file)
    img_width, img_height = im.size
    width = img_width // x_split
    height = img_height // y_split
    for i in range(0, y_split):
        for j in range(0, x_split):
            box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
            a = im.crop(box)
            a.save(save_dir + "/" + file_name + "-" + str(i) + "-" + str(j) + file_ext)

if __name__ == '__main__':
    main()