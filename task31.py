class laptop():
    color="black"
    brand="Dell"
    ram="4gb"
    def on(self):
        print("your laptop is on")
        print(self.ram)
    def off(self):
        print("your laptop is shutdown")
        print(self.color)
Dell=laptop()
Dell.on()
Dell.off()
    



