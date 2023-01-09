import setuptools

setuptools.setup(
    name="batchspawner-portwrap",
    version="0.0.1",
    url="https://github.com/ryanlovett/batchspawner-portwrap",
    author="Ryan Lovett",
    author_email="rylo@berkeley.edu",
    description="Launch portwrapped command from jupyterhub's batchspawner",
    packages=setuptools.find_packages(),
    keywords=["portwrap", "batchspawner", "jupyterhub"],
    install_requires=["portwrap"],
    entry_points={
        "console_scripts": [
            "batchspawner-portwrap = batchspawner_portwrap.__main__:main",
        ]
    },
)
