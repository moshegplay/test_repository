def test_login_invalid_password_character(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="idantheking", password="id$n", error="invalid character")


def test_login_invalid_password(app):
    app.navigate(app.home.login)
    app.home.login.with_error(username="idantheking", password="idan11229922", error="password not found")