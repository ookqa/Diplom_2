from faker import Faker

fake = Faker()


class GenerateUserCredentials:
    email = ('buntester' + fake.lexify(text='????????????') + '@bunstester.com').lower()
    password = fake.lexify(text='????????????')
    name = fake.name()


class ExistentUserCredentials:
    email = 'heyiambuntester@buntester.com'
    wrong_email = 'heyiamnotbuntester666@buntester.com'
    password = 'buntesterpass'
    wrong_password = 'notbuntesterpass666'
    name = 'buntester'

class IngredientsData:
    BUN = '61c0c5a71d1f82001bdaaa6d'
    SAUCE = '61c0c5a71d1f82001bdaaa75'
    FILLER = '61c0c5a71d1f82001bdaaa78'



