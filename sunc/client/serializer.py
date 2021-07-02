class BaseSerializer:
    field = ''

    def __new__(cls, *args, **kwargs):
        print(cls.__dict__)
        print(cls)
        print(kwargs)


serializer = BaseSerializer(teste='teste')
