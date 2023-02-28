n1, n2, n3 = float(input()), float(input()), float(input())
p1, p2 = int(input())/100, int(input())/100
p3 = 1-p1-p2
print(f"Média Final: {(n1*p1 + n2*p2 + n3*p3):.1f}")