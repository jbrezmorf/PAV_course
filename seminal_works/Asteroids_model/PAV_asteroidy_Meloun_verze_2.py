#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 08:32:17 2018

@author: zbysek
"""
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.integrate as integrate

"""Základní měnitelné parametry"""
N = 20# počet hmotných bodů
dt = 12 # jednotka: mon (měsíc) - doba jednoho integračního kroku
hranice = 30 # AU - hranice Sluneční soustavy (kde nejdál se budou generovat shluky)
hranice_lim = 2 # krát hranice, násobek hodnoty hranice, kde končí zobrazení
                    # a vlastnosti objektů jsou anulovány
kst = 1e-1 # konstanta úměrnosti pro velikost koleček představujících hmotnost tělesa

"""Víceméně neměnné konstanty"""
G_new = 1.4430834462989718e-08 # AU^3/(Me.měsíc^2) - gravitační konstanta přepočtená na větší jednotky
Ms = 333000 #*Me - hmotnost Slunce v násobcích hmotnosti Země
ds = 1e-3 # AU - poloměr Slunce
m_teles = 14000 # Me - celková hmotnost všech asteroidů
m0 = 14 #  Me - násobek hmotností Země, počáteční hmotnost jednoho shluku asteroidů
d0 = 1/2 # AU - počáteční poloměr shluků asteroidů
t0 = 0 # čas 0
#tf = 12*100000 # mon - konečný čas simulace v měsících
tf = 12*100 # mon - konečný čas simulace v měsících
cas_mezi_snimky = 25

"""Výpočet G_new"""
#G = 6.674e-11 # m3.kg-1.s-2 - gravitační konstanta
#G_new_vypocet = G*(AU**3/(Me*3600*24*30)) # AU^3/(Me.měsíc^2)
#AU = 149597887e3 # m - astronimická jednotka (vzdálenost Země-Slunce, použitá pouze pro výpočet G_new)
#Me = 5.9736e24 # kg - hmotnost Země (použitá pouze pro výpočet G_new)

"""Odkomentovat pro zobrazení dráhy shluků (jednen kus kódu ze tří: 1/3)"""
#cara = list()
#for teleso in range(N):
#    cara.append([telesa[teleso, (0, 1)]])

def animate(i):
    print("Compute frame: ", i)
    """Funkce postupuje funkci animation.FuncAnimate aktuální bod pro zobrazení
    z řady generované funkcí integrate.solve_ivp"""
    
    reseni = integrate.solve_ivp(let, (0, dt), telesa.ravel(), method="RK45", t_eval=(0, dt)) # řešič vrací aktuální pozici bodů

    telesa[:, 0:4] = reseni.y[:, -1].reshape((-1, 6))[:, 0:4]
    
    """Následující část odkomentovat pro zobrazení dráhy planet, blit=False, jinak
    to nefunguje (2/3)"""         
#    for teleso in range(N):
#        cara[teleso] = np.concatenate((cara[teleso], [telesa[teleso+1, (0, 1)]]), axis=0)
#    for n, car in enumerate(linky):
#        car.set_data(cara[n].T)
        
    body1.set_offsets(telesa[:, (0, 1)]) # Změna pozic bodů pro scatter plot - vizualizace hmotnosti
    body2.set_offsets(telesa[:, (0, 1)]) # Změna pozic bodů pro scatter plot - vizualizace průměru
    body1.set_sizes(((telesa[:, 4])**(1/3)*kst*body_na_jednotku_x)**2) # změna hmotnosti
    body2.set_sizes((telesa[:, 5]*body_na_jednotku_x*2)**2) # změna průměru shluku
    time_text.set_text(time_template % (i*dt/12)) # změna času - zobrazení
        
    return body1, body2, linky, time_text

def let(cas, telesa_ravel):
    """Funkce zadávající hodnoty zrychlení pro integraci pomocí integrate.solve_ivp.
    Po zpracování jsou výstupem hodnoty zintegrovaných závisle proměnných levých stran
    Promene:
        :cas: aktuálně hodnocený čas, z řady čas z intervalu t0 až tf
        :telesa_ravel: Do 1-D řady rozložená tabulka/matice informací o tělesech: telesa.
                        Jsou z ní vybírány především výchozí polohy a rychlosti"""
    
    telesa2 = telesa_ravel.reshape((-1, 6)) # seřazení vstupu do původní řady/matice
    telesa_a = telesa2.copy() # vytvoření kopie vstupu
    telesa_a[:, 0:2] = telesa2[:, 2:4] # přepis sloupců 0, 1 na vektory rychlostí
    
    for k in range(1, N+1): # budeme řešit výslednou sílu působící na těleso k
        if telesa2[k, 0:2].all != 0.0: # nebudou se hodnotit působící síly pro tělesa s polohou [0, 0]
                                        # - všechna tělesa, která se dostanou moc blízko nebo moc daleko od Slunce
                                        # jsou vynulována (pozice, rychlosti, hmotnosti, průměry = 0)
#            m0 = telesa[k, 4] # z tabulky/matice telesa vybereme hmotnost telesa k jako m0
            r0 = telesa2[k, 0:2].copy() # z tabulky telesa vybereme souřadnice tělesa k jako r0[x0, y0]
            r = r0 - telesa2[:, 0:2] # vytvoříme řadu vektorů r udávajících polohu všech těles vůči tělesu k
            r_vel = la.norm(r, axis=1) # velikost polohových vektorů určíme jako normu vektoru
#            r_vel = np.sqrt(np.sum(r*r, axis=1)) # vytvoříme řadu obsahující pro každé těleso vzdálenost od tělesa k
            """V následující části se testují srážky pomocí funkce srazky(a, b, c, tmax)."""
            v_0 = telesa2[k, 2:4] # rychlost sledovaného shluku
            Vs = telesa2[:, 2:4] - v_0 # rychlost všech ostatních shluků vůči sledovanému shluku
            Vs_vel = la.norm(Vs, axis=1) # velikost všech rychlostí ostatních shluků vůči sledovanému
            l_0 = telesa2[k, 5] # poloměr sledovaného shluku
            l = telesa2[:, 5] + l_0 # minimální vzdálenost vůči ostatním shlukům, menší vzdálenost už znamená srážku  
            T = srazka((Vs_vel**2), (2*r_vel*Vs_vel), (r_vel**2-l**2), dt) # volání funkce pro zjištění srážek
#                print(T)
            delka_T = len(T)
            if delka_T > 0: # Pokud jsou detekovány srážky, všechny vlastnosti těles budou sloučeny
                for n in T:
                    hmotnost_sum = telesa2[k, 4] + telesa2[n, 4] # výsledná hmotnost
                    telesa_a[k, 0:2] = ((telesa2[k, 2:4]*telesa2[k, 4]+
                                        telesa2[n, 2:4]*telesa2[n, 4])/hmotnost_sum) # výsledná rychlost (hmotností vážený průměr)
                    telesa2[k, 0:2] = ((telesa2[k, 0:2]*telesa2[k, 4]+
                                        telesa2[n, 0:2]*telesa2[n, 4])/hmotnost_sum) # výsledná poloha (hmotností vážený průměr)
                    telesa2[k, 5] = np.sqrt((telesa2[k, 5]**2 + telesa2[n, 5]**2)/2) # výsledný poloměr shluku (kvadratický průměr)
                    telesa2[k, 4] = hmotnost_sum

                    telesa2[n, :] = 0.0 # shluk, jehož vlastnosti byly přiřazeny sledovanému shluku k, je nulován
                    telesa_a[n, :] = 0.0
            """"""
            r0 = telesa2[k, 0:2].copy() # z tabulky telesa vybereme souřadnice tělesa k jako r0[x0, y0]
            r = r0 - telesa2[:, 0:2] # vytvoříme řadu vektorů r udávajících polohu všech těles vůči tělesu k
            r_vel = la.norm(r, axis=1)
            if 1 > r_vel[0] or r_vel[0] > hranice*hranice_lim: #Nulování tělesa, pokud je moc blízko nebo daleko
                                                 #od Slunce
                telesa_a[k, :] = 0.0
                telesa[k, :] = 0.0
            else:
                r_vel[k] = 1.0 # vzdálenost vůči tělesu k samotnému je pochopitelně nulová, zde ji nastavujeme na 1.0
                a_vektory = np.multiply(-G_new*telesa2[:,4].reshape(N+1, 1)*np.power(r_vel.reshape(N+1, 1), -3), r)
                # a_vektory - pomocí Newtonova zákona gravitace spočítány aktuální vektory zrychelní
                a_all_k = np.sum(a_vektory, axis=0) # Výsledný vektor zrychlení působící na shluk k
                telesa_a[k, 2:4] = a_all_k
    telesa_a[0, :] = 0.0 # nulování výstupu pro Slunce - počítáme s ním jako statickým objektem
    telesa_a[:, 4:6] = 0.0 # nulování sloupců 4 a 5 na výstupu (měnily by integraci)
    telesa[:, 4:6] = telesa2[:, 4:6]
    return telesa_a.ravel()

def srazka(a, b, c, tmax):
    """Funkce vyhodnocuje kvadratickou nerovnici ve smyslu existence řešení
    v intervalu (0, tmax)."""
    
    D = b**2 - 4*a*c # determinant
    T = list() # pokud nedojde ke srážce je vrácen prázdný list T
    for k in range(1, N+1):
        if D[k] > 0:
            t1 = (-b[k] + np.sqrt(D[k]))/(2*a[k])
            t2 = (-b[k] - np.sqrt(D[k]))/(2*a[k])
            plus = 0
            if (0 > t1 and t2 > tmax) or (0 > t2 and t1 > tmax):
                plus = k
#                T_plus[0, 0] = t1
#            if 0 < t2 < tmax:
#                plus = k
#                T_plus[0, 1] = t2
            if plus == k:
#                T_plus[0, 2] = k
                T.append(k)
    return T # list T obsahuje identifikátory těles v matici telesa, které určují tělesa účastnící se srážky
        
def init_telesa():
    """Zavádí tabulku/matici obsahující všechny aktuální informace o tělesech ve sluneční soustavě"""
    rozlozeni_R = (1, hranice) # hmota je na počátku rovnoměrně rozmístěna mezi dvěma hodnotami y
    rozlozeni_alfa = (0, 2*np.pi) # hmota je na počátku rovnoměrně rozdělena do kruhu
    
    R_vsechna = np.random.uniform(rozlozeni_R[0], rozlozeni_R[1], N) # náhodné body z rovnoměrného rodělení
    alfa_vsechna = np.random.uniform(rozlozeni_alfa[0], rozlozeni_alfa[1], N)
    
    m0_vsechna = np.ones(N)*m0 
    d0_vsechna = np.ones(N)*d0
    x0_vsechna = R_vsechna*np.cos(alfa_vsechna)
    y0_vsechna = R_vsechna*np.sin(alfa_vsechna) # rovnoměrné rozdělení v mezikruží 0.1 AU až 30 AU
    
    """Výpočet počáteční kruhové rychlosti shluků"""
    vx0_vsechna = np.zeros(N)
    vy0_vsechna = np.zeros(N)
    epsilon = 0.0 # řízení rozptylu náhodného vektoru rychlosti, doporučeno v intervalu (0.001,0.1)
    velikost_R = np.sqrt(np.sum((x0_vsechna**2, y0_vsechna**2), axis=0))
    beta = np.sqrt(G_new*Ms*velikost_R**-1)
#    beta = G_new*Ms/velikost_R # po odkomentování všechna tělesa poletí do Slunce
    vx0_vsechna = beta*(-y0_vsechna/velikost_R)
    vy0_vsechna = beta*(x0_vsechna/velikost_R)
    Ex = vx0_vsechna*epsilon*np.random.rand() # náhodná složka počáteční rychlosti shluků x a o řádek níže y
    Ey = vy0_vsechna*epsilon*np.random.rand() 
    vx0_vsechna += Ex
    vy0_vsechna += Ey
        
    slunce = np.array([0, 0, 0, 0, Ms, ds])
    telesa = np.stack((x0_vsechna, y0_vsechna, vx0_vsechna, vy0_vsechna, m0_vsechna,
                      d0_vsechna), axis=1) # tabulka/matice pro N těles: každé má svou,
                                         # x0, y0, vx0, vy0, vzdálenost od Slunce
    telesa = np.r_[slunce[None, :], telesa] # zahrnutí Slunce do celkové matice/tabulky
    
    return telesa

def init_ani():
    """Zavádí všechny důležité objekty do animace, definuje zobrazovací plátno - figure."""
    fig = plt.figure(dpi=72, figsize=(14,14)) # aby zobrazení odpovícalo rozlišení značek 72 dpi + nastavení
                                              # velikosti zobrazení
    ax = fig.add_subplot(111)
    ax.grid()
#    ax.axis('equal')
    lim = hranice_lim*hranice # Nastavuje hranici zobrazení (1.2 x hranice sluneční soustavy)
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim) 

    osa_x = 2*abs(ax.get_xlim()[0]) # zjišťuje délku osy_x v jejích jednotkách [AU]
    dpi_fig = fig.dpi # rozlišení "figure"
    inch_x = fig.get_size_inches()[0] # rozměr "figure" ve směru osy x v jednotkách [inch]
#    inch_y = fig.get_size_inches()[1]
    
#    vyska_procenta = ax.get_position().height
    sirka_procenta = ax.get_position().width # kolik procent z celkové šířky "figure" zabírá osa x
    
    body_na_jednotku_x = (sirka_procenta*inch_x*dpi_fig)/osa_x # určuje přepočet pro správné zobrazení velikosti shluků
                                                               # - scatter plot má vlastní jednotky dpi^2 
    
    time_template = 'čas = %.1flet' # vzor pro přepis času v obrázku
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes) # umístění informace o čase
    
    body1 = ax.scatter([], [], marker="o", alpha=0.5, color="red") # zavedení teček rezprezentujících hmotnosti
    body2 = ax.scatter([], [], marker="o", alpha=0.5, color="None", edgecolor="blue" ) # zavedení kružnic zobrazující průměry shluků
    sol1 = ax.scatter(0, 0, marker="o", s=(Ms**(1/3)*kst*body_na_jednotku_x)**2, c="yellow", alpha=0.8) # bod reprezentující hmotnost Slunce
    sol2 = ax.scatter(0, 0, marker="o", s=(ds*body_na_jednotku_x*2)**2, color="None", edgecolors="blue") # kružnice reprezentující průměr Slunce
    
    """Odkomentovat níže pro zobrazení křivek letu. (3/3)"""    
    linky = []
#    for n in range(N):
#        car, = ax.plot([], [], c="red", lw = 1, ls="--")
#        linky.append(car,)
#    
    return fig, body1, body2, sol1, sol2, time_text, body_na_jednotku_x, time_template, linky
    
if __name__ == "__main__":
    
    telesa = init_telesa()
    fig, body1, body2, sol1, sol2, time_text, body_na_jednotku_x, time_template, linky = init_ani()
    #reseni = integrate.solve_ivp(let, (0, dt), telesa.ravel(), method="RK45")#, t_eval=np.linspace(0, dt*100, dt))
    ani = animation.FuncAnimation(fig, animate, frames=tf, repeat=False, blit=False, interval=cas_mezi_snimky)
    plt.show()
#
#pro rozběhnutí nebo zastavení animace fungují příkazy níže:
##pause
#ani.event_source.stop()
##
###unpause
# ani.event_source.start()
