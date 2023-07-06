from setuptools import setup, find_packages

setup(
    name='news_processor',
    version='0.0.1',
    description='News processors with NLP',

    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,

    install_requires=[
        'bs4==0.0.1',
        'requests==2.22.0',
        'numpy==1.17.3',
        'scipy==1.10.0',
        'scikit-learn==0.21.3',
        'konlpy==0.5.1'
    ],
)
