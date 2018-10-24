"""Concatenation."""


def bar(name, times):
    """Hello many times in many languages."""
    print('Hello', name, times, 'times!')  # it's not concatenated but seems like
    print('Hallo %s %s mal!' % (name, times))
    print('Bonjour ' + name + ' ' + str(times) + ' fois!')
    print('こんにちは {name} {times}回!'.format(name=name, times=times))
    print('Kon\'nichiwa %(name)s %(times)s-kai!' % {'name': name, 'times': times})
    print('Olá %(name)s %(times)s vezes!' % locals())


bar('Treedbox', 10)
# Hello Treedbox 10 times!
# Hallo Treedbox 10 mal!
# Bonjour Treedbox 10 fois
# こんにちは Treedbox 10回!
# Kon'nichiwa Treedbox 10-kai!
# Olá Treedbox 10 vezes!
