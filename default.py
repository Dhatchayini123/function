def person(name,age=35):
    print("name:",name)
    print("age:",age)
    return
person(age=50,name="miki")
#this statement runs in name=miki,age=50
person(name="miki")
#this statement runs in name=miki,where age is default so age=35
