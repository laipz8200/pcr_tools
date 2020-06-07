from app import create_app, db
from app.models import Icon

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Icon': Icon}
