from flask import Flask, request, render_template
from sympy import factorint

app = Flask(__name__)
# 1- verification de la congurience de FERMAT : 

def  binair (k) :# ecrire la fonction qui converte le nombre en binair 
    binair = ''
    while k !=0 :
      bit = k % 2  
      binair = str(bit) + binair
      k = k // 2
    return binair
n= int(input())
def puissance(n, a=2):
    # Convertir n en binaire pour obtenir la liste des puissances à calculer
    binaire = binair(n-1)  
    s = 1  
    for i, bit in enumerate(reversed(binaire)):
        if bit == '1':  
            p = a  
            for _ in range(i):  
                p = p * p  
            s *= p
    return s
print (puissance(n))

def est_premier(n): # teste de primalité avec la methode d'essai 
    if n <= 1:  # Les nombres <= 1 ne sont pas premiers
        return False
    for i in range(2, int(n**0.5) + 1):  # Vérifie jusqu'à la racine carrée de n
        if n % i == 0:  # Si n est divisible par i, alors ce n'est pas un nombre premier
            return False
    return True 


# def decomposition(n): 
#     pass

def carmicheal(n):
     facteurs = factorint(n)
     #verifier que tout les facteur de n sont distinct cest a dire n=p^e * p-2^e_2 ..... tout les puissance e_i=1 
     for facteur, exponent in facteurs.items():
        if exponent != 1:
            return False
     # verifier la condirion p_i -1 divise n-1
     for facteur in facteurs.keys():
         if (n - 1)%(facteur - 1)  != 0: 
            return False 
     return True 

  
def test_congurience(n):
     p = puissance(n) % n 
     if p == 1:
         if est_premier(n) == True : 
            return f"{n} est un nombre premier" , "result-prime"  # jai ajouter ca pour changer les classe de css 
         elif carmicheal(n) == True :
            return f"{n} est un nombre de Carmicheal" , "result-carmichael" 
         else :
            return f"{n} est un pseudo premier de Fermat . en revanche , il nest pas de carmicheal  " , "result-pseudo-prime"  
     else:
         return f"{n} est composé." , "result-composite" 
      
@app.route('/')
def home():
    return render_template('index.html', result=None)

@app.route('/test', methods=['POST'])
def test():
    number = int(request.form['number'])
    result ,  result_class = test_congurience(number)
    return render_template('index.html', number=number, result=result , result_class=result_class )

if __name__ == '__main__':
    app.run(debug=True)