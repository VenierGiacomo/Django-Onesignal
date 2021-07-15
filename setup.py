from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Apple :: macOs :: macOs Big Sur 11.2.3',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='django-onesignal',
  version='1.0.0',
  description='An interface to send push notification (both mobile and web) from Django using',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Giacomo Venie',
  author_email='giacomo.venier@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='django, onesignal', 
  packages=find_packages(),
  install_requires=['requests, json, datetime'] 
)
