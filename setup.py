from setuptools import setup, find_packages

setup(name="tap-drip",
      version="0.0.1",
      description="Singer.io tap for extracting data from drip API",
      author="Stitch",
      url="http://singer.io",
      classifiers=["Programming Language :: Python :: 3 :: Only"],
      py_modules=["tap_drip"],
      install_requires=[
        "singer-python==6.8.0",
        "requests==2.32.5",
        "backoff==2.2.1",
        "parameterized"
      ],
      entry_points="""
          [console_scripts]
          tap-drip=tap_drip:main
      """,
      packages=find_packages(),
      package_data = {
          "tap_drip": ["schemas/*.json"],
      },
      include_package_data=True,
)
