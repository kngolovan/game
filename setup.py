from setuptools import setup, find_packages


setup(
    name="My Application",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "alembic==1.4.3",
        "flask==1.1.2",
        "flask-sqlalchemy==2.4.4",
        "gunicorn==20.0.4",
        "psycopg2==2.8.6",
        "python-dotenv==0.15.0",
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
