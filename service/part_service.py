from database.database import get_db


class PartService:


    @staticmethod
    def get_batteries():
        db = get_db()
        return db.execute(
            "SELECT id_battery, name FROM batteries",
            
        ).fetchall()

    @staticmethod
    def get_cases():
        db = get_db()
        return db.execute(
            "SELECT id_case, name FROM cases",
            
        ).fetchall()

    @staticmethod
    def get_processors():
        db = get_db()
        return db.execute(
            "SELECT id_processor, name FROM processors",
            
        ).fetchall()


    @staticmethod
    def get_battery_price_by_id(id):
        db = get_db()
        return db.execute(
            "SELECT price FROM batteries WHERE id_battery = ?",
            [id]
        ).fetchone()

    @staticmethod
    def get_case_price_by_id(id):
        db = get_db()
        return db.execute(
            "SELECT price FROM cases WHERE id_case = ?",
            [id]
        ).fetchone()

    @staticmethod
    def get_processor_price_by_id(id):
        db = get_db()
        return db.execute(
            "SELECT price FROM processors WHERE id_processor = ?",
            [id]
        ).fetchone()

    @staticmethod
    def get_all_processors():
        db = get_db()
        return db.execute(
            "SELECT * FROM processors",
            
        ).fetchall()

    @staticmethod
    def get_all_batteries():
        db = get_db()
        return db.execute(
            "SELECT * FROM batteries",
            
        ).fetchall()

    @staticmethod
    def get_all_cases():
        db = get_db()
        return db.execute(
            "SELECT * FROM cases",

        ).fetchall()