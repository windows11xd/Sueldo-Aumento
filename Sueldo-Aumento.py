print("="*3, "EMPRESA COCA COLA", "="*3)
print("""Sueldo (S/.)    Aumento (%)
    5001 - más      10
    3501 - 5000     15
    2001 - 3500     20
    Hasta 2000      25""")

money = int(input("Ingrese su sueldo: "))
while money:
        if money <= -1:
                money = int(input("Ingrese monto correcto: "))
                continue
        def sueldo(money):
                if money >= 0 and money <= 2000:
                        aumento1 = money*0.25
                        suma1 = aumento1+money
                        print("El suledo base es: ",money)
                        print("El aumento es: ",aumento1)
                        print("Su sueldo aumentado en 25%: ",round(suma1))
                if money >= 2001 and money <= 3500:
                        aumento2 = money*0.2
                        suma2 = aumento2+money
                        print("El suledo base es: ",money)
                        print("El aumento es: ",aumento2)
                        print("Su sueldo aumentado en 20%: ",round(suma2))                              
                if money >= 3501 and money <= 5000:
                        aumento3 = money*0.15
                        suma3 = aumento3+money
                        print("El suledo base es: ",money)
                        print("El aumento es: ",aumento3)
                        print("Su sueldo aumentado en 15%: ",round(suma3))                             
                if money >= 5001:
                        aumento4 = money*0.1
                        suma4 = aumento4+money
                        print("El suledo base es: ",money)
                        print("El aumento es: ",aumento4)
                        print("Su sueldo aumentado en 10%: ",round(suma4))        
        sueldo(money)
        break