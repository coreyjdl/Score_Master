from jinja2 import Template



with open('templates/admin.html') as file:
	t = Template(file.read())
	print(t.render(question='', teams={}, q_count=''))