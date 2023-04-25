
from flask import redirect, render_template, request, session
from functools import wraps



"""

This file is for all function/logic that is not directly related to a spefic page
ex: common API calls, or sql queiries

"""




"""

Creating of login requiremnts

"""

def login_req(f):

    @wraps(f)

    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function