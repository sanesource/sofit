from setuptools import find_packages, setup


setup(
    name='sofit',
    version='0.1',
    description='Get solutions to errors/issues within your terminal.',
    packages=find_packages(),
    include_package_data=True,
    entry_points='''
        [console_scripts]
        sofit=sofit.sofit:main
    '''
)
