from setuptools import setup, find_packages

HYPEN_E_DOT='-e .'

def get_requires(file_path:str) -> list[str]:
    '''
    this function returns the list of requirements
    '''

    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("/n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup(

    name='mlpoject',
    version='0.0.1',
    author='Sanket',
    author_email='sanketbandgar01@gmail.com',
    packages=find_packages(),
    install_requires=get_requires('requirements.txt'),
)