from faker import Faker

fake = Faker()


class GenerateUserCredentials:
    email = 'buntester-' + fake.lexify(text='????????????') + '@bunstester.com'
    password = fake.lexify(text='????????????')
    name = fake.name()


class ExistentUserCredentials:
    email = 'heyiambuntester@buntester.com'
    wrong_email = 'heyiamnotbuntester666@buntester.com'
    password = 'buntesterpass'
    wrong_password = 'notbuntesterpass666'
    name = 'buntester'
