from setuptools import setup
from Cython.Build import cythonize

if __name__ == "__main__":
    setup(
        package_dir={'src/': ''},
        ext_modules=cythonize("src/bubblesort/clibs/*.pyx",
                              compiler_directives={"language_level": "3"})
    )
