from setuptools import setup, find_packages

setup(
    name='hrnet-pose-estimation',
    version='0.1.0',
    packages=find_packages(include=['hrnet_pose', 'hrnet_pose.*']),
    install_requires=[
        'EasyDict==1.7',
        'shapely==1.6.4',
        'Cython',
        'scipy',
        'pandas',
        'pyyaml',
        'json_tricks',
        'scikit-image',
        'yacs>=0.1.5'
    ],
    package_data={'experiments': ['*.yaml']}
)
