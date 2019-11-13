import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arissupriy", # Replace with your own username
    version="0.0.1",
    author="Aris Supriyanto",
    author_email="arissy96@gmail.com",
    description="Build your own console",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arissupriy/konsol",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.6',
)