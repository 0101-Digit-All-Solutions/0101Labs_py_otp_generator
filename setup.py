from setuptools import setup, find_packages

setup(
    name='0101Labs_py_otp-generator',
    version='1.0.0',
    description='A Python library for generating OTPs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='0101 Digit All',
    author_email='technology@0101digitall.com',
    url='https://github.com/0101-Digit-All-Solutions/-0101Labs-py_otp_generator',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
