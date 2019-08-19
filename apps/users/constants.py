
class UserType:

    CUSTOMER = 1
    CLEANER = 2

    FieldStr = {
        CUSTOMER: 'Customer',
        CLEANER: 'Cleaner'
    }

    @classmethod
    def get_choices(cls):
        return cls.FieldStr.items()