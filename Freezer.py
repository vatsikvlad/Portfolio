from flask_frozen import Freezer
from Main import app

app.config['FREEZER_RELATIVE_URLS'] = True
freezer: Freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()