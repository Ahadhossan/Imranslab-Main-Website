from setuptools import setup, find_packages

setup(
    name="jira-integration",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    author="Imranul Islam",
    description="A Python package for Jira issue creation with test payloads.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
