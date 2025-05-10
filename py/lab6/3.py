class Converter:

    dictonary={"millimeter":1,"centimeter":10,"inch":25.4,"foot":304.8,"yard":914.4,"meter":1000,"kilometer":1000000,"mile":1609344}
    
    
    def __init__(self,length,type):
        self.lb=length
        self.type=type
        self.dummylength=self.lb*Converter.dictonary[type]

    def millimeter(self):
        return self.dummylength
    
    def centimeter(self):
        return self.dummylength/10
    
    def inch(self):
        return self.dummylength/25.4
    
    def foot(self):
        return self.dummylength/304.8
    
    def yard(self):
        return self.dummylength/914.4
    
    def meter(self):
        return self.dummylength/1000
    
    def kilometer(self):
        return self.dummylength/1000000
    
    def mile(self):
        return self.dummylength/1609344


print("1.millimeter  2.centimeter\n3.inch        4.foot\n5.yard        6.meter\n7.kilometer   8.mile")
type=input("Enter Type: ")
if type not in Converter.dictonary.keys():
    print("invalid type!")
    type=input("Enter Type: ")
length=int(input("Length: "))
print()
obj1=Converter(length,type)
a=True
while a:
    print()
    type1=int(input("1.millimeter  2.centimeter\n3.inch        4.foot\n5.yard        6.meter\n7.kilometer   8.mile\n9.exit\nselect type you want to convert: "))
    match type1:
        case 1: print(obj1.millimeter()," millimeters")
        case 2: print(obj1.centimeter()," centimeters")
        case 3: print(obj1.inch()," inches")
        case 4: print(obj1.foot()," feets")
        case 5: print(obj1.yard()," yards")
        case 6: print(obj1.meter()," meters")
        case 7: print(obj1.kilometer()," kilometers")
        case 8: print(obj1.mile()," miles")
        case 9: a=False


