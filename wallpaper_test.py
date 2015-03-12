__author__ = 'yesh233'

import unittest
import config
from wallpaper import *


class ImageDownloaderTestCase(unittest.TestCase):
    def setUp(self):
        self.ImageDownloader = ImageDownloader(config.wallpaper_query_url, config.bing_base_url,
                                               config.resolution_ratio, config.save_directory)

    def tearDown(self):
        self.ImageDownloader = None

    def test_get_image_save_path(self):
        self.assertEqual(self.ImageDownloader.get_image_save_path(), 'abc')

if __name__ == '__main__':
    unittest.main()
