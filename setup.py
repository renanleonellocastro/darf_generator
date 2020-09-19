import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="darf-generator", 
    version="0.0.1",
    author="Renanzera Roots",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/renanleonellocastro/darf_generator",
    scripts=["scripts/darf_gen_app.py"],
    package_dir={"": "src"},
    packages=setuptools.find_namespace_packages(where="src"),
    test_suite="tests",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
