#pip3 install argsparse os tqdm requests
from tqdm import tqdm
import requests
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--url',help='url file download')
parser.add_argument('--out',help='path of file out')
args = parser.parse_args()

url = args.url
file_out = args.out

if not os.path.isdir(file_out):
	os.makedirs(file_out)

buffer_size = 1024
response = requests.get(url,stream=True)
file_size = int(response.headers.get('Content-Length',0))

path_file = os.path.join(file_out,url.split('/')[-1])

progress = tqdm(desc=f'Download file {path_file}',total=file_size,unit='B',unit_scale=True)

with open(path_file,'wb') as f:
	for data in response.iter_content(buffer_size):
		f.write(data)
		progress.update(len(data))

