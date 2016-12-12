class student:
    def __init__(self, name, hometown, age, height, fav_icecream):

        self.name=name
        self.hometown=hometown
        self.age=age
        self.height=height
        self.fav_icecream=fav_icecream

    def print_summary(self):
        print('My name is '+ self.name
              + ', I live in '+ self.hometown
              +'. I am '+ self.age +' years old. and '
              + self.height+ ' meters high, and my favorite ice cream flavor is '
              + self.fav_icecream + ', of course.')
