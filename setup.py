import setuptools


requirements = []
with open('requirements.txt', 'r') as f:
    for line in f:
        requirements.append(line.strip())

requirements.append(
    "submodule_practice_parent "
    "@ git+ssh://git@"
    "github.com/nabenabe0928/submodule_practice_parent"
    "@v0.0.1#egg=submodule_practice_parent"
)

setuptools.setup(
    name="submodule_practice_child",
    version="0.0.1",
    author="nabenabe0928",
    author_email="shuhei.watanabe.utokyo@gmail.com",
    url="https://github.com/nabenabe0928/submodule_practice_child",
    packages=setuptools.find_packages(),
	python_requires='>=3.8',
    platforms=['Linux'],
    install_requires=requirements,
    include_package_data=True,
    ext_modules=[setuptools.Extension]
)
