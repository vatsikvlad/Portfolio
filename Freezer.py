from flask_frozen import Freezer
from Main import app

freezer: Freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()