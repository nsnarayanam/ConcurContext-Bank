
from setuptools import setup, find_packages

setup(
    name='concurcontext',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'streamlit>=1.32.0',
    ],
    entry_points={
        'console_scripts': [
            'concurcontext = streamlit_app:main',
        ],
    },
)
