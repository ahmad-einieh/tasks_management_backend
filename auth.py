
from fastapi import  Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Optional
import jwt
from fastapi import APIRouter


from models import User , Token

# Define a secret key for JWT encoding and decoding
SECRET_KEY = "this_is_a_secret_key_for_development"

# Define a token URL for OAuth2 authentication
TOKEN_URL = "/token"

# Create an instance of OAuth2PasswordBearer with the token URL
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=TOKEN_URL)


#! temp
# Create a fake database of users with username and password
users_db = {
    "alice": {"username": "alice", "password": "secret"},
    "bob": {"username": "bob", "password": "secret"}
}




# Define a function to verify the user credentials
def verify_user(username: str, password: str) -> Optional[User]:
    # Check if the username exists in the database
    user = users_db.get(username)
    # If the user exists and the password matches, return the user
    if user and user["password"] == password:
        return User(**user)
    # Otherwise, return None
    return None

# Define a function to generate a JWT token from the user data
def generate_token(user: User) -> Token:
    # Encode the user data with the secret key and an expiration time
    encoded_data = jwt.encode({"username": user.username}, SECRET_KEY, algorithm="HS256")
    # Return a token model with the encoded data and the token type
    return Token(access_token=encoded_data, token_type="bearer")

# Define a function to decode a JWT token and get the user data
def decode_token(token: str) -> Optional[User]:
    try:
        # Decode the token with the secret key
        decoded_data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        # Get the username from the decoded data
        username = decoded_data.get("username")
        # If the username exists in the database, return the user
        if username in users_db:
            return User(**users_db[username])
        # Otherwise, return None
        return None
    except jwt.PyJWTError:
        # If there is any error in decoding, return None
        return None

# Define a dependency function to get the current user from the token
def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    # Decode the token and get the user data
    user = decode_token(token)
    # If the user is valid, return it
    if user:
        return user
    # Otherwise, raise an HTTP exception with status code 401 (unauthorized)
    raise HTTPException(status_code=401, detail="Invalid or expired token")

# Create an instance of FastAPI

authRouter = APIRouter()

# Define an endpoint for getting a token with OAuth2 password flow
@authRouter.post(TOKEN_URL, response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Verify the user credentials from the form data
    user = verify_user(form_data.username, form_data.password)
    # If the user is valid, generate a token and return it
    if user:
        token = generate_token(user)
        return token
    # Otherwise, raise an HTTP exception with status code 401 (unauthorized)
    raise HTTPException(status_code=401, detail="Invalid username or password")
