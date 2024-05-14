def strong_password(password: str) -> bool:
    if len(password) < 8:
        return False
    elif password.isupper() or password.islower():
        return False
    elif len(set(password) and set("'><:][@$%^&*)(#^:;?'=+-'_")) < 1:
        return False
    elif len(set(password) and set("1234567890")) < 2:
        return False
    else :
        return True
    
print(strong_password('aP1:kD_l0'))
print(strong_password('password'))

# True
# False