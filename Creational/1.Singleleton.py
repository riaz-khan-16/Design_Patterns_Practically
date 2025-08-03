class Singleton:
    _instance = None

    def __init__(self):
        print("Initializing...")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

# Now calling Singleton() directly will NOT prevent the singleton behavior,
# but it breaks the pattern and creates multiple instances!

obj1=Singleton.get_instance()
obj2=Singleton.get_instance()

print(obj1==obj2)
