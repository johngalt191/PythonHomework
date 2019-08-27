from setuptools import setup

setup(
    name='pycalc',  # Required
    version='1.0',  # Required
    description='Pure-python command-line calculator.',  # Optional
    url='https://github.com/johngalt191/PythonHomework',  # Optional
    author='ALIAKSANDR REPIKAU',  		# Optional
    author_email='adgomel@gmail.com',  	# Optional
    py_modules=["pycalc"],			# Required
    entry_points={'console_scripts': ['pycalc=pycalc:main', ], },
    # packages=['pycalc_project']		# Required
    # python_requires='>3.0, <3.7'
    )
