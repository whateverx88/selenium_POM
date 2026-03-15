from faker import Faker

class RegistrationDataGenerator:
    def __init__(self):
        self.fake = Faker()
        self.FIRST_NAME = self.fake.first_name()

data = RegistrationDataGenerator()
print(data.FIRST_NAME)