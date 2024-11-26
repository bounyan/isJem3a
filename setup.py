from setuptools import setup, find_packages

setup(
    name="isJem3a",
    version="1.0.0",
    description="A package to check if tomorrow is Friday",
    author="chkoupey",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'isJem3a=isJem3a.check:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
