from setuptools import setup, find_packages


setup(
    name="My Application",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["flask"],
    extras_require={
        "ci": ["black", "pytest", "pytest-sugar", "pytest-cov", "pylint"]
    },
)
