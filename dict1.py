marks = {}

x = int(input("physics marks: "))
marks.update({"phys": x})

x = int(input("chemistry marks: "))
marks.update({"chem": x})

x = int(input("maths marks: "))
marks.update({"maths": x})

print(marks)