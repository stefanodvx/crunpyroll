import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crunchyroll-beta",
    version="1.1.1",
    author="stefanodvx",
    author_email="pp.stefanodvx@gmail.com",
    description="API for Crunchyroll BETA",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stefanodvx/crunchyroll",
    project_urls={
        "Tracker": "https://github.com/stefanodvx/crunchyroll/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)