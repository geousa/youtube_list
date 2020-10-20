from setuptools import setup

setup(
    name='yt_search',
    version='0.1.2',
    packages=['yt_list'],
    url='https://github.com/geousa/youtube_list',
    license='GPL-3.0 License',
    author='GEO',
    install_requires=["bs4", "requests", "requests_cache"],
    author_email='geocipto@gmail.com',
    description='youtube'
)
