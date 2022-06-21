from setuptools import setup, find_namespace_packages

setup(
    name='lw',
    version='1',
    python_requires='>=3.8',
    author='Alex Cannan',
    author_email='alexfcannan@gmail.com',
    packages=find_namespace_packages(include=['lw.*', 'lw']),
    long_description="the best band in new york",
    install_requires=[
        "loguru",
        "fastapi",
        "gunicorn",
        "uvicorn[standard]",
        "jinja2"
    ],
)
