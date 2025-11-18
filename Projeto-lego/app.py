from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)

@app.route('/')
def index():
return render_template('index.html', team=TEAM, projects_count=len(PROJECTS))




@app.route('/projects')
def projects():
return render_template('projects.html', projects=PROJECTS)




@app.route('/fll')
def fll():
season = 2025
return render_template('fll.html', season=season)




@app.route('/go-to-projects')
def go_to_projects():
return redirect(url_for('projects'))




if __name__ == '__main__':
app.run(debug=True)