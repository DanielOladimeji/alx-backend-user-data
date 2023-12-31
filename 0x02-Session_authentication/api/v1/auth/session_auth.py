#!/usr/bin/env python3
"""Define SessionAuth class"""
import base64
from uuid import uuid4
from typing import TypeVar
from .auth import Auth
from models.user import User
from flask import abort


class SessionAuth(Auth):
    """Implements Session Authorization methods"""
    user_id_by_session_id = {}

    def session_cookie(self, request=None):
        """Retrieves the session cookie from the request."""
        if request is None:
            return None

        # Adjust this line based on your actual implementation
        return request.cookies.get('session_cookie')

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user with id user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        id = uuid4()
        self.user_id_by_session_id[str(id)] = user_id
        return str(id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a user ID based on a session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Returns a user instance based on a cookie value"""
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """Del a user session"""
        if request is None:
            return False
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return False
        user_id = self.user_id_for_session_id(session_cookie)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_cookie]
        return True
