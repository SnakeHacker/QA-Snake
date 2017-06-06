
from setuptools import setup, find_packages

setup(
    name='QASnake',
    version='0.1.0',
    description='QA Snake v0.1.0',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    author='Snake',
    url='http://www.snakehacker.me',
    author_email='616976756@qq.com',
    license='MIT',
    packages=['BaiduMap', 'QA', 'QA.resources', 'demo', 'QACrawler', 'Tools'],
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.aiml', '*.png'],
    },
    zip_safe=False,
)