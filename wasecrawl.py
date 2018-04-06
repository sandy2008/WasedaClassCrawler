import re
from selenium import webdriver
import time
output = open(r'output.txt','a')

showmore = "func_showchg('JAA103SubCon', '100')"
pagejs = "page_turning('JAA103SubCon','2')"

browser = webdriver.PhantomJS()
browser.get('https://www.wsl.waseda.jp/syllabus/JAA103.php')

p = '20\d\d.{5,10000}?</td>\\n</tr>\\n'
p = re.compile(p, re.S)

pdelete = r'<.*?>'
pdelete = re.compile(pdelete)

time.sleep(0.5)

browser.execute_script(showmore)

for i in range(5):
	match = p.findall(browser.page_source)
	for t in match:
		t = re.sub(pdelete, '', t)
		output.write(t)
	browser.execute_script(pagejs)
	time.sleep(0.5)
	
output.close()