#Módulo para las funciones de los plots
import pandas  as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Grafica de la comparativa de vacunaciones en la comunidad de Madrid del 2018 vs 2019

def vacunaciones_cam(DataFrame,años):
    valores=DataFrame.columns[3::]
    for x in valores:
        print("\n",x,"\n")
        vacunados=DataFrame(values=x)
        vacunados.plot(kind='bar',width=0.8,colors=años.values())
        plt.title(x)
        plt.show()
    for x in valores:
        vacunados=DataFrame(values=x)
        vacunados.plot()
        vacunados.plot(kind='bar',width=0.8,colors=años.values())
        plt.title(x)
        plt.savefig("../resources/plots/"+x+".png")
        plt.close()


#Grafica porcentaje de vacunaciones por rangos edad seguimiento de CAM para las campañas

def porcentajes(DataFrame,colores_edad):
    valores=DataFrame.columns
    desfase=(0.0,0.0,0.0)
    edades=("De 0 a 59 años","De 60 a 64 años","Mayores de 65")
    for x in valores:
        print("\n",x,"\n")
        porcentaje=DataFrame(values=x)
        plt.pie(porcentaje,labels=edades,colors=colores_edad.values(),autopct="%1.1f%%",shadow=True,startangle=90,explode=desfase)
        plt.title(x)
        plt.show()
    for x in valores:
        porcentaje=DataFrame(values=x)
        plt.pie(porcentaje,labels=edades,colors=colores_edad.values(),autopct="%1.1f%%",shadow=True,startangle=90,explode=desfase)
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
        estadistica.plot(kind='barh')
        plt.title(x)
        plt.show()
    for x in valores:
        estadistica=DataFrame(values=x)
        estadistica.plot(kind='barh')
        plt.title(x)
        plt.savefig("../resources/plots/"+x+".png")
        plt.close()


#VACUNADOS DE 60 A 64 AÑOS

def vacunados_60_64(DataFrame,col):
    valores=DataFrame.columns
    for x in valores:
        print("\n",x,"\n")
        de60_64=DataFrame(values=x)
        de60_64.plot(kind='bar',width=0.1,colores=col.values())
        plt.title(x)
        plt.show()
    for x in valores:
        de60_64=DataFrame(values=x)
        de60_64.plot(kind='bar',width=0.1,colores=col.values())
        plt.title(x)
        plt.savefig("../resources/plots/"+x+".png")
        plt.close()

#VACUNADOS >65 AÑOS

def vacunados_65(DataFrame):
    valores=DataFrame.columns
    for x in valores:
        print("\n",x,"\n")
        de65=DataFrame(values=x)
        de65.plot()
        plt.title(x)
        plt.show()
    for x in valores:
        de65=DataFrame(values=x)
        de65.plot()
        plt.title(x)
        plt.savefig("../resources/plots/"+x+".png")
        plt.close()


# ESTADISTICA VACUNADOS > 65 AÑOS


def estadistica_65(DataFrame,color):
    valores=DataFrame.columns
    for x in valores:
        print("\n",x,"\n")
        estadistica=DataFrame(values=x)
        estadistica.plot(kind='barh',colors=color.values())
        plt.title(x)
        plt.show()
    for x in valores:
        estadistica=DataFrame(values=x)
        estadistica.plot(kind='barh',colors=color.values())
        plt.title(x)
        plt.savefig("../resources/plots/"+x+".png")
        plt.close()


#TOTAL ENPADRONADOS CON NUMERO DE VACUNADOS POR RANGO DE EDAD EN CAM 2019
   
def padron_vac(DataFrame,edad):
    valores=DataFrame.columns
    for x in valores:
        print("\n",x,"\n")
        padron=DataFrame(values=x,fill_value=0)
        padron.plot(kind='bar',width=0.8,colors=edad.values())
        plt.title(x)
        plt.show()
    for x in valores:
        padron=DataFrame(values=x,fill_value=0)
        padron.plot(kind='bar',width=0.8,colors=edad.values())
        plt.title(x)
        plt.savefig("../resources/plots/"+x+".png")
        plt.close()

#CORRELACION TOTAL ENPADRONADOS CON NUMERO DE VACUNADOS POR RANGO DE EDAD EN CAM 2019

def correlacion(DataFrame,edad):
    valores=DataFrame.columns
    for x in valores:
        print("\n",x,"\n")
        c=DataFrame.corr(values=x,fill_value=0)
        sns.heatmap(c,cmap="BrBG",annot=True)
        plt.title(x)
        plt.show()
    for x in valores:
        c=DataFrame.corr(values=x,fill_value=0)
        sns.heatmap(c,cmap="BrBG",annot=True)
        plt.title(x)
        plt.savefig("../resources/plots/"+x+".png")
        plt.close()

#PRECIOS VENTA VACUNA COVID

def venta_precio(DataFrame,colores):
    valores=DataFrame.columns
    for x in valores:
        print("\n",x,"\n")
        estadistica=DataFrame(values=x)
        estadistica.plot(kind='bar',colors=colores.values())
        plt.title(x)
        plt.show()
    for x in valores:
        estadistica=DataFrame(values=x)
        estadistica.plot(kind='bar',colors=colores.values())
        plt.title(x)
        plt.savefig("../resources/plots/"+x+".png")
        plt.close()

#COSTE VACUNA COVID OBLIGATORIA

def coste_obligado(DataFrame,colores):
    valores=DataFrame.columns
    for x in valores:
        print("\n",x,"\n")
        vaco=DataFrame(values=x)
        vaco.plot(kind='bar',colors=colores.values())
        plt.title(x)
        plt.show()
    for x in valores:
        vaco=DataFrame(values=x)
        vaco.plot(kind='bar',colors=colores.values())
        plt.title(x)
        plt.savefig("../resources/plots/"+x+".png")
        plt.close()


#COSTE VACUNA COVID REF GRIPE

def coste_ref(DataFrame,colores):
    valores=DataFrame.columns
    for x in valores:
        print("\n",x,"\n")
        vacref=DataFrame(values=x)
        vacref.plot(kind='bar',colors=colores.values())
        plt.title(x)
        plt.show()
    for x in valores:
        vacref=DataFrame(values=x)
        vacref.plot(kind='bar',colors=colores.values())
        plt.title(x)
        plt.savefig("../resources/plots/"+x+".png")
        plt.close()