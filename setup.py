import setuptools

setuptools.setup(
    name="jupyterhub-portwrap",
    version="0.0.1",
    url="https://github.com/ryanlovett/jupyterhub-portwrap",
    author="Ryan Lovett",
    author_email="rylo@berkeley.edu",
    description="Launch portwrapped command from jupyterhub spawner",
    packages=setuptools.find_packages(),
    keywords=["portwrap", "batchspawner"],
    install_requires=["portwrap"],
    entry_points={
        "console_scripts": [
            "jupyterhub-portwrap = jupyterhub_portwrap.__main__:main",
        ]
    },
)
