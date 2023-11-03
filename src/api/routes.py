"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, Users, Authors, Members, Advisors, Followers, CategoryServices, Services, ShoppingCarts, ShoppingCartItems, Bills, BillItems, BillingIssues, Posts, Media, Likes, Comments, ReportPosts
from api.utils import generate_sitemap, APIException
from datetime import datetime


api = Blueprint('api', __name__)


@api.route('/users', methods=['GET', 'POST']) 
def handle_users():
    if request.method == 'GET':
        users = db.session.execute(db.select(Users))
        users_list = [user.serialize() for user in users]
        response_body = {'message': 'User List', 
                         'results': users_list}
        return response_body, 200 
    if request.method == 'POST':
        data = request.get_json()
        user = Users(id=data['id'],
                     email=data['email'], 
                     password=data['password'], 
                     is_active=True, 
                     is_admin=True)
        db.session.add(user)
        db.session.commit()
        response_body = {'message': 'User created', 
                         'results': user.serialize()}
        return response_body, 201


@api.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_user_id(user_id):
    # User = db.session.execute(db.select(Users).filter_by(user_id=user_id)).scalar_one() 
    # if user is None:
    #    response_body = {'message': 'User not found'}
    #    return response_body, 404
    user = db.one_or_404(db.select(Users).filter_by(id=user_id), 
                         description=f"User not found , 404.")
    if request.method == 'GET':
        response_body = {'message': 'User', 
                         'results': user.serialize()}
        return response_body, 200
    if request.method == 'PUT':
        data = request.get_json()
        user.email = data['email']
        user.password = data['password']
        user.is_active = data['is_active']
        user.is_admin = data['is_admin']
        db.session.commit()
        response_body = {'message': 'User updated', 
                         'results': user.serialize()}
        return response_body, 200
    if request.method == 'DELETE':
        user.is_active = False
        db.session.commit()
        response_body = {'message': 'User inactived'}
        return response_body, 200
       

@api.route('/authors', methods=['GET', 'POST']) 
def handle_authors():
    if request.method == 'GET':
        authors = db.session.execute(db.select(Authors)) 
        authors_list = [author.serialize() for author in authors]
        response_body = {'message': 'Author list', 
                         'results': author_list}
        return response_body, 200 
    if request.method == 'POST':
        data = request.get_json()
        author = Authors(id=data['id'],
                         alias=data['alias'], 
                         birth_date=data['birth_date'], 
                         city=data['city'], 
                         country=data['country'], 
                         quote=data['quote'], 
                         about_me=data['about_me'], 
                         is_active=True,
                         user_id=data['user_id'])
        db.session.add(author)
        db.session.commit()
        response_body = {'message': 'Author created', 
                         'results': author.serialize()}
        return response_body, 201


@api.route('/authors/<int:author_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_author_id(author_id):
    author = db.one_or_404(db.select(Authors).filter_by(id=author_id), 
                           description=f"Author not found , 404.")
    if request.method == 'GET':
        response_body = {'message': 'Author', 
                         'results': author.serialize()}
        return response_body, 200
    if request.method == 'PUT':
        data = request.get_json()
        author.alias = data['alias']
        author.birth_date = data['birth_date']
        author.city = data['city']
        author.country = data['country']
        author.quote = data['quote']
        author.about_me = data['about_me']
        author.is_active = data['is_active']
        db.session.commit()
        response_body = {'message': 'Author updated', 
                         'results': author.serialize()}
        return response_body, 200
    if request.method == 'DELETE':
        author.is_active = False
        db.session.commit()
        response_body = {'message': 'Author inactived'}
        return response_body, 200
    
    
@api.route('/members', methods=['GET', 'POST']) 
def handle_members():
    if request.method == 'GET':
        members = db.session.execute(db.select(Members))
        members_list = [member.serialize() for member in members]
        response_body = {'message': 'Members', 
                         'results': members_list}
        return response_body, 200 
    if request.method == 'POST':
        data = request.get_json()
        member = Members(name=data['name'], 
                         nif=data['nif'], 
                         address=data['address'], 
                         starting_date=data['starting_date'], 
                         current_date=data['current_date'], 
                         final_date=data['final_date'], 
                         current_discount=data['current_discount'], 
                         remaining_reviews=data['remaining_reviews'], 
                         reviews_expiring_date=data['reviews_expiring_date'], 
                         status=data['status'], 
                         awards=data['awards'], 
                         author_id=data['author_id'],
                         is_active=True)
        db.session.add(member)
        db.session.commit()
        response_body = {'message': 'Member created', 
                         'results': member.serialize()}
        return response_body, 201


@api.route('/members/<int:member_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_member_id(member_id):
    member = db.one_or_404(db.select(Members).filter_by(id=member_id), 
                           description=f"Member not found , 404.")
    if request.method == 'GET':
        response_body = {'message': 'Member', 
                         'results': member.serialize()}
        return response_body, 200
    if request.method == 'PUT':  # Revisar cuando tengamos la Autenticación
        data = request.get_json()
        member.name = data['name']
        member.nif = data['nif']
        member.address = data['address']
        member.starting_date = data['starting_date']
        member.current_date = data['current_date']
        member.final_date = data['final_date']
        member.current_discount = data['current_discount']
        member.remaining_reviews = data['remaining_reviews']
        member.reviews_expiring_date = data['reviews_expiring_date']
        member.status = data['status']
        member.awards = data['awards']
        member.is_active = data['is_active']
        db.session.commit()
        response_body = {'message': 'Member updated', 
                         'results': member.serialize()}
        return response_body, 200
    if request.method == 'DELETE':
        member.is_active = False
        db.session.commit()
        response_body = {'message': 'Member inactived'}
        return response_body, 200


@api.route('/advisors', methods=['GET', 'POST'])  
def handle_advisors():
    if request.method == 'GET':
        advisors = db.session.execute(db.select(Advisors))
        advisors_list = [advisor.serialize() for advisor in advisors]
        response_body = {'message': 'Advisors List', 
                         'results': advisors_list}
        return response_body, 200 
    if request.method == 'POST':
        data = request.get_json()
        advisor = Advisor(id=data['id'],
                          name=data['name'], 
                          nif=data['nif'], 
                          category=data['category'], 
                          address=data['address'], 
                          city=data['city'], 
                          country=data['country'], 
                          about_me=data['about_me'], 
                          is_active=True,
                          user_id=data['user_id'])
        db.session.add(advisor)
        db.session.commit()
        response_body = {'message': 'Advisor created', 
                         'results': advisor.serialize()}
        return response_body, 201


@api.route('/advisors/<int:advisor_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_advisor_id(advisor_id):
    advisor = db.one_or_404(db.select(Advisors).filter_by(advisor_id=advisor_id), 
                            description=f"Advisor not found , 404.")
    if request.method == 'GET':
        response_body = {'message': 'Advisor', 
                         'results': advisor.serialize()}
        return response_body, 200
    if request.method == 'PUT':
        data = request.get_json()
        advisor.name = data['name']
        advisor.nif = data['nif']
        advisor.category = data['category']
        advisor.address = data['address']
        advisor.city = data['city']
        advisor.country = data['country']
        advisor.about_me = data['about_me']
        advisor.is_active = data['is_active']
        db.session.commit()
        response_body = {'message': 'Advisor updated', 
                         'results': advisor.serialize()}
        return response_body, 200
    if request.method == 'DELETE':
        advisor.is_active = False
        db.session.commit()
        response_body = {'message': 'Advisor inactived'}
        return response_body, 200


@api.route('/followers', methods=['GET', 'POST']) 
def handle_followers():
    if request.method == 'GET':
        followers = db.session.execute(db.select(Followers))
        followers_list = [follower.serialize() for follower in followers]
        response_body = {'message': 'Followers List', 
                         'results': followers_list}
        return response_body, 200 
    if request.method == 'POST':
        data = request.get_json()
        follower = Followers(id=data['id'],
                             follower_id=data['follower_id'], 
                             following_id=data['following_id'])
        db.session.add(follower)
        db.session.commit()
        response_body = {'message': 'Follower created', 
                         'results': follower.serialize()}
        return response_body, 201


@api.route('/followers/<int:follower_id>', methods=['GET', 'DELETE'])  
def handle_follower_id(follower_id):
    follower = db.session.execute(db.select(Follower).filter_by(follower_id=follower_id)).scalars()
    if follower is None:
        response_body = {'message': 'You do not have any followers yet'}
        return response_body, 404
    if request.method == 'GET':
        response_body = {'message': 'Follower', 
                         'results': follower.serialize()}
        return response_body, 200
    if request.method == 'DELETE':
        # Delete: quiero eliminar a alguien que me sigue
        # JSON: recibo el id del que me sigue (following)
        # Busco en la base de datos (modelo) el registro que tiene el follower (del endpoint) y el following (del json)
        # si lo encuentro, borro ese registro. Sino lo encuentro es porque no me sigue ese usuario.  
        data = request.get_json()
        concret_follower = db.session.execute(db.select(Follower).filter_by(follower_id=follower_id, following_id=data['following_id'])).scalars()
        if concret_follower is None:
            response_body = {'message': 'There is no follower to delete'}
            return response_body, 400
        db.session.delete(concret_follower)
        db.session.commit()
        response_body = {'message': 'Follower deleted'}
        return response_body, 200


@api.route('/followings/<int:following_id>', methods=['GET'])  
def handle_following_id(following_id):
    followings = db.session.execute(db.select(Follower).filter_by(following_id=following_id)).scalars()
    if followings is None:
        response_body = {'message': 'You are not following to anyone yet'}
        return response_body, 404
    if request.method == 'GET':
        response_body = {'message': 'Following', 
                         'results': follower.serialize()} 
        return response_body, 200
    if request.method == 'DELETE':
    # Delete: un seguidor quiere dejar de seguir a alguien 
    # JSON: recibe el follower, 
    # busco en la base de datos el registro que tiene el follower ( del json) y el following (del endpoint)
    # si lo encuentro, borro ese registro. Sino lo encuentro es porque no se sigue a ese usuario.  
        data = request.get_json()
        follower.following_id=data[following_id]
        if following.id is None:
            response_body = {'message': 'You are not following any account yet'}
            return response_body, 400
        if follower.following_id == following_id:
            db.session.delete(follower)
            db.session.commit()
            response_body = {'message': 'Following deleted'}
            return response_body, 200
        else:
            response_body = {'message': 'Follower with provided following ID not found'}
            return response_body, 404


@api.route('/services', methods=['GET', 'POST']) 
def handle_services():
    if request.method == 'GET':
        services = db.session.execute(db.select(Services))
        services_list = [service.serialize() for service in services]
        response_body = {'message': 'Services', 
                         'results': services_list}
        return response_body, 200 
    if request.method == 'POST':
        data = request.get_json()
        service = Services(id=data['id'],
                           name=data['name'], 
                           starting_date=data['starting_date'], 
                           final_date=data['final_date'], 
                           is_available=data['is_available'],  
                           price=data['price'],
                           category_id=data['category_id'],
                           advisor_id=data['advisor_id'])
        db.session.add(service)
        db.session.commit()
        response_body = {'message': 'Service created', 
                         'results': service.serialize()}
        return response_body, 201


@api.route('/services/<int:service_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_service_id(service_id):
    service = db.one_or_404(db.select(Services).filter_by(service_id=service_id), 
                            description=f"service not found , 404.")
    if request.method == 'GET':
        response_body = {'message': 'Service', 
                         'results': service.serialize()}
        return response_body, 200
    if request.method == 'PUT':
        data = request.get_json()
        service.name = data['name']
        service.starting_date = data['starting_date']
        service.final_date = data['final_date']
        service.is_available = data['is_available']
        service.price = data['price']
        service.category_id = data['category_id']
        service.advisor_id = data['advisor_id']
        db.session.commit()
        response_body = {'message': 'Service updated', 
                         'results': service.serialize()}
        return response_body, 200
    if request.method == 'DELETE':
        # Si el taller aún no inició se borra. Y si ya se dió, lo deshabilitamos. 
        current_date = datetime.now()
        if service.starting_date <= current_date:
            service.is_available = False  
            db.session.commit()
            response_body = {'message': 'Service is now unavailable'}
            return response_body, 200
        db.session.delete(service)
        db.session.commit()
        # FIX: NO lo haremos en esta versión. Deberíamos avisar a los que han contratado el servicio 
        response_body = {'message': 'Service deleted'}
        return response_body, 200


@api.route('/category-services', methods=['GET', 'POST']) # Nombre compuesto
def handle_category_services():
    if request.method == 'GET':
        category_services = db.session.execute(db.select(CategoryServices))
        category_services_list = [category_service.serialize() for category_service in category_services]
        response_body = {'message': 'Category Services', 
                         'results': category_services_list}
        return response_body, 200 
    if request.method == 'POST':
        data = request.get_json()
        category_service = CategoryServices(id=data['id'],
                                            name=data['name'], 
                                            description=data['description'],
                                            is_active=data['is_active'])  
        db.session.add(category_service)
        db.session.commit()
        response_body = {'message': 'Category Service created', 
                         'results': category_service.serialize()}
        return response_body, 201


@api.route('/category-services/<int:category_services_id>', methods=['GET', 'PUT', 'DELETE'])  # Nombre compuesto
def handle_category_service_id(category_service_id):
    category_service = db.one_or_404(db.select(CategoryServices).filter_by(category_service_id=category_service_id), 
                                     description=f"Category Service not found , 404.")
    if request.method == 'GET':
        response_body = {'message': 'Category Service', 
                         'results': category_service.serialize()}
        return response_body, 200
    if request.method == 'PUT':  
        data = request.get_json()
        category_service.name=data['name'], 
        category_service.description=data['description']
        category_service.is_active=data['is_active']
        db.session.commit()
        response_body = {'message': 'Category Service updated', 
                         'results': category_service.serialize()}
        return response_body, 200
    if request.method == 'DELETE':
        # FIX: Marcar como inactiva una categoría si se va a dejar de impartir todos los servicios de esa categoría. 
        services = db.session.execute(db.select(Services).filter_by(category_services_id=category_services_id)).scalars()
        if services is None:
            response_body = {'message': 'There are no services'}
        for service in services:
            service.is_available = False
            db.session.commit()  # Revisar si funciona bien!
        category_service.is_active = False 
        db.session.commit()
        response_body = {'message': 'Category Service inactive'}
        return response_body, 200


@api.route('/shopping-carts', methods=['GET', 'POST'])  # Nombre compuesto
def handle_shopping_carts():
    if request.method == 'GET':
        shopping_carts = db.session.execute(db.select(ShoppingCarts))
        shopping_cart_list = [shopping_cart.serialize() for shopping_cart in shopping_carts]
        response_body = {'message': 'Shopping Carts', 
                         'results': shopping_cart_list}
        return response_body, 200 
    if request.method == 'POST':  
        data = request.get_json()
        shopping_cart = ShoppingCart(id=data['id'],
                                     total_amount=data['total_amount'], 
                                     discount=data['discount'], 
                                     date=data['date'], 
                                     status=data['status'],
                                     member_id=data['member_id']
                                     )
        db.session.add(shopping_cart)
        db.session.commit()
        response_body = {'message': 'Shopping Cart created', 
                         'results': shopping_cart.serialize()}
        return response_body, 201


@api.route('/members/<int:member_id>/shopping-carts', methods=['GET', 'DELETE'])
def handle_shopping_cart_id(shopping_cart_id):
    shopping_cart = db.one_or_404(db.select(ShoppingCart).filter_by(member_id=member_id), 
                                  description=f"Shopping Cart not found , 404.")
    if request.method == 'GET':
        current_date = datetime.now()
        expired_items = []
        shopping_cart_items = db.session.execute(db.select(ShoppingCartItems).filter_by(shopping_cart_id=shopping_cart.id)).scalars()
        for item in shopping_cart_items:
            if item.starting_date <= current_date:
                expired_items.append(item)
        if expired_items:
            for item in expired_items:
                db.session.delete(item)
            db.session.commit()
        shopping_cart_items = db.session.execute(db.select(ShoppingCartItems).filter_by(shopping_cart_id=shopping_cart.id)).scalars()  # Lista actualizada
        shopping_cart_items_list = [item.serialize() for item in shopping_cart_items]
        response_body = {'message': 'Shopping Cart',
                         'results': {'cart': shopping_cart.serialize(),
                                     'items': shopping_cart_items_list}}
        return response_body, 200
    if request.method == 'DELETE':
        #  Borrar items y luego el shopping Cart
        db.session.delete(shopping_cart_items)
        db.session.delete(shopping_cart)
        db.session.commit()
        response_body = {'message': 'Shopping Cart deleted'}
        return response_body, 200
   



"""    Ejemplos   """


@api.route('/reviews', methods=['GET', 'POST'])
def handle_reviews():
    if request.method == 'GET':
        reviews = db.session.execute(db.select(Reviews).order_by(Reviews.id)).scalars()
        review_list = [review.serialize() for review in reviews]
        response_body = {'message': 'Listado de reviews',
                         'results': review_list}
        return response_body, 200 
    if request.method == 'POST':
        response_body = {'message': 'endpoint todavia no realizado'}
        return response_body, 200 


@api.route('/reviews/<int:reviews_id>', methods=['GET', 'PUT', 'DELETE'])
def reviews(reviews_id):
    if request.method == 'GET':
        response_body = {'message': 'endpoint todavia no realizado'}
        return response_body, 200  
    if request.method == 'PUT':
        response_body = {'message': 'endpoint todavia no realizado'}
        return response_body, 200 
    if request.method == 'DELETE':
        response_body = {'message': 'endpoint todavia no realizado'}
        return respons