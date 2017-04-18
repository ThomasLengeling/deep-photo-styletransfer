import os
import math

DIR = local_frame_dir
numImgs = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

print(numImgs)

for i in numImgs:
    cmd = ''

    'python3 deep_photo.py -content_image examples/movie_charles_in/frame'+i+'.png -content_seg examples/movie_charles_seg/frame'+i+'.png -style_image examples/city_night.png -style_seg examples/city_night_seg.png -laplacian examples/movie_charles_lap/frame_'+i+'_700.csv -output_image examples/movie_charles_out/frame'+i+'.png -image_size 700'

    print(cmd)
    os.system(cmd)
