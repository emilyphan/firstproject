import setuptools


setuptools.setup(
    name="firstproject",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'gui_scripts': [
            'firstproject = firstproject.main:entry_point',
        ],
    },
    install_requires=[
        'pyqt5',
    ],
)