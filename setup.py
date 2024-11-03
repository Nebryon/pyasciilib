from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pyasciilib",
    version="1.0.2",
    author="Alexandre Poggioli",
    author_email="alexandrepoggioli09@gmail.com",
    description="A library to convert images to ASCII art using different methods",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Slinky802/pyasciilib",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "Pillow>=8.0.0",  # Version minimale recommandée pour Pillow
    ],
    entry_points={
        "console_scripts": [
            "pyasciilib=pyasciilib.cli:main",
        ],
    },
)
