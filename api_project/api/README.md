"""
Authentication & Permissions Setup

- Using TokenAuthentication from DRF
- All views require authentication unless overridden
- Tokens retrieved via /api/get-token/
- Example:
      Authorization: Token <token_string>
- BookViewSet uses IsAuthenticated to restrict access to logged-in users
"""
