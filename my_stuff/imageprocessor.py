from PIL import Image
import code

def rotate_box(an_image):
    box = (100,100,400,400)
    region = an_image.crop(box)
    transposed = region.transpose(Image.ROTATE_180)
    an_image.paste(transposed, box)
    return an_image

def to_grayscale(an_image):
	grayscale_im = an_image.convert('LA')
	return grayscale_im

#saving the new grayscale pictures in the new folder
num = 0
for pic_name in code.get_filenames2('C:\\Users\\JRaimann\\Desktop\\pictures'):
    im = Image.open(pic_name)
    im = to_grayscale(im)
    newfilename = 'pic_gray_' + str(num) + '.jpg'
    num = num + 1
    newfullpath = os.path.join('C:\\Users\\JRaimann\\Desktop\\pictures\\grayscale',newfilename)
    im.save(newfullpath)


for pic_name in code.get_filenames2('C:\\Users\\JRaimann\\Desktop\\pictures'):
    im = Image.open(pic_name)
    im = rotate_box(im)
    im.show()

im = Image.open ("C:\\Users\\JRaimann\\Desktop\\pictures\\picture1.jpg")
print(im.size)
print(im.format)
im = rotate_box(im)
im.show()
im.save('C:\\Users\\JRaimann\\Desktop\\pictures\\grayscale\\picture1.jpg')


im2 = Image.open ("C:\\Users\\JRaimann\\Desktop\\pictures\\picture2.jpg")
im2 = rotate_box(im2)
im2.show()

im3 = Image.open ("C:\\Users\\JRaimann\\Desktop\\pictures\\picture3.jpg")
im3 = rotate_box(im3)
im3.show()

im4 = Image.open ("C:\\Users\\JRaimann\\Desktop\\pictures\\picture4.jpg")
im4 = rotate_box(im4)
im4.show()


box = (100,100,400,400)
region = im.crop(box)
transposed = region.transpose(Image.ROTATE_180)
im.paste(transposed, box)
im.show()


