# Subject (the one being observed)
class YouTubeChannel:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, person):
        self.subscribers.append(person)

    def upload_new_video(self, video):
        print(f"Channel: Uploaded {video}")
        for sub in self.subscribers:
            sub.notify(video)

# Observer (subscriber)
class Subscriber:
    def __init__(self, name):
        self.name = name

    def notify(self, video):
        print(f"{self.name} got notified about new video: {video}")

# Using it
channel = YouTubeChannel()
alice = Subscriber("Alice")
bob = Subscriber("Bob")

channel.subscribe(alice)
channel.subscribe(bob)

channel.upload_new_video("Python Design Patterns")
