def orth_triangle(*, cathetus1: float=0, cathetus2: float=0, hypotenuse: float=0) -> float:
    if cathetus1 !=0 and cathetus2 !=0 and hypotenuse !=0:
        return None
    
    if hypotenuse == 0:
        return (cathetus1**2 + cathetus2**2) ** 0.5
    
    cat_sum = cathetus1 + cathetus2

    if hypotenuse > cat_sum:
        return (hypotenuse**2 - cat_sum**2) ** 0.5
    else :
        return None
print(orth_triangle(cathetus1=3, hypotenuse=5))
    # 4.0
print(orth_triangle(cathetus1=8, cathetus2=15))
    # 17.0
print(orth_triangle(cathetus2=9, hypotenuse=3))
    # None
