## Python3 Utilities

Project Homepage: https://github.com/ohidurbappy/python3-utilities

An utility library for python3 that saves time by avoiding to write repetitive codes.

### Usage

#### Installing

```bash
pip install python3-utilities
```






### How to build


**Update Setuptools and wheel**
```bash
python3 -m pip install --user --upgrade setuptools wheel
```

**Now run this command from the same directory where setup.py is located:**
```bash
python3 setup.py sdist bdist_wheel
```

**This command should output a lot of text and once completed should generate two files in the dist directory:**

```
dist/
  example_pkg_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
  example_pkg_YOUR_USERNAME_HERE-0.0.1.tar.gz

```

**To upload to pypi Install twine and run it**
```
python3 -m pip install --user --upgrade twine
python3 -m twine upload --repository pypi dist/*
or
python3 -m twine upload dist/*
```
> [!NOTE]
> You will need to provide token from pypi in this step
> username: __token__
> password: your-token


For updating [See Here](https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives)