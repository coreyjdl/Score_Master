from flask import Flask, render_template, redirect, url_for, request, send_file

from jinja2 import Template

app = Flask(__name__)

question = ''
teams = {}


def get_count():
	return range(max(len(teams[team]) for team in teams) if teams else False

@app.route('/')
def index():
	return open('templates/index.html').read()

@app.route('/admin', methods=['GET', 'POST'])
def admin():
	global question
	if request.method == 'POST':
		# FOR DEBUGING FORM 
		# for key, value in request.form.items():
			# print(key, value )
		# FOR DEBUGING FORM 
		
		if request.form.get('question', False):
			question = request.form['question']
		
		if request.form.get('add_team', False):
			teams[request.form['add_team']] = []
			
		for data in request.form:
			if data[:5] == 'score':
				edit = data.split(',')
				team = edit[1]
				index = int(edit[2])
				score = request.form[data]
				if team in teams:
					if score != '':
						if (index - 1) == len(teams[team]):
							teams[team].append(score)
						else:
							teams[team][index - 1] = score
				
			if data[:3] == 'del':
				del teams[request.form[data]]
			
	template = Template(open('templates/admin.html').read())
	
	return template.render(question=question, teams=teams, q_count=get_count())
		 	
@app.route('/score')
def score():	
	if teams:
		template = Template(open('templates/scores.html').read())

		return template.render(teams=teams, q_count=get_count())
	else:
		return ''

@app.route('/question')
def question():
	return question or ''

if __name__ == '__main__':
	app.run(host='0.0.0.0')
