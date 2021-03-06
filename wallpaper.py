__author__ = 'yesh233'

import config
import urllib
import urllib2
import json
import time
import os
import errno
import subprocess


class ImageDownloader(object):
    def __init__(self, query_url, base_url, resolution_ratio, save_directory):
        self.__query_url = query_url
        self.__base_url = base_url
        self.__resolution_ratio = resolution_ratio
        self.__save_directory = save_directory

    def __get_image_url(self):
        return self.__base_url + json.loads(urllib2.urlopen(self.__query_url).read())['images'][0]['urlbase']+'_' + \
            self.__resolution_ratio+'.jpg'

    def __get_save_directory(self):
        return os.path.expanduser('~')+self.__save_directory

    def __make_save_directory(self):
        try:
            os.makedirs(self.__get_save_directory())
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(self.__get_save_directory()):
                pass
        else:
            raise

    def get_image_save_path(self):
        return self.__get_save_directory()+time.strftime('%y-%m-%d')+'.jpg'

    def download_image(self):
        self.__make_save_directory()
        urllib.urlretrieve(self.__get_image_url(), self.get_image_save_path())


class WallpaperSetter(object):
    def __init__(self, script_path):
        self.__wallpaper_set_script_path = script_path

    def set_wallpaper(self, image_path):
        try:
            subprocess.call([self.__wallpaper_set_script_path, 'file://'+image_path])
        except:
            raise


class BingWallpaper(object):
    def __init__(self, image_downloader, wallpaper_setter):
        self.__image_downloader = image_downloader
        self.__wallpaper_setter = wallpaper_setter

    def run(self):
        self.__image_downloader.download_image()
        self.__wallpaper_setter.set_wallpaper(self.__image_downloader.get_image_save_path())


def main():
    bing_wallpaper = BingWallpaper(ImageDownloader(config.wallpaper_query_url, config.bing_base_url,
                                                   config.resolution_ratio, config.save_directory),
                                   WallpaperSetter(config.set_wallpaper_script_path))
    bing_wallpaper.run()


if __name__ == '__main__':
    main()