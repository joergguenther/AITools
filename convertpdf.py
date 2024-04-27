# This program converts each PDF page into a single image

import os
from pdf2image import convert_from_path

# Assign input_dir to PDF dir, ex: "C://Users//user//Desktop//pdfs"
input_dir = os.path.expanduser('~/Development/PDF Raw Input')
# Assign output_dir to the dir you’d like the images to be saved"
output_dir = os.path.expanduser('~/Development/Images Output')
dir_list = os.listdir(input_dir)

print(input_dir)
print(output_dir)
print(dir_list)

index = 1
while index < len(dir_list):

    
    print(dir_list[index])	
    ##print(filename)
    images = convert_from_path(f'{input_dir}//' + dir_list[index])
    for i in range(len(images)):
        images[i].save(f'{output_dir}//doc' + str(index) +'_page'+ str(i) +'.jpg', 'JPEG')
    index += 1
    
    
    