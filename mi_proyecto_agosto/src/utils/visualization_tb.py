#Módulo para las funciones de los plots
import pandas  as pd 
import matplotlib.pyplot as plt

# Grafica de la comparativa de vacunaciones en la comunidad de Madrid del 2018 vs 2019

def vacunaciones_cam(DataFrame,años):
    años=["#1f77b4","#bcbd22","#2ca02c"]
    valores=DataFrame.columns[3::]
    for x in valores:
        print("\n",x,"\n")
        vacunados=DataFrame(values=x)
        vacunados.plot(color=años)
        plt.title(x)
        plt.show()
    for x in valores:
        vacunados=DataFrame(values=x)
        vacunados.plot()
        vacunados.plot(color=años)
        plt.title(x)
        plt.savefig("../resources/plots/"+x+".png")
        plt.close()


#Grafica porcentaje de vacunaciones por rangos edad seguimiento de CAM para las campañas

def porcentajes(DataFrame,colores_edad):
    colores_edad=["#1f77b4","#2ca02c","#8c564b"]
    valores=DataFrame.columns
    desfase=(0.0,0.0,0.0)
    edades=("De 0 a 59 años","De 60 a 64 años","Mayores de 65")
    for x in valores:
        print("\n",x,"\n")
        porcentaje=DataFrame(values=x)
        plt.pie(porcentaje,labels=edades,colors=colores_edad,autopct="%1.1f%%",shadow=True,startangle=90,explode=desfase)
        plt.title(x)
        plt.show()
    for x in valores:
        porcentaje=DataFrame(values=x)
        plt.pie(porcentaje,labels=edades,colors=colores_edad,autopct="%1.1f%%",shadow=True,startangle=90,explode=desfase)
        plt.title(x)
        plt.savefig("../resources/plots/"+x+".png")
        plt.close()

#VACUNADOS DE 0 A 59 AÑOS

def vacunados_59_cam(DataFrame):
    valores=DataFrame.columns
    for x in valores:
        print("\n",x,"\n")
        de0_59=DataFrame(values=x)
        de0_59.plot()
        plt.title(x)
        plt.show()
    for x in valores:
        de0_59=DataFrame(values=x)
        de0_59.plot()
        plt.title(x)
        plt.savefig("../resources/plots/"+x+".png")
        plt.close()
        
# ESTADISTICA VACUNADOS DE 0 A 59 AÑOS


def estadistica_59_cam(DataFrame):
    valores=DataFrame.columns
    for x in valores:
        print("\n",x,"\n")
        estadistica=DataFrame(values=x)
        estadistica.plot()
        plt.title(x)
        plt.show()
    for x in valores:
        estadistica=DataFrame(values=x)
        estadistica.plot()
        plt.title(x)
        plt.savefig("../resources/plots/"+x+".png")
        plt.close()


