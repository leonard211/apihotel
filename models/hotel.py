from con_sql import bd

class HotelModel(bd.Model):
    __tablename__ = "utilizadores"
    user_id = bd.Column(bd.String, primary_key = True)
    nome = bd.Column (bd.String(80))
    estrelas = bd.Column (bd.Float(precision = 1))
    diaria = bd.Column (bd.Float(precision = 2))
    cidade = bd.Column (bd.String(40))

    # Construtor da classe 
    def __init__(self,hotel_id,nome,estrelas,diaria,cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def json(self):
        return{
            "hotel_id": self.hotel_id,
            "nome" : self.nome,
            "estrelas" : self.estrelas,
            "diaria": self.diaria,
            "cidade": self.cidade
        }

    @classmethod
    def find_hotel(cls,id_hotel):
        hotel= cls.query.filter_by(hotel_id = id_hotel).first()
        if hotel:
            return hotel
        return None
    
    def save_hotel(self):
        bd.session.add(self)
        bd.session.commit()
        
    def delete_hotel(self):
        bd.session.delete(self)
        bd.session.commit()
        
    def update_hotel(self, nome_atualizado,estrelas_atualizadas,diaria_atualizada,cidade_atualizada):
        self.nome = nome_atualizado
        self.estrelas = estrelas_atualizadas
        self.diaria = diaria_atualizada
        self.cidade = cidade_atualizada



        











        from con_sql import bd

class HotelModel(bd.Model):
    __tablename__ = "hoteis"
    hotel_id = bd.Column(bd.String, primary_key=True, autoincrement=True)
    username = bd.Column (bd.String(40))
    password = bd.Column (bd.String(40))
    

    # Construtor da classe 
    def __init__(self,username,password):
        self.hotel_id = username
        self.nome = password

    def json(self):
        return{
            "user_id": self.user_id,
            "username" : self.username,
            "password" : self.password,
        }

    @classmethod
    def find_hotel(cls,username):
        user= cls.query.filter_by(username=username).first()
        if user:
            return user
        return None
    
    def save_user(self):
        bd.session.add(self)
        bd.session.commit()
        
    def delete_user(self):
        bd.session.delete(self)
        bd.session.commit()
        
   

    