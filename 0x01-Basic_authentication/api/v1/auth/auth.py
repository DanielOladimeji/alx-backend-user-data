#!/usr/bin/env python3
"""
Definition of class Auth
"""

from typing import List, TypeVar
from flask import request


class Auth:
    """
    Manages the API authentication
"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the given path.

        Args:
        - path: str: The path to check authentication for.
        - excluded_paths: List[str]: The list of paths that
        do not require authentication.

        Returns:
        - bool: Whether authentication is required for the given path.
        """
        if not path:
            return True

        if not excluded_paths or len(excluded_paths) == 0:
            return True

        for ex_path in excluded_paths:
            if path == ex_path[:-1] or path.startswith(ex_path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Retrieve the authorization header from the request.

        Args:
        - request: The Flask request object.

        Returns:
        - str: The authorization header or None if not present.
        """
        if request is None:
            return None
        header = request.headers.get('Authorization')
        if header is None:
            return None
        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieve the current user from the request.

        Args:
        - request: The Flask request object.

        Returns:
        - User: The current user or None if not authenticated.
        """
        return None
