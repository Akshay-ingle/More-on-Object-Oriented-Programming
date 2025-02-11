class IOSstring:
    def __init__(self):
        self.str1=''
    def dt(self):
        self.str1=input('enter the string:')
    def pt(self):
        print(self.str1.upper())
ob=IOSstring()
ob.dt()
ob.pt()         