# no linux é possivel escrever os comandos do git direto no terminal
# no windows tem que ser no terminal do git hub
# duas autenticacoes antes de comecar:
    # git config --global user.name 'serg-ht'
    # git config --global user.email 'sergiohteixeira@gmail.com'

#dois arquivos importantes:
# 1 gitignore (configura o git para ignorar alguns arquivos dentro do repositorio)

''' quando subir os arquivos no repositorio o git não vai subir as pastas que estao especificadas nesse arquivo
    por exemplo pastas .env
echo .env >> . gitignore
'''
# a outra pasta importante é o readme.txt


### AUL 6
# git it add .
# vai mandar os aqruivos para serem commitados

# git commit manda tudo para o git hub
 # git commit -m "primeiro commit"
# git push. efetua

#### aula 7 branchs
'''
 quando se cria uma branch todo codigo é o mesmo até aquela ramificacao
depois dela toda modificacao vai afetar apenas a branch e nao o codigo principal
quando quiser juntar a branch na principal usa-se o comando merge

'''

# git branch (apresenta todas as branches no seu computador)
# git branch -a (todas as branchs remotas - que estao no github)

# git checkout -b branch_aula  (cria um novo branch)

# git checkout main  (volta para a branch principal)
