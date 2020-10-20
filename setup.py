from setuptools import setup

setup(
    name='youtube_searcher',
    version='0.1.2',
    packages=['yt_list'],
    url='https://github.com/youtube_list/yt_search',
    license='GPL-3.0 License',
    author='GEO',
    install_requires=["bs4", "requests", "requests_cache"],
    author_email='geocipto@gmail.com',
    description='youtube list'
)
