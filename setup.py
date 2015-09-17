from numpy.distutils.core import setup, Extension

wrapper = Extension('fwrapper', sources=['fib1.f'], libraries=['my_module'])

setup(
    name='fortranwrap',
    version='0.1',
    libraries = [('my_module', dict(sources=['fib1.f'],
                                    extra_f90_compile_args=["-ffixed-form"]))],
    ext_modules = [wrapper]
)

