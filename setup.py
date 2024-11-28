from setuptools import find_packages, setup
from typing import List
HYPHEN_E_DOT = "-e ."


def get_req(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("/n", " ") for i in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="ml-student-prediction",
    version="0.0.1",
    author="Daniel Augustine",
    author_email="augustinedanielp@gmail.com",
    packages=find_packages(),
    install_requires=get_req('requirements.txt'))
