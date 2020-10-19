from setuptools import setup

setup(
    name='calculator',
    version='0.1.0',
    author='Jugal Bilimoria',
    description="A gui calculator program using tkinter",
    url='https://github.com/JugalBili/Python-GUI-Calculator',
    license='license.txt',
    long_description=open('README.md').read(),
    install_requires=[
        "tk >= 8.6.10"
    ],
    python_requires='>=3.6',
)