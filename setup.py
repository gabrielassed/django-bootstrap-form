from setuptools import find_packages, setup

from bootstrapform.meta import VERSION

setup(
    name="django-bootstrap-form",
    version=str(VERSION),
    description="django-bootstrap-form",
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="bootstrap,django",
    author="tzangms",
    author_email="tzangms@gmail.com",
    url="http://github.com/tzangms/django-bootstrap-form",
    license="MIT",
    test_suite="runtests.runtests",
    install_requires=["django>=1.5", "packaging>=20.0"],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
