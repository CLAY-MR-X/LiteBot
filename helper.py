from pyrogram import Client, filters
import os
import subprocess
from io import StringIO
import sys
import random

#как получить апи айди и апи хеш читайте тут https://docs.pyrogram.org/intro/setup

global you_id

you_id=Ваш айди аккаунта

app = Client("name", 
                      api_id=Ваш апи айди,
                      api_hash="ваш апи хеш")
@app.on_message(filters.text, filters.me)
def hello(client, m):
	if "py3" in m.text.lower():
		script=m.text.replace("py3 ", "")
		old_stdout = sys.stdout
		result = sys.stdout = StringIO()
		exec(script)
		sys.stdout = old_stdout 
		m.edit(f'''**code**:
	
```{script}```
	
**result**:
	
```{result.getvalue()}```
''')
	if "bash" in m.text.lower():
		test1=m.text.replace("bash ", "")
		script=test1.format(m, app)
		test=os.popen(f'''{script}''').read()
		m.edit(f'''**code**:
	
```{script}```
	
**result**:
	
```{test}```
	''')
	if 'bind ' in  m.text:
		reply=m.reply_to_message
		params=m.text.replace('bind ', '')
		try:
			save=open('binds/'+params+'.py', 'w')
			save.write(reply.text)
			save.close()
			m.edit('**Бинд успешно настроен!**')
		except Exception as e:
			print(e)
			
	else:
		files=os.listdir('binds')
		for file in files:
			if file.replace('.py', '') in m.text[:len(file.replace('.py', ''))]:
				ok=open('binds/'+file, 'r')
				script=ok.read()
				reply=m.reply_to_message
				exec(script)
				ok.close()
					
app.run()
