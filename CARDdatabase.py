from database import db


class ForeignCelebrities(db.Model):
    __tablename__ = 'foreign_celebrities'
    __searchable__ = ['celebrity_name']

    id = db.Column(db.Integer, primary_key=True)
    celebrity_name = db.Column(db.String(100), nullable=False)
    celebrity_img = db.Column(db.String(200), nullable=False)
    unique_id = db.Column(db.String(100), nullable=False, unique=True)
    outfits = db.relationship('ForeignOutfits', backref='celebrities', lazy=True)

    def __repr__(self):
        return f'<ForeignCelebrities {self.celebrity_name}>'


class ForeignOutfits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    outfit_item = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    item_img = db.Column(db.String(200), nullable=False)
    celebrity_id = db.Column(db.Integer, db.ForeignKey('foreign_celebrities.id'), nullable=False)
    link = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<ForeignOutfits {self.outfit_item}>'


class CISCelebrities(db.Model):
    __tablename__ = 'cis_celebrities'
    __searchable__ = ['celebrity_name']

    id = db.Column(db.Integer, primary_key=True)
    celebrity_name = db.Column(db.String(100), nullable=False)
    celebrity_img = db.Column(db.String(200), nullable=False)
    unique_id = db.Column(db.String(100), nullable=False, unique=True)
    outfits = db.relationship('CISOutfits', backref='celebrities', lazy=True)

    def __repr__(self):
        return f'<CISCelebrities {self.celebrity_name}>'


class CISOutfits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    outfit_item = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    item_img = db.Column(db.String(200), nullable=False)
    celebrity_id = db.Column(db.Integer, db.ForeignKey('cis_celebrities.id'), nullable=False)
    link = db.Column(db.String(200))

    def __repr__(self):
        return f'<CISOutfits {self.outfit_item}>'


class RuBrands(db.Model):
    __tablename__ = 'ru_brands'
    __searchable__ = ['brand_name']

    id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String(100), nullable=False)
    brand_img = db.Column(db.String(200), nullable=False)
    unique_id = db.Column(db.String(100), nullable=False, unique=True)
    outfits = db.relationship('RuOutfits', backref='brands', lazy=True)

    def __repr__(self):
        return f'<RuBrands {self.brand_name}>'


class RuOutfits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    outfit_item = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    item_img = db.Column(db.String(200), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('ru_brands.id'), nullable=False)
    link = db.Column(db.String(200))

    def __repr__(self):
        return f'<RuOutfits {self.outfit_item}>'
    
favorites = db.Table('favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('celebrity_id', db.Integer, db.ForeignKey('foreign_celebrities.id'), primary_key=True)
    )