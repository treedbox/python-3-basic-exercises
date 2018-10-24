import foo as f

# print(foo)
# NameError: name 'foo' is not defined

print(f)
# <module 'foo' from '/home/treedbox/treedbox/dev/python/python.1.0.0/python/module/import/as/foo.py'>

print(f.foo())
# Foo text from module foo
# None
# None is because the return is a print() inside another print()

f.bar()
# Foo text from module foo

f.foo()
# Bar text from module foo
