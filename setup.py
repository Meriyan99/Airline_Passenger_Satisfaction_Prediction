from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> list[str]:
    '''
        This function will return list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # while go through line by line ignore the new line charachter
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='Airline_Passenger_Satisfaction_Prediction',
    version='0.0.1',
    author='Meriyan',
    author_email='it21076916@my.sliit.lk',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)