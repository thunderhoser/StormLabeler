"""Setup file for StormLabeler."""

from setuptools import setup

PACKAGE_NAMES = [
    'stormlabeler', 'stormlabeler.utils', 'stormlabeler.scripts'
]

KEYWORDS = [
    'machine learning', 'deep learning', 'artificial intelligence',
    'data mining', 'weather', 'meteorology', 'thunderstorm', 'wind', 'tornado'
]

SHORT_DESCRIPTION = (
    'Interface for humans to label "interesting" (tornado-related) parts of '
    'storms and compare their answers with deep learning.')

LONG_DESCRIPTION = SHORT_DESCRIPTION

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

PACKAGE_REQUIREMENTS = [
    'numpy',
    'scipy',
    'scikit-image',
    'netCDF4',
    'opencv-python',
    'matplotlib',
    'pandas',
    'shapely',
    'roipoly'
]

if __name__ == '__main__':
    setup(name='StormLabeler',
          version='0.1',
          description=SHORT_DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license='MIT',
          author='Ryan Lagerquist',
          author_email='ryan.lagerquist@ou.edu',
          url='https://github.com/thunderhoser/StormLabeler',
          packages=PACKAGE_NAMES,
          scripts=[],
          keywords=KEYWORDS,
          classifiers=CLASSIFIERS,
          include_package_data=True,
          zip_safe=False,
          install_requires=PACKAGE_REQUIREMENTS)
