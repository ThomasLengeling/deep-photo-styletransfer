import os
import math

cwd = os.getcwd()

DIR = cwd+'/examples/movie_charles_in'
numImgs = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

print(numImgs)

for i in range(numImgs):

    cmd = ''
    index = str(i)

    cmd = 'python3 deep_photo.py -content_image examples/movie_charles_in/frame'+index+'.png -style_image examples/city_night.png -style_seg examples/city_night_seg.png -laplacian examples/movie_charles_lap/frame_'+index+'_700.csv -output_image examples/movie_charles_out/frame'+index+'.png -image_size 700'

    print(cmd)
    os.system(cmd)
