from foobar import bar, foo


bar()
# Bar text from module foobar

print(bar)
# <function bar at 0x7fbb71784378>
# 0x7fbb71784378 memory adress

foo()
# Foo text from module foobar

print(foo)
# <function foo at 0x7f18dc676ec0>

# print(foo)
# NameError: name 'foo' is not defined

# foo.foo()
# AttributeError: 'function' object has no attribute 'foo'

# foo.bar()
# AttributeError: 'function' object has no attribute 'bar'
