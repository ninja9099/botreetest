
class UserType:
    ADMIN = 1
    CUSTOMER = 2
    CLEANER = 3

    FieldStr = {
        ADMIN: 'Admin',
        CUSTOMER: 'Customer',
        CLEANER: 'Cleaner',

    }

    @classmethod
    def get_choices(cls):
        return cls.FieldStr.items()