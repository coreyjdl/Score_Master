from flask import Flask, render_template, redirect, url_for, request, send_file

from jinja2 import Template

from collections import defaultdict

app = Flask(__name__)

class DefaultList(list):

    def __init__(self, it=None, default=0):
        self.default = [default]
        list.__init__(self, it or [])

    def __setitem__(self, idx, value):
        if idx >= len(self):
            self.extend(self.default*(idx-len(self)+1))
        list.__setitem__(self, idx, value)


class TriviaSession():
	
	def __init__(self, instance_id):
		self.instance_id = instance_id #will be shared with the URL trivial.com/?session=instance_id
		self.question = ''
		self.teams = defaultdict(DefaultList)
		
	def required_column_count(self):
		return max(self.teams.values(), key=len) if self.teams else False
	
	def delete_team(self, team):
		self.teams.pop(team)
	
	def add_team(self, team):
		self.teams[team]
	
	def set_score(self, team, round, score):
	    self.teams[team][round] = score



question = ''
teams = defaultdict(DefaultList)

def get_count():
	return max(teams.values(), key=len) if teams else False

@app.route('/')
def index():
	return open('templates/index.html').read()

@app.route('/admin', methods=['GET', 'POST'])
def admin():
	global question  #fix this to be a class drawing from a databse
	
	if request.method == 'POST':
					
		question = request.form.get('question', question)
		
		new_team = request.form.get('add_team', False)
		teams[new_team] if new_team else None
			
		for data in request.form:
			teams.pop(request.form[data]) if data.startswith('del') else None
			
			if data.startswith('score'):
			
				_, team, index = data.split(',')
				index = int(index) - 1

				score = request.form[data]
				score = int(score) if score else 0
				
				if team in teams:
					teams[team][index] = score
		
			

	template = Template(open('templates/admin.html').read())
	return template.render(question=question, teams=teams, q_count=get_count())
		 	
@app.route('/score')
def score():	
	template = Template(open('templates/scores.html').read())
	return template.render(teams=teams, q_count=get_count()) if teams else ''

@app.route('/question')
def set_question():
	return question
	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
