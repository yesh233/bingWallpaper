__author__ = 'yesh233'

import config
import urllib
import urllib2
import json
import time
import os
import errno


def get_image_url(query_url=config.wallpaper_query_url, base_url=config.bing_base_url,
                  resolution_ratio=config.resolution_ration):
    return base_url + json.loads(urllib2.urlopen(query_url).read())['images'][0]['urlbase']+'_' + \
        resolution_ratio+'.jpg'


def generate_save_path(images_path):
    return images_path+time.strftime('%y-%m-%d')+'.jpg'


def download_image(image_url, save_path):
    urllib.urlretrieve(image_url, save_path)


def set_wallpaper(save_path, set_wallpaper_command=config.set_wallpaper_command):
    try:
        os.system(set_wallpaper_command+'file://'+save_path)
    except:
        raise


def makedir(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def generate_images_path(path=config.save_path):
    return os.path.expanduser('~')+path


def test():
    print get_image_url()
    print generate_save_path(generate_images_path())
    print set_wallpaper(generate_save_path(generate_images_path()))


def main():
    makedir(generate_images_path())
    download_image(get_image_url(), generate_save_path(generate_images_path()))
    set_wallpaper(generate_save_path(generate_images_path()))


if __name__ == '__main__':
    main()
    # test()