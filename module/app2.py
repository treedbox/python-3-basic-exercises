from foobar import bar


bar()
# Bar text from module foobar

print(bar)
# <function bar at 0x7fbb71784378>


# foo()
# NameError: name 'foo' is not defined
# soluction include foo at import statemenet
# from foobar import foo, bar

# print(foo)
# NameError: name 'foo' is not defined

# foobar.foo()
# AttributeError: 'function' object has no attribute 'foo'

# foobar.bar()
# AttributeError: 'function' object has no attribute 'bar'
