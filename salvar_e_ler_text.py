while True:
 o=input('1:add 2:ler 3:sair\n')
 if o=='1':open('t.txt','a').write(input('t:')+'\n')
 elif o=='2':print(open('t.txt','r').read())
 elif o=='3':break