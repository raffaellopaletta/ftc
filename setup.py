from setuptools import setup

setup(name='fuzzy_text_classifier',
      version='0.1',
      description='A fuzzy classifier library for natural language text',
      url='https://github.com/raffaellopaletta/ftc',
      author='Raffaello Paletta',
      author_email='raffaellopaletta@gmail.com',
      license='MIT',
      packages=['fuzzy_text_classifier'],
      install_requires=[
            'typing'
      ],
      zip_safe=False)