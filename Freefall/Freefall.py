def getInputUser():
	person = raw_input('Username: ')
	checkUsername(person)

def getInputPass(person, count):
	password = raw_input('Password for ' + person + ': ')
	checkPassword(person, password, count)

def checkUsername(person):
	if person == 'philip':
		getInputPass(person, count = 3)
	else:
		print('Sorry, your account is unavailable at this time.')

def checkPassword(person, password, count):
  if password == 'test':
  	cmdLine()
  else:
  	if count == 0:
  		print('Too many attempts. Please contact your system administrator.')
  	else:
  		count = count - 1
  		print('Wrong password, please try again.')
  		getInputPass(person, count)

def cmdLine():
  print possibleCommands()
  text = raw_input('- ')
  if text != 'exit':
    checkCommand(text)
    cmdLine()

def possibleCommands():
  return exit, logout

def checkCommand(text):
  if text == 'logout'
  return

if __name__ == '__main__':
  getInputUser()