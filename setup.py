from setuptools import setup, find_packages


setup(
    version="0.0.11",
    name="aiodynamo",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "attrs>=17.4.0",
        "aiobotocore>=0.10.0",
        "boto3>=1.9.49",
        "aiohttp>=3.5.4",
    ],
)
