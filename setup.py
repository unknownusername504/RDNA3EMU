from setuptools import setup

setup(
    name='rdna3emu',
    version='0.0.1',
    license='MIT',
    packages=['rdna3emu'],
    install_requires=[
        'numpy', 'ply'
    ],
    python_requires='>=3.8',
)