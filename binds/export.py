import os
file=m.text.replace('export', '')
files=os.listdir('binds')

if m.reply_to_message.document.file_name in files:
  m.edit('**Бинд с таким именем уже есть**')
else:
  app.download_media(m.reply_to_message, file_name='binds/'+m.reply_to_message.document.file_name)
  m.edit('**Бинд успешно загружен**')