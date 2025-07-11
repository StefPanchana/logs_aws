from setuptools import setup, find_packages

setup(
    name="logs-aws-client",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
        "python-dotenv>=1.0.0"
    ],
    author="AWS Team",
    description="Cliente para microservicio de logs AWS",
    python_requires=">=3.8"
)