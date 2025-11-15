# OBJECT METHOD

class school:

    s_name = 'KVM WAI'
    s_loc = 'WAI'

    def __init__(self, st_name, st_id):

        self.st_name = st_name
        self.st_id = st_id

    def display(self):

        print(self.st_name, self.st_id)

    def modify_st_name(self, new_name):
        self.st_name = new_name

st1 = school('Unik',101)
st1.display() # OP: Unik 101

st2 = school('Ritu',102)
st2.display() # OP: Ritu 102

st1.modify_st_name('Rohit')
st1.display() # OP: Rohit 101
