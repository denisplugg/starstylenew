from app import db,app
from CARDdatabase import ForeignCelebrities, ForeignOutfits, CISCelebrities, CISOutfits, RuBrands, RuOutfits
from ALLSTARSdatabase import AllStars


def add_foreign_celebrity(celebrity_name, celebrity_img, unique_id):
    
    new_foreign_celebrity = ForeignCelebrities(celebrity_name=celebrity_name, celebrity_img=celebrity_img, unique_id=unique_id)

    try:
        db.session.add(new_foreign_celebrity)
        db.session.commit()
        print(f'Foreign Celebrity {celebrity_name} added successfully.')
    except Exception as e:
        db.session.rollback()
        print(f'Error adding foreign celebrity: {str(e)}') 


def add_foreign_outfit(outfit_item, price, item_img, celebrity_id):
    new_foreign_outfit = ForeignOutfits(outfit_item=outfit_item, price=price, item_img=item_img, celebrity_id=celebrity_id)

    try:
        db.session.add(new_foreign_outfit)
        db.session.commit()
    except Exception as e:
        db.session.rollback()  
        print(f'Error adding foreign outfit: {str(e)}') 

def add_cis_celebrity(celebrity_name, celebrity_img, unique_id):
    new_cis_celebrity = CISCelebrities(celebrity_name=celebrity_name, celebrity_img=celebrity_img, unique_id=unique_id)

    try:
        db.session.add(new_cis_celebrity)
        db.session.commit()
        print(f'CIS Celebrity {celebrity_name} added successfully.')
    except Exception as e:
        db.session.rollback()
        print(f'Error adding cis celebrity: {str(e)}') 


def add_cis_outfit(outfit_item, price, item_img, celebrity_id):
    new_cis_outfit = CISOutfits(outfit_item=outfit_item, price=price, item_img=item_img, celebrity_id=celebrity_id)

    try:
        db.session.add(new_cis_outfit)
        db.session.commit()
        print(f'CIS Outfit {outfit_item} added successfully.')
    except Exception as e:
        db.session.rollback()
        print(f'Error adding cis outfit: {str(e)}')


def add_ru_brand(brand_name, brand_logo, unique_id):
    new_ru_brand = RuBrands(brand_name=brand_name, brand_logo=brand_logo, unique_id=unique_id)

    try:
        db.session.add(new_ru_brand)
        db.session.commit()
        print(f'RU Brand {brand_name} added successfully.')
    except Exception as e:
        db.session.rollback()
        print(f'Error adding ru brand: {str(e)}')

def add_ru_outfit(outfit_item, price, item_img, brand_id):
    new_ru_outfit = RuOutfits(outfit_item=outfit_item, price=price, item_img=item_img, brand_id=brand_id)

    try:
        db.session.add(new_ru_outfit)
        db.session.commit()
        print(f'RU Outfit {outfit_item} added successfully.')
    except Exception as e:
        db.session.rollback()
        print(f'Error adding ru outfit: {str(e)}')

def add_star(name, description, image_url, nation):
    new_star = AllStars(name=name, description=description, image_url=image_url, nation=nation)

    try:
        db.session.add(new_star)
        db.session.commit()
        print(f'Star {name} added successfully.')
    except Exception as e:
        db.session.rollback()
        print(f'Error adding star: {str(e)}')


if __name__ == '__main__':
    with app.app_context():
        add_star('Fable','F | ABLE — бренд, ориентированный на исследовательскую культуру, эксперименты и функциональность. В основе нашей работы лежит идеальный баланс между инновациями и практичностью, между изучением материалов и рациональным подходом к дизайну. Наш ассортимент включает премиальные изделия, разработанные с учетом мультидисциплинарного подхода к дизайну. В собственной лаборатории мы контролируем каждый этап производства, добиваясь безупречного качества и идеального воплощения наших идей.','',3)
        