import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fuzzy-text-classifier",
    version="1.1.0",
    author="Raffaello Paletta",
    author_email="raffaellopaletta@gmail.com",
    description="A fuzzy classifier for natural language text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/raffaellopaletta/ftc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
