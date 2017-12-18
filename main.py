print('Welcome To My First Script\n'
      '           By\n'
      '          G30P\n')

print('      Version = 0.1\n')
print('      Coded = G30P\n')

x = input('Add Your Target IP!! ')
print('Target IP set to ' + x )

saveFile = open('Target.txt','w')
saveFile.write(x)
saveFile.close()

