__author__ = 'yesh233'

import unittest
from wallpaper import *
import subprocess
import os


class ImageDownloaderTestCase(unittest.TestCase):
    def setUp(self):
        self.__image_downloader = ImageDownloader(config.wallpaper_query_url, config.bing_base_url,
                                                  config.resolution_ratio, config.save_directory)

    def tearDown(self):
        self.__image_downloader = None

    def test_get_image_save_path(self):
        self.assertEqual(self.__image_downloader.get_image_save_path(), '/home/yesh233/.bingWallpaper/' +
                                                                        time.strftime('%y-%m-%d')+'.jpg')


class WallpaperSetterTestCase(unittest.TestCase):
    def setUp(self):
        self.__wallpaper_setter = WallpaperSetter(config.set_wallpaper_command)

    def tearDown(self):
        self.__wallpaper_setter = None

    def test(self):
        subprocess.call(['./wallpaper_setter.sh', 'file:///home/yesh233/.bingWallpaper/15-03-13.jpg'])

if __name__ == '__main__':
    unittest.main()
