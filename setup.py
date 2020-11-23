from setuptools import setup, find_packages


setup(
    name="My Application",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "alembic",
        "flask",
        "flask-sqlalchemy",
        "psycopg2-binary",
        "python-dotenv",
    ],
    extras_require={
        "ci": [
            "black",
            "coveralls",
            "pytest",
            "pytest-cov",
            "pylint",
            "pylint_flask",
            "pylint_flask_sqlalchemy",
        ]
    },
)
