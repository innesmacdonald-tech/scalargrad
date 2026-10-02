import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scalargrad",
    version="0.1.0",
    author="Innes Macdonald",
    author_email="innesmacdonald.ism@gmail.com",
    description="A small scalar-valued autograd engine with a minimal neural network library. Based on micrograd by Andrej Karpathy.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
