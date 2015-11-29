"""
    Testes de internacionalização
"""

import gettext

x = gettext.bindtextdomain('mensagens')

print(x)

_ = gettext.gettext
print(_('this'))

