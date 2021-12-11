from cylinder import cylinder

cy = cylinder(1.0, "red", 1.0)
radius = float(input("input radius: "))
while radius < 1 : 
    radius = float(input("input radius value can't be zero, re-input radius :"))
color = str(input("input color: "))
height = float(input("input height of the cylinder: ")) 

cy.setRadius(radius)
cy.setColor(color)
cy.setHeight(height)

print("radius :", cy.getRadius())
print("color :", cy.getColor())
print("height :", cy.getHeight())
print("area :", cy.getArea())
print("volume :", cy.getVolume())

