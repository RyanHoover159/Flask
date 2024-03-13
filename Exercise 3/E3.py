from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global dictionary to store registered users
registered_users = {}

# List of hardcoded student organizations
student_organizations = ['Organization A', 'Organization B', 'Organization C', 'Organization D', 'Organization E']

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        organization = request.form['organization']

        # Backend validation
        if not name:
            return render_template('home.html', error='Name is required.', organizations=student_organizations)
        if organization not in student_organizations:
            return render_template('home.html', error='Invalid organization.', organizations=student_organizations)

        registered_users[name] = organization
        return redirect(url_for('registered_users'))
    
    return render_template('home.html', organizations=student_organizations)

@app.route('/registered_users')
def registered_users():
    return render_template('registered_users.html', users=registered_users)

if __name__ == '__main__':
    app.run(debug=True)
