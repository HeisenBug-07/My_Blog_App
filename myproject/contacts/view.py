from datetime import datetime
from flask import render_template, redirect, url_for, Blueprint
from myproject.modles import db, Contacts
from myproject.contacts.forms import ContactUs

contact_blueprint = Blueprint('Contacts', __name__, template_folder='templates/contacts')


@contact_blueprint.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactUs()
    if form.validate_on_submit():
        post = Contacts(name=form.name.data, email=form.email.data,
                        feedback=form.feedback.data, date=datetime.utcnow())
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('Posts.feedback'))
    return render_template('contact.html', form=form)
