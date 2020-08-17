import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python3-utilities", # Replace with your own username
    version="0.0.1",
    author="Ohidur Rahman Bappy",
    author_email="ohidurbappy+python3.utilities@gmail.com",
    description="An utility library for python3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ohidurbappy/python3-utilities",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)