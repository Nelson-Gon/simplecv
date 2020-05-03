from setuptools import setup, find_packages
setup(name='pyautocv',
      version="0.2.0",
      description='(Semi) Automated Image Processing',
      url="http://www.github.com/Nelson-Gon/pyautocv",
      author='Nelson Gonzabato',
      author_email='gonzabato@hotmail.com',
      license='MIT',
      keywords="image-data image-analysis computer-vision image-processing",
      packages=find_packages(),
      long_description=open('README.md', encoding="UTF-8").read(),
      scripts=['examples/example.py'],
      long_description_content_type='text/markdown',
      install_requires=['scikit-image', 'scipy', 'matplotlib', 'opencv-python'],
      zip_safe=False,
      python_requires='>=3.6',
      include_package_data=True)
