# -*- coding: utf-8 -*-

from pathlib import PurePath

from decouple import AutoConfig


# Build paths inside the project like this: BASE_DIR.joinpath('some')
# `pathlib` is better than writing:
# BASE_DIR = dirname(dirname(dirname(dirname(__file__))))
BASE_DIR = PurePath(__file__).parent.parent

# Loading `.env` files
# See docs: https://gitlab.com/mkleehammer/autoconfig
config = AutoConfig(search_path=BASE_DIR.joinpath('config'))
