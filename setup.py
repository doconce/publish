import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name             = "publish-doconce",
    version          = "1.1.4",
    author           = "Logg Systems/Anna Logg",
    author_email     = "anna@loggsystems.se",
    maintainer       = "Alessandro Marin",
    maintainer_email = "alessandro.marin@fys.uio.no",  
    description      = "Distributed publication management system",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url              = "https://github.com/doconce/publish",
    packages         = ["publish",
                          "publish.formats",
                          "publish.config"],
    classifiers      = ['Development Status :: 5 - Production/Stable',
                          'Intended Audience :: Science/Research',
                          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                          'Environment :: Console',
                          'Programming Language :: Python :: 3'],
    python_requires  = '>=3.6',
    install_requires = [ 'python-Levenshtein-wheels', 'lxml' ],
    scripts          = ["scripts/publish"],
    data_files       = [("share/man/man1", ["doc/man/man1/publish.1.gz"])],
)