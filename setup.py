import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aemo-EIGENMODE",
    version="0.1.20",
    author="Eric Sheppard",
    author_email="eric@eigenmo.de",
    description="A package to parse and verify AEMO MMS data model files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/esheppa/aemo-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires='>=3.8',
)
