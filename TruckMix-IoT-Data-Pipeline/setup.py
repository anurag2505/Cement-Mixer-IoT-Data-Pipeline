from setuptools import setup, find_packages

setup(
    name='Cement-Mixer-IoT-Data-Pipeline',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Add your project dependencies here
        'pandas',
        'numpy',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            # Add command line scripts here
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A data pipeline for Cement Mixer IoT data',
    url='https://github.com/yourusername/Cement-Mixer-IoT-Data-Pipeline',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)