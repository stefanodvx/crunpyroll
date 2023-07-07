import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crunpyroll",
    version="2.1",
    author="stefanodvx",
    author_email="pp.stefanodvx@gmail.com",
    description="Async Crunchyroll API Wrapper in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stefanodvx/crunpyroll",
    project_urls={
        "Tracker": "https://github.com/stefanodvx/crunpyroll/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["httpx"],
    packages=setuptools.find_packages(),
    python_requires=">=3.11",
)