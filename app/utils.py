from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask import jsonify

def hash_password(password: str) -> str:
    """
    Hash a password using Werkzeug's security utilities.
    """
    return generate_password_hash(password)

def verify_password(stored_password: str, provided_password: str) -> bool:
    """
    Verify a stored password against a provided password.
    """
    return check_password_hash(stored_password, provided_password)

def create_token(identity: str) -> str:
    """
    Create a JWT token for a user identity.
    """
    return create_access_token(identity=identity)

def handle_error(message: str, status_code: int):
    """
    Create a JSON response for error handling.
    """
    response = jsonify({"error": message})
    response.status_code = status_code
    return response

def get_current_user():
    """
    Retrieve the current user from the JWT token.
    """
    current_user_id = get_jwt_identity()
    # Assuming you have a function to get user by ID
    from app.models import User
    return User.query.get(current_user_id)
