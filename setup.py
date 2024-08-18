from setuptools import setup, find_packages

setup(
    name='assistant_bot',
    version='0.1.0',
    description='A console bot to assist you manage the contacts and notes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/bilousbv/project-team-5',
    packages=find_packages(),
    install_requires=[
        'colorama==0.4.6',
        'prettytable==3.11.0',
        'pyreadline3==3.4.1',
        'wcwidth==0.2.13',
        'setuptools==72.2.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'assistant_bot=assistant_bot.main:main',
        ],
    },
)