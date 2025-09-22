from setuptools import setup, find_packages

setup(
    name="chomu",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["psutil", "tabulate", "termcolor"],
    entry_points={
        "console_scripts": [
            "chomu=chomu.main:main",
        ],
    },
    author="MrAashish0x1",
    description="Linux Service Manager CLI tool",
    python_requires=">=3.8",
)
