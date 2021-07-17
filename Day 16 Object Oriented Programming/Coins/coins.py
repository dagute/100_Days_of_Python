import random

class Coin:
    def __init__(self, rare=False, clean=True, heads=True, **kwargs): # pack down all the info in kwargs accept all the data

        for key, value in kwargs.items():
            setattr(self, key, value) 

        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.color = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def __del__(self):
        print("coin spent!")

    def fip(self):
        head_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __str__(self):
        if self.original_value >= 1:
            return "£{} Coin".format(int(self.original_value))
        else:
            return "{}p Coin".format(int(self.original_value * 100))

class One_Pence(Coin): #class Pound inhert from Coin Class
    def __init__(self):
        data = {
            "original_value":0.01,
            "clean_colour":"bronze",
            "rusty_colour":"brownish",
            "num_edges" : 1,
            "diameter": 20.3,
            "thickness": 1.52,
            "mass":3.56,
            }
        super().__init__(**data) #unpack the data

class Two_Pence(Coin):
    def __init__(self):
        data = {"original_value":0.02,
                "clean_colour":"bronze",
                "rusty_colour":"brownish",
                "num_edges" : 1,
                "diameter": 25.9,
                "thickness": 1.85,
                "mass":7.12,
            }
        super().__init__(**data)
 

class Five_Pence(Coin):
    def __init__(self):
        data = {"original_value":0.05,
                "clean_colour":"silver",
                "rusty_colour": None,
                "num_edges" : 1,
                "diameter": 18.0,
                "thickness": 1.77,
                "mass":3.25,
            }
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour

class Ten_Pence(Coin):
    def __init__(self):
        data = {"original_value":0.10,
                "clean_colour":"silver",
                "rusty_colour":None,
                "num_edges" : 1,
                "diameter": 24.5,
                "thickness": 1.85,
                "mass":6.50,
            }
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour

class Twenty_Pence(Coin):
    def __init__(self):
        data = {"original_value":0.20,
                "clean_colour":"silver",
                "rusty_colour":None,
                "num_edges" : 7,
                "diameter": 21.4,
                "thickness": 1.7,
                "mass":5.00,
            }
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour

class Fifty_Pence(Coin):
    def __init__(self):
        
        data = {"original_value":0.50,
                "clean_colour":"silver",
                "rusty_colour":None,
                "num_edges" : 7,
                "diameter": 27.3,
                "thickness": 1.78,
                "mass":8.00,
            }

        super().__init__(**data)

    def rust(self):
        self.colour = self.clean_colour

    def clean(self):
        self.colour = self.clean_colour

class One_Pound(Coin):
    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_colour": "gold",
            "rusty_colour" : "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness":3.15,
            "mass": 9.5
            }
        super().__init__(**data)

class Two_Pound(Coin):
    def __init__(self):
        data = {"original_value":2.00,
                "clean_colour":"gold & silver",
                "rusty_colour":"greenish",
                "num_edges" : 1,
                "diameter": 28.4,
                "thickness": 2.50,
                "mass":12.00,
            }

        super().__init__(**data)

coins = [One_Pence(), Two_Pence(), Five_Pence(), Ten_Pence(), Twenty_Pence(),
             Fifty_Pence(), One_Pound(), Two_Pound()]

for coin in coins:
    arguments = [coin, coin.colour, coin.value, coin.diameter, coin.thickness,
                           coin.num_edges, coin.mass]

    string = "{} - Colour: {}, value:{}, diameter(mm):{}, thickness(mm):{}, number of edges:{}, mass(g):{}".format(*arguments)
    print(string)




"""

    def __init__(self, rare=False):

        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00
            
        self.colour = "gold"
        self.num_edges = 1
        self.diameter = 22.5 #mm
        self.thickness = 3.15#mm
        self.heads = True  #All These Values are states

    def __del__(self):
        print("coin spent!)

    def rust(self):
        self.color = "green"

    def clean(self):
        self.colour = "gold"

    def fip(self):
        head_options = [True, False]
        choice = random.choice(heads_options)
        sef.heads = choice
"""
    


# del coin1

#coin1.rust()        

#coin1 = Pound() #object
#print(coin1.value)

#coin2 = Pound()
#coin1.color = "green"
#coin1.value = 1.25 



