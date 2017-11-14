from setuptools import setup, find_packages

# Try to convert markdown README to rst format for PyPI.
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='ontraportlib',
    version='1.2.1',
    description='<p>Enter your App ID and API Key above. If you do not have an App ID or API Key login to your ONTRAPORT account and navigate <a href="https://app.ontraport.com/#!/api_settings/listAll">here</a>. Authentication parameters must be sent in the request header as <strong>Api-Appid</strong> and <strong>Api-Key</strong>. Each ONTRAPORT account is allowed up to 180 requests per minute.</p>',
    long_description=long_description,
    author='Shahid Khaliq',
    author_email='shahid.khaliq@apimatic.io',
    url='https://apimatic.io/',
    packages=find_packages(),
    install_requires=[
        'requests>=2.9.1, <3.0',
        'jsonpickle>=0.7.1, <1.0',
        'cachecontrol>=0.11.7, <1.0',
        'python-dateutil>=2.5.3, <3.0'
    ],
    tests_require=[
        'nose>=1.3.7'
    ],
    test_suite = 'nose.collector'
)