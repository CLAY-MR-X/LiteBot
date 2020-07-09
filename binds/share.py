import os
file=m.text.replace('share ', '')
files=os.listdir('binds')
if file+'.py' in files:
  app.send_document(m.chat.id, f'binds/{file}.py')
  m.edit('**Бинд успешно отправлен**')
else:
  m.edit('**Такого бинда нету**')