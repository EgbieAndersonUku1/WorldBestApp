# setup files

from setuptools import setup

setup(name="WorldBestApp",
      version="1.0",
      description="Testing the login system for a web based app",
      author="Egbie",
      packages=[
          "web_utils",
          "page_object",
          "page_object.login",
          "page_object.welcome_page"
      ]

      )
