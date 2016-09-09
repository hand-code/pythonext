from distutils.core import setup, Extension

module1 = Extension('cepoll',
                    sources=['epoll.c'],
                    include_dirs=['/usr/local/include'],
                    # libraries=['tcl83'],
                    library_dirs=['/usr/local/lib'])

setup(
    author='nbboy',
    name='cepoll',
    version='1.0',
    description='epoll support',
    ext_modules=[module1])
