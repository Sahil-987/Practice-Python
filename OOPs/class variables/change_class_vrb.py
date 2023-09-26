## changing values of class variables
## 2 ways 
## 1. changing values of class variables -- for a particular object
## 2. changing values of class variables -- permanently

class Atm:

    ifsc = "IDBI-ifsc"
    counter = 1

    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.sno = Atm.counter
        Atm.counter += 1

        print(self.sno, self.name, self.pin, Atm.ifsc)



if __name__ == "__main__":
    print("\n\n*****temp change - class variable********\n\n")
    x = Atm("sahil", 1234)
    x.ifsc = x.ifsc + " kanpur" # for a particular object
    print(x.ifsc)
    y = Atm("Waris", 4567) 
    y.ifsc = y.ifsc + " Ambala" # for a particular object
    print(y.ifsc)
    print("\n\n*****permanent change - class variable********\n\n")

    Atm.ifsc = "hdfc-ifsc"

    x = Atm("sahil", 1234)
    y = Atm("Waris", 4567)
