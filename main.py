chaves = {
    'Nome': input(f'Infome o nome do usuário: '),
    'CPF': input(f'Infome o CPF do usuário: '),
    'RG': input(f'Infome o RG do usuário: '),
    'Data de Nascimento': input(f'Infome a Data de Nascimento do usuário: '),
    'Gênero': input(f'Infome o Gênero do usuário: '),
    'E-mail': input(f'Infome o E-mail do usuário: '),
    'Tipo sanguíneo': input(f'Infome o Tipo sanguíneo do usuário: '),
    'Profissão': input(f'Infome a Profissão do usuário: '),
    'Empresa': input(f'Infome a Empresa que o usuario trabalha: ')

}

for chave in chaves:
    print(chaves.get(chave))