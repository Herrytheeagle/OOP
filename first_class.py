class Sch:
    # Class Attribute
    specification = 'institution'

    # Initializer / Instance Attribute
    def __init__(self, name, location):
        self.name = name
        self.location = location

# Instantiate the class object
jabu = Sch('Joseph Ayo Babalola University', 'Osun State')
futa = Sch('Federal University of Technology', 'Ondo State')
cu = Sch('Covenant University', 'Ogun State')
unilag = Sch('University Of Lagos', 'Lagos State')

# Access the instance attributes
print("{} is located in {}!".format(jabu.name, jabu.location))
print("{} is located in {}!".format(futa.name, futa.location))
print("{} is located in {}!".format(cu.name, cu.location))
print("{} is located in {}!".format(unilag.name, unilag.location))

# Is Futa an institution
if futa.specification == 'institution':
    print("{} is an {}".format(futa.name, futa.specification))


