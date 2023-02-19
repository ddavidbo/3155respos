from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

ORGANIZATIONS = ["Organization A", "Organization B", "Organization C", "Organization D", "Organization E"]

registered_users = {}

@app.route('/')
def home():
    return render_template('home.html', organizations=ORGANIZATIONS)

@app.route('/users')
def users():
    return render_template('users.html', users=registered_users)

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    organization = request.form['organization']
    
    if not name:
        error = "Name is required."
    elif not organization:
        error = "Organization is required."
    elif organization not in ORGANIZATIONS:
        error = "Invalid organization."
    elif name in registered_users:
        error = "Name already registered."
    else:
        registered_users[name] = organization
        return redirect(url_for('users'))
    
    return render_template('home.html', organizations=ORGANIZATIONS, error=error, name=name, organization=organization)

@app.route('/layout')
def layout():
    return render_template('layout.html')

if __name__ == '__main__':
    app.run(debug=True)
