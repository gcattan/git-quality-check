import os.path as op

from setuptools import setup, find_packages


# get the version (don't import mne here, so dependencies are not needed)
version = None
with open(op.join("git_quality_check", "_version.py"), "r") as fid:
    for line in (line.strip() for line in fid):
        if line.startswith("__version__"):
            version = line.split("=")[1].strip().strip("'")
            break
if version is None:
    raise RuntimeError("Could not determine version")

with open("README.md", "r", encoding="utf8") as fid:
    long_description = fid.read()

setup(
    name="git-quality-check",
    version=version,
    description="A simple tool to evalute the quality of a git repository.",
    url="https://github.com/gcattan/git-quality-check",
    author="Gregoire Cattan",
    author_email="gcattan@hotmail.com",
    license="BSD (3-clause)",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Documentation": "https://github.com/gcattan/git-quality-check",
        "Source": "https://github.com/gcattan/git-quality-check",
        "Tracker": "https://github.com/gcattan/git-quality-check/issues/",
    },
    platforms="any",
    python_requires=">=3.9",
    install_requires=[],
    # extras_require={'docs': ['sphinx-gallery', 'sphinx-bootstrap_theme', 'numpydoc', 'mne', 'seaborn'],
    # 'tests': ['pytest', 'seaborn', 'flake8', 'mne', 'pooch', 'tqdm']},
    zip_safe=False,
)
