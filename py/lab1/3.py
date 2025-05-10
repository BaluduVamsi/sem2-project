a = [
    ("inches", 12),             
    ("yards", 1 / 3),           
    ("miles", 1 / 5280),        
    ("millimeters", 304.8),      
    ("centimeters", 30.48),   
    ("meters", 0.3048),          
    ("kilometers", 0.0003048)   
]
feet = float(input("Enter a length in feet: "))
for i, (b,_) in enumerate(a, 1):
    print(f"{i}. {b}")
c = int(input("Enter  your choice: "))
if 1 <= c <= len(a):
    b, d = a[c - 1]
    co= feet * d
    print(f"{feet} feet is equal to {co} {b}.")
else:
    print("Invalid choice")