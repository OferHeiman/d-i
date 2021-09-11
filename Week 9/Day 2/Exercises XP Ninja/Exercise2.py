import random

class QuantumParticle:
    id = 1
    def __init__(self,x=0,y=0,p=0):
        self.x = x
        self.y = y
        self.p = p
        if not self.p == 0.5 or not self.p == -0.5:
            self.p = random.choices([0.5,-0.5])
        self.entangled = None
        self.id = QuantumParticle.id
        QuantumParticle.id +=1 
    
    def position(self):
        self.disturbance()
        random_number = random.randint(1,10001)
    
    def momentum(self):
        self.disturbance()
        random_number = random.uniform(0,1)

    def spin(self):
        self.disturbance()
        random_number = random.choices([0.5,-0.5])
    
    def disturbance(self):
        self.x = random.randint(1,10001)
        self.y = random.uniform(0,1)
        print("Quantum Interferences!!")


    def __repr__(self):
        return repr(f"p{self.id}")


    def entangle(self,p2):
        if self.entangled == p2 and p2.entangled == self:
            print("Spooky Action at a Distance")
        elif self.entangled == None and p2.entangled == None:
            self.entangled = p2
            p2.entangled = self
            if self.p == 0.5:
                p2.p = -0.5
            else:
                p2.p = 0.5
            print(f"Particle p{self.id} is now in quantum entanglement with Particle p{p2.id}")
        elif self.entangled:
            print(f"Particle p{self.id} is already entangled with p{self.entangled}")
        elif p2.entangled:
            print(f"Particle p{p2.id} is already entangled with p{p2.entangled}")
            
p1 = QuantumParticle(x=1,p=5.0)
p2 = QuantumParticle(x=2,p=5.0)
p1.entangle(p2)
p1.entangle(p2)