class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # starting at middle value
        self.energy = 10  # starting at full energy
        self.happiness = 5  # starting at middle value
        self.tricks = []  # list to store tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)  
        self.happiness = min(10, self.happiness + 1)  
        print(f"🍽️ {self.name} is eating... Yum! 😋")

    def sleep(self):
        self.energy = min(10, self.energy + 5)  
        print(f"😴 {self.name} is sleeping... Zzz 💤")

    def play(self):
        if self.energy < 2:
            print(f"😫 {self.name} is too tired to play!")
            return
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"🎾 {self.name} is playing... Woo! 🎈")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
            print(f"🎓 {self.name} learned {trick}! 🌟")
        else:
            print(f"📝 {self.name} already knows {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"🎪 {self.name}'s tricks: {', '.join(self.tricks)} ✨")
        else:
            print(f"📚 {self.name} doesn't know any tricks yet!")

    def get_status(self):
        print(f"\n📊 {self.name}'s current status:")
        print(f"🍖 Hunger: {self.hunger}/10")
        print(f"⚡ Energy: {self.energy}/10")
        print(f"😊 Happiness: {self.happiness}/10")
