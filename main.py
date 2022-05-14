fileName = './/sys_test//sys_test_main.py'
#.//Jan//Jan_2-1.py
#.//Jakob//Jakob_1.py
#.//Jan//Vergleich//Main.py

with open(fileName, 'rb') as source_file:
  code = compile(source_file.read(), fileName, "exec")

exec(code)
