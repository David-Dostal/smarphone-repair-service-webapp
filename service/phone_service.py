from database.database import get_db



class PhoneService:
    
    @staticmethod
    def get_all():
        db = get_db()
        sql = "SELECT * FROM phones "
        return db.execute(sql).fetchall()

    

    @staticmethod
    def insert_phone(labour_intensity, name, type, user_id_employee, processors_id_processor, cases_id_case, batteries_id_battery, manufacture_price, final_price, img=None):
        db = get_db()
        db.execute(
            'INSERT INTO phones (labour_intensity, name , type,  user_id_employee, processors_id_processor, cases_id_case, batteries_id_battery, manufacture_price, final_price, img) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            [labour_intensity, name , type, user_id_employee, processors_id_processor, cases_id_case, batteries_id_battery, manufacture_price, final_price,img]
        )
        
        db.commit()

    

    