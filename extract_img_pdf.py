#pip3 install PyMuPDF Pillow argparse os

import fitz # PyMuPDF
import io
from PIL import Image
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-f',help='path of pdf file e.g. test\\doc\\test.pdf')
parser.add_argument('-o',help='path of file out e.g. test\\doc')
args = parser.parse_args()

file = args.f
file_out = args.o

if file_out[-1] == '\\':
	file_out = file_out[:-1]

if not os.path.isdir(file_out):
	os.makedirs(file_out)

pdf_file = fitz.open(file)
for page_index in range(len(pdf_file)):
	page = pdf_file[page_index]
	image_list = page.getImageList()
	if image_list:
		print(f'Found a total of {len(image_list)} images in page{page_index+1}')
	else:
		print(f'Not Found image in page{page_index+1}')

	for image_index,img in enumerate(image_list,start=1):
		base_image = pdf_file.extractImage(img[0])
		image_ext = base_image['ext']
		iamge_bytes = base_image['image']
		image = Image.open(io.BytesIO(iamge_bytes))
		image.save(open(f'{file_out}\\image_{page_index+1}_{image_index}.{image_ext}','wb'))