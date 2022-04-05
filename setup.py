from setuptools import setup


setup(
    name='cldfbench_martinovicgothun',
    py_modules=['cldfbench_martinovicgothun'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'martinovicgothun=cldfbench_martinovicgothun:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
