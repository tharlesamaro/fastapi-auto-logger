from setuptools import setup


setup(
    name='fastapi_auto_logger',
    description="This package offers a simple and automated solution for logging unhandled errors in FastAPI applications. The package includes a custom logger that automatically captures unhandled errors and logs them to a log file.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    version='0.0.1',
    author='Tharles Amaro',
    author_email='tharlesamaro@gmail.com',
    url="https://github.com/tharlesamaro/fastapi-auto-logger",
    license='MIT',
    keywords=["fastapi", "http", "auto", "api", "logger", "file", "log", "python"],
    packages=['fastapi_auto_logger', 'tests'],
    install_requires=[
        'fastapi',
    ],
    extras_require={
        'dev': [
            'pytest',
            'flake8',
            'mypy',
            'black'
        ]
    },
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 4 - Beta',
        "Environment :: Web Environment",
        'License :: OSI Approved :: MIT License',
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development",
        "Typing :: Typed",
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        'Programming Language :: Python',
    ],
    
)
