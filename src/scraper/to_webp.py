import os, sys
from os.path import isfile, join, isdir
import shutil
import subprocess as sp


'''converting to webp'''
def transcode_img(quality):

    img_paths = []
    count = 0
    

    img_paths = [f for f in os.listdir('images/') if isfile(join('images/', f))]

    if (isdir('images/'  + quality)):
        shutil.rmtree('images/' + quality)
        os.mkdir('images/'  + quality)
    else:
        os.mkdir('images/'  + quality)

    logs = []
    for i in img_paths:

        query = ''
        without_query = ''
        if '?' in i:
            x = i.split('?')
            query = x.pop()
            query = '?' + query
            x = '?'.join(x)
            without_query = x
        else:
            x = i
        # handle .webp only as file name
        ext = x.split('.')[-1]
     
        if ext == '':
            x += '.webp' + query
        elif ext.isdigit():
            x = x
        else:
            x = x.replace(ext, 'webp') + query

        #default quality is 75. Giving a higher value can at time yield better results and thus, increases image's size
        output = sp.getoutput('cwebp -short -q ' + quality + ' "images/' + i + '" -o "images/' + quality + '/' + x + '"' )
        
        val = output.split()
        if len(val) == 2:  # when successful, short output is always in the form of '%d %f\n'
            logs.append([i, val[0], without_query])

            if 'Saved output' in output:
                size = output.split('Saved output file ')[1].split()[0][1:]
                logs.append([i, size, without_query])


        count += 1

    return logs



def main():

    rpt = sys.argv[1]

    try:
        logs = transcode_img(str(75)) 

        for i in range(7, 0,-2):
            logs = transcode_img(str(i*10)) 

        print('Image transcoding complete. Results written to: ' + rpt)
    except Exception as err:
        print('Image transcoding failed for ', rpt,'\n', err)

   

main()