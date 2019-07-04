from tkinter import *
from tkinter import ttk

damas = Tk()
damas.title("!!!!!GAME!!!! Olivares.B_Caiza.E")
tablero = Canvas(damas, width=400, height=400)
damas.geometry('940x640')
tablero.place(x=210, y=50)
ficharoja = PhotoImage(file='ficha1.png')
fichaazul = PhotoImage(file='ficha2.png')

def seleccionar_ficha(event):
    global rectangulo
    a = tablero.find_closest(event.x, event.y)[0] 
    b = tablero.gettags(a)
    if "ficha" in b:
        c = str(a)
        d = datos.get(c,None)
        if d is not None:
            coordenadas["a"] = a
            X = event.x - (event.x % 50)
            Y = event.y - (event.y % 50) 
            coordenadas["posicionx"] = event.x
            coordenadas["posiciony"] = event.y  
            coordenadas["finalpx"] = X
            coordenadas["finalpy"] = Y 
            coordenadas["X"] = event.x-d["posicionx"]
            coordenadas["Y"] = event.y-d["posiciony"]
        else:
            pass
    else:
        coordenadas["a"] = None 

def Click_ficha(event):
    pass


def validar_posicion(event):
    global datos
    global rectangulo
    global tablero
    a = coordenadas["a"]
    if a is None:
    	return
    _posicionx = coordenadas["posicionx"]
    _posiciony = coordenadas["posiciony"]
    finalpx = coordenadas["finalpx"]
    finalpy = coordenadas["finalpy"]
    c = str(a)
    ultima_posicion = datos.get(c,None) 
    ultimapx = ultima_posicion["posicionx"]
    ultimapy = ultima_posicion["posiciony"] 
    b = tablero.gettags(a)
    s = tablero.find_overlapping(event.x, event.y,event.x, event.y) 
    
    if s[1]!=1:
        X = event.x - (event.x % 50)
        Y = event.y - (event.y % 50)
        Invalido.place_forget() 
        Jugador.place_forget() 
        e = str(X)+"-"+str(Y)
        X1 = X - finalpx
        Y1 = Y - finalpy
        X2 = abs(X1)
        Y2 = abs(Y1)
        if(X1==0 or Y1==0 or X2!=Y2 or X2>160):
            Invalido.place(x="625",y="250")
            X4 = ultimapx - _posicionx + coordenadas["X"]
            Y4 = ultimapy - _posiciony + coordenadas["Y"] 
            tablero.move(a,X4,Y4)
        else: 
            if X2>80:
                X3 = X - anonima(X1) * 50
                Y3 = Y - anonima(Y1) * 50
                t = str(X3)+"-"+str(Y3) 
                t1 = str(X)+"-"+str(Y) 
                d = datos.get(t,None) 
                f = datos.get(t1,None) 
                if d is None:   
                    X4 = ultimapx - _posicionx + coordenadas["X"]
                    Y4 = ultimapy - _posiciony + coordenadas["Y"] 
                    tablero.move(a,X4,Y4) 
                else:  
                    if f is None:
                        g = tablero.gettags(d)
                        if "ficha" in g:
                            if ("ficha_azul" in b and "ficha_roja" in g) or ("ficha_azul" in g and "ficha_roja" in b):
                                X4 = X -_posicionx + coordenadas["X"]
                                Y4 = Y - _posiciony + coordenadas["Y"]
                                tablero.move(a,X4,Y4)
                                datos[e] = a
                                h = str(datos[c]["posicionx"])+"-"+str(datos[c]["posiciony"])
                                datos[h] = None
                                datos[c]["posicionx"]=X
                                datos[c]["posiciony"]=Y
                                tablero.delete(d);
                                datos[str(d)] = None
                                datos[t] = None 
                            else:
                                X4 = ultimapx - _posicionx + coordenadas["X"]
                                Y4 = ultimapy - _posiciony + coordenadas["Y"] 
                                tablero.move(a,X4,Y4) 
                        else:
                            X4 = ultimapx - _posicionx + coordenadas["X"]
                            Y4 = ultimapy - _posiciony + coordenadas["Y"] 
                            tablero.move(a,X4,Y4) 
                    else:
                        X4 = ultimapx - _posicionx + coordenadas["X"]
                        Y4 = ultimapy - _posiciony + coordenadas["Y"] 
                        tablero.move(a,X4,Y4) 
            else:
                d = datos.get(e,None) 
                if d is not None:   
                    X4 = ultimapx - _posicionx + coordenadas["X"]
                    Y4 = ultimapy - _posiciony + coordenadas["Y"] 
                    tablero.move(a,X4,Y4)  
                else:
                    X4 = X -_posicionx + coordenadas["X"]
                    Y4 = Y - _posiciony + coordenadas["Y"]
                    tablero.move(a,X4,Y4)
                    datos[e] = a
                    h = str(datos[c]["posicionx"])+"-"+str(datos[c]["posiciony"])
                    datos[h] = None
                    datos[c]["posicionx"]=X
                    datos[c]["posiciony"]=Y

def mover_ficha(event):
    global coordenadas
    global tablero
    a = coordenadas["a"]
    _posicionx = coordenadas["posicionx"]
    _posiciony = coordenadas["posiciony"]
    X4 = event.x - _posicionx
    Y4 = event.y - _posiciony
    coordenadas["posicionx"] = event.x
    coordenadas["posiciony"] = event.y
    if  a is not None:
        b = tablero.gettags(a)
        if "ficha" in b:
            tablero.tag_raise(a)
            tablero.move(a,X4,Y4)





Invalido= ttk.Label(damas,text="MOVIMIENTO INVALIDO",foreground="black")
Titulo=ttk.Label(damas,text="JUEGO DE DAMAS",foreground="red")
Jugador= ttk.Label(damas,text="COMENZAR CUALQUIER JUGADOR",foreground="black")

Titulo.place(x="50",y="100")
Jugador.place(x="15",y="150")
lista = []
datos = {} 
cont = 0 
coordenadas = {"a":None,"posicionx":0,"posiciony":0}
posiciones_negras = [];
posiciones_azules = [];
rectangulo = tablero.create_rectangle(0,0,400,400, outline="red", fill="black")
for i in range(8):
    for j in range(8):
        r = i*50
        s = j*50 
        if cont % 2 == 0: 
            if j % 2==0:
                if cont<=2:           
                    rectangulo = tablero.create_image(s,r, anchor = NW, image=fichaazul,tags=("ficha_azul","ficha")) 
                    datos[str(s)+"-"+str(r)] = rectangulo
                    datos[str(rectangulo)] = {"posicionx":s,"posiciony":r}
                else:
                    if cont<=4:   
                        pass    
                    else: 
                        rectangulo = tablero.create_image(s,r, anchor = NW, image=ficharoja,tags=("fica_roja","ficha"))
                        datos[str(s)+"-"+str(r)] = rectangulo
                        datos[str(rectangulo)] = {"posicionx":s,"posiciony":r}
            else:
                rectangulo = tablero.create_rectangle(s,r,s+50,r+50, outline="red", fill="red")
        else:
            if j % 2!=0:
                if cont<=2: 
                    rectangulo = tablero.create_image(s,r, anchor = NW, image=fichaazul,tags=("ficha_azul","ficha"))
                    datos[str(s)+"-"+str(r)] = rectangulo
                    datos[str(rectangulo)] = {"posicionx":s,"posiciony":r}
                else:
                    if cont<=4:   
                        pass            
                    else: 
                        rectangulo = tablero.create_image(s,r, anchor = NW, image=ficharoja,tags=("ficha_roja","ficha"))
                        datos[str(s)+"-"+str(r)] = rectangulo
                        datos[str(rectangulo)] = {"posicionx":s,"posiciony":r}
            else:
                rectangulo = tablero.create_rectangle(s,r,s+50,r+50, outline="red", fill="red")
         
        lista.append(rectangulo)
    cont+=1 

anonima = lambda x: (1, -1)[x < 0]


tablero.tag_bind("ficha","<Button-1>", Click_ficha) 
tablero.tag_bind("ficha","<ButtonPress-1>", seleccionar_ficha) 
tablero.tag_bind("ficha","<ButtonRelease-1>", validar_posicion) 
tablero.tag_bind("ficha","<B1-Motion>", mover_ficha) 


damas.mainloop()