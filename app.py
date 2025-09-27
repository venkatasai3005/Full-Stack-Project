from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# -----------------------------------------------------------------------------
# Flask App Configuration
# -----------------------------------------------------------------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key'  # For flashing messages. Replace in production.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -----------------------------------------------------------------------------
# Database Model
# -----------------------------------------------------------------------------
class Application(db.Model):
    __tablename__ = 'applications'

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(120), nullable=False)
    application_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False)  # Applied, Interview, Rejected, Offer
    notes = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Application {self.company_name} - {self.role}>"


# -----------------------------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------------------------
def init_db():
    """Create database tables if they don't exist."""
    with app.app_context():
        db.create_all()


def parse_date(date_str: str):
    """Parse a date in YYYY-MM-DD format, return a datetime.date or None."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


# -----------------------------------------------------------------------------
# Routes
# -----------------------------------------------------------------------------
@app.route('/')
def index():
    """Home page with links to features."""
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add_application():
    """Create a new job application record."""
    if request.method == 'POST':
        company_name = request.form.get('company_name', '').strip()
        role = request.form.get('role', '').strip()
        application_date_str = request.form.get('application_date', '').strip()
        status = request.form.get('status', '').strip()
        notes = request.form.get('notes', '').strip()

        # Server-side validation
        missing = [
            field for field, value in [
                ('Company Name', company_name),
                ('Role', role),
                ('Application Date', application_date_str),
                ('Status', status),
                ('Notes', notes),
            ] if not value
        ]
        if missing:
            flash(f"Please fill all fields: {', '.join(missing)}", 'danger')
            return redirect(url_for('add_application'))

        app_date = parse_date(application_date_str)
        if not app_date:
            flash('Invalid date format. Please use the date picker (YYYY-MM-DD).', 'danger')
            return redirect(url_for('add_application'))

        if status not in ['Applied', 'Interview', 'Rejected', 'Offer']:
            flash('Invalid status selected.', 'danger')
            return redirect(url_for('add_application'))

        new_app = Application(
            company_name=company_name,
            role=role,
            application_date=app_date,
            status=status,
            notes=notes,
        )
        db.session.add(new_app)
        db.session.commit()
        flash('Application added successfully!', 'success')
        return redirect(url_for('list_applications'))

    return render_template('add.html')


@app.route('/applications')
def list_applications():
    """List all job applications."""
    apps = Application.query.order_by(Application.application_date.desc()).all()
    statuses = ['All', 'Applied', 'Interview', 'Rejected', 'Offer']
    return render_template('applications.html', applications=apps, statuses=statuses)


@app.route('/edit/<int:app_id>', methods=['GET', 'POST'])
def edit_application(app_id):
    """Edit an existing application."""
    application = Application.query.get_or_404(app_id)

    if request.method == 'POST':
        company_name = request.form.get('company_name', '').strip()
        role = request.form.get('role', '').strip()
        application_date_str = request.form.get('application_date', '').strip()
        status = request.form.get('status', '').strip()
        notes = request.form.get('notes', '').strip()

        missing = [
            field for field, value in [
                ('Company Name', company_name),
                ('Role', role),
                ('Application Date', application_date_str),
                ('Status', status),
                ('Notes', notes),
            ] if not value
        ]
        if missing:
            flash(f"Please fill all fields: {', '.join(missing)}", 'danger')
            return redirect(url_for('edit_application', app_id=app_id))

        app_date = parse_date(application_date_str)
        if not app_date:
            flash('Invalid date format. Please use the date picker (YYYY-MM-DD).', 'danger')
            return redirect(url_for('edit_application', app_id=app_id))

        if status not in ['Applied', 'Interview', 'Rejected', 'Offer']:
            flash('Invalid status selected.', 'danger')
            return redirect(url_for('edit_application', app_id=app_id))

        application.company_name = company_name
        application.role = role
        application.application_date = app_date
        application.status = status
        application.notes = notes

        db.session.commit()
        flash('Application updated successfully!', 'success')
        return redirect(url_for('list_applications'))

    # GET
    return render_template('edit.html', application=application)


@app.route('/delete/<int:app_id>', methods=['POST'])
def delete_application(app_id):
    """Delete an application (POST-only)."""
    application = Application.query.get_or_404(app_id)
    db.session.delete(application)
    db.session.commit()
    flash('Application deleted.', 'info')
    return redirect(url_for('list_applications'))


@app.route('/stats')
def stats():
    """Dashboard showing simple counts."""
    total = Application.query.count()
    applied = Application.query.filter_by(status='Applied').count()
    interview = Application.query.filter_by(status='Interview').count()
    rejected = Application.query.filter_by(status='Rejected').count()
    offer = Application.query.filter_by(status='Offer').count()

    return render_template(
        'stats.html',
        total=total,
        applied=applied,
        interview=interview,
        rejected=rejected,
        offer=offer,
    )


# -----------------------------------------------------------------------------
# Entrypoint
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    # Ensure DB exists before starting server
    init_db()
    # Run the app in debug mode for development
    app.run(debug=True)
