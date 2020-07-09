from pyrogram import Client, Filters
import os
import subprocess
from io import StringIO
import sys
import random

app = Client("name", 
                      api_id=id,
                      api_hash="hash")
@app.on_message(Filters.text)
def hello(client, m):
	if m.from_user.id==677370194:
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
