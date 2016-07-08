from jinja2 import Template
from flask import Flask

app = Flask(__name__)
	

@app.route('/')



def index():
	test = open('test.html').read()
	template = Template(test)
	
	question = 'Q1: What is the thing in the back of your throat called?'
	
	teams = ['Orange Parakeets', 'Cyan Wallabys', 'Chartreuse Flamingos']
	
	q_count = range(6)



	return template.render(question=question, teams=teams, q_count=q_count)
	
if __name__ == '__main__':
	app.run(host='0.0.0.0')
	
