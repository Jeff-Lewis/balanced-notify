from setuptools import setup


install_requires=[
    'Flask==0.10',
    'simplejson==3.3',
    'jsonschema==2.2.0',
    'flask-mongoengine==0.7.0',
    'wtforms==1.0.5',
]

setup(
    name='balanced_notify',
    version='0.0.1',
    url='http://github.com/balanced/balanced-notify/',
    license='MIT',
    author='Balanced',
    author_email='dev+balanced-notify@balancedpayments.com',
    long_description=__doc__,
    packages=['notify'],
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
    platforms='any',
)
