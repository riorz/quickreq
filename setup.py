from distutils.core import setup

setup(
    name='quickReq',
    version='0.0.1',
    author='Rio Lin',
    description='Simple tool to update requirements.',
    url='https://github.com/riorz/quickreq',
    packages=['quickreq'],
    entry_points={
        'console_scripts': [
            'quickreq = quickreq.command_line:main',
        ],
    }
)
