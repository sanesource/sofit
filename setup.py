from setuptools import find_packages, setup


def read_requirements():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')
    return requirements


setup(
    name='sofit',
    version='0.1',
    description='Get solutions to errors/issues within your terminal.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    entry_points='''
        [console_scripts]
        sofit=sofit.sofit:main
    '''
)
