n = input('Digite algo: ')
print(' Faz parte do alfabeto ? {0}'
      ' Faz parte de cadeia de números ? {1}'
      ' Faz parte de cadeia de alfanumérico ? {2}'
      ' Está em caixa alta? {3}'
      ' Está em caixa baixa ? {4}'
      ' É printável? {5}'
      ' Tipo é : {6}'.format(n.isalpha(),
                    n.isnumeric(),
                    n.isalpha(),
                    n.isupper(),
                    n.islower(),
                    n.isprintable(),
                    type(n)))