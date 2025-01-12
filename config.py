from database.database import db
from database.insert import insert_filiais, cursor
from database.create import create_filiais 

def configure_all():
    configure_db()
    
def configure_db():
    db
    create_filiais()
    insert_filiais()
    db.commit()
    cursor.close()
    db.close()