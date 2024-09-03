from flask import Blueprint, request, jsonify
from . import db
from .models import User, Train, Booking
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('routes', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'])
    new_user = User(username=data['username'], password=hashed_password, role='user')
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message="User registered"), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    return jsonify(message="Invalid credentials"), 401

@bp.route('/add_train', methods=['POST'])
@jwt_required()
def add_train():
    current_user = get_jwt_identity()
    user = User.query.get(current_user)
    if user.role != 'admin':
        return jsonify(message="Admin access required"), 403

    data = request.get_json()
    new_train = Train(source=data['source'], destination=data['destination'],
                      total_seats=data['total_seats'], available_seats=data['total_seats'])
    db.session.add(new_train)
    db.session.commit()
    return jsonify(message="Train added"), 201

@bp.route('/seat_availability', methods=['GET'])
def seat_availability():
    source = request.args.get('source')
    destination = request.args.get('destination')
    trains = Train.query.filter_by(source=source, destination=destination).all()
    result = [{'id': train.id, 'available_seats': train.available_seats} for train in trains]
    return jsonify(trains=result), 200

@bp.route('/book_seat', methods=['POST'])
@jwt_required()
def book_seat():
    current_user = get_jwt_identity()
    user = User.query.get(current_user)
    
    if user.role == 'user':
        data = request.get_json()
        train = Train.query.get(data['train_id'])
        
        if train and train.available_seats >= data['seats']:
            train.available_seats -= data['seats']
            new_booking = Booking(user_id=user.id, train_id=train.id, seats_booked=data['seats'])
            db.session.add(new_booking)
            db.session.commit()
            return jsonify(message="Seats booked"), 200
        return jsonify(message="Not enough seats available"), 400
    
    return jsonify(message="User access required"), 403

@bp.route('/booking_details', methods=['GET'])
@jwt_required()
def booking_details():
    current_user = get_jwt_identity()
    user = User.query.get(current_user)
    
    if user.role == 'user':
        bookings = Booking.query.filter_by(user_id=user.id).all()
        result = [{'train_id': booking.train_id, 'seats_booked': booking.seats_booked} for booking in bookings]
        return jsonify(bookings=result), 200
    
    return jsonify(message="User access required"), 403
