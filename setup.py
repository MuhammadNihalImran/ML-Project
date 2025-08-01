from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements


setup(
    name="ML Project",
    version="0.0.1",
    author="Nihal",
    author_email="Nihal@123",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    description="A machine learning project setup",
)
