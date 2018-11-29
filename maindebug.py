# Python Solar System Sim 2.0;
# Earth-Juptier-Sun interacting w/ intermediate functions
import math 
import cmath
import numpy as np
import time # used to adjust final output

"""Import numpy to use vectors and create shorter code"""
# define key variables

""" Using standard units defined by
T = 31557600 # 1 year in seconds
au = 149597870.7 # 1 astronomical unit
Msun = 1.9891*math.pow(10, 30)
"""

# ------- Define all universal constants -------- #

G = 4*(math.pi)**2
MSUN = 1
MEARTH = 3.3*MSUN*math.pow(10, -6)
MJUPITER = 1.05*MSUN*math.pow(10, -3)
dt = 0.01# Set the time step each iteration undergoes
maxnsteps = 0.05

# --- Give initial positions and velocities --- #
"""Consider making this user input later on"""
""" Sun index 0 -> Earth index 1 -> Jupiter index 2"""


planet_mass = [MSUN, MEARTH, MJUPITER]
planet_position = [np.array([0.0, 0.0]), np.array([1.0, 0.0]),np.array([5.2, 0.0])]
planet_velocity = [[0.0, 0.0],[0.0, 2*math.pi], [0.0, 2.68754684]]

#earth_pos = np.array([1.0, 0.0])
#jupiter_pos = np.array([5.2, 0.0])

#earth_velocity_vector = np.array([0.0, 2*math.pi]) 
#jupiter_velocity_vector = np.array([0.0, 2.68754]) # In notes 

# --- Give each planet a list to record plot values to --- #

e_list=[] 
j_list=[]

dimension = 2

"""Use vectors to define the orbit"""
# --- define distance function --- #
def distance(body_one, body_two):
    
    distance = math.sqrt(np.dot(body_one[0] - body_two[0],body_one[0] - body_two[0]))
    #print(distance)
    return distance

# --- define acceleration function --- #
def acceleration(body_one):
    acceleration_vector = [0.0,0.0]
    
    for i in range(3) :

        if (distance(planet_position[i],body_one)**3) != 0:
            
            acceleration_vector[0] = acceleration_vector[0] +(G*planet_mass[i]*(planet_position[i][0]-body_one[0]))/(distance(planet_position[i],body_one)**3)
            acceleration_vector[1] = acceleration_vector[1] +(G*planet_mass[i]*(planet_position[i][1]-body_one[1]))/(distance(planet_position[i],body_one)**3)
            #print(acceleration_vector)
            
    #print(acceleration_vector)
    return acceleration_vector
        

# --- define the recalculations of velocity and position --- #

def iteration(changing_variable, update_variable):
        
    iterated_variable = [changing_variable[0] + update_variable[0]*dt, changing_variable[1] + update_variable[1]*dt]
    #print(iterated_variable)               
    return iterated_variable



# --- define both Approximations --- #
def earthEuler():
    time = 0
    
    earth_acceleration_vector = [0.0,0.0]
    jupiter_acceleration_vector = [0.0,0.0]
    planet_position = [np.array([0.0, 0.0]), np.array([1.0, 0.0]),np.array([5.2, 0.0])]
    planet_velocity = [np.array([0.0, 0.0]),np.array([0.0, 2*math.pi]), np.array([0.0, 2.68754684])]
    
    for _ in range(int(maxnsteps/dt)):
        
        earth_acceleration_vector = acceleration(planet_position[1])
        jupiter_acceleration_vector = acceleration(planet_position[2])

        #print(earth_acceleration_vector)
        #print(jupiter_acceleration_vector)

        sun_pos = [0.0, 0.0]
        earth_pos = iteration(planet_position[1], planet_velocity[1])
        jupiter_pos = iteration(planet_position[2], planet_velocity[2])
        #print(earth_pos, jupiter_pos)

        sun_velocity = [0.0, 0.0]
        earth_velocity = iteration(planet_position[1], earth_acceleration_vector)
        jupiter_velocity = iteration(planet_velocity[2], jupiter_acceleration_vector)
        #print(earth_pos)
        #print(jupiter_pos)
    
            
        planet_position = [sun_pos, earth_pos, jupiter_pos]
        planet_velocity = [sun_velocity, earth_velocity, jupiter_velocity]
        #print(earth_velocity)
        #print(jupiter_velocity)
        e_list.append([time, earth_pos[0], earth_pos[1], earth_velocity[0], earth_velocity[1]])
        j_list.append([time, jupiter_pos[0], jupiter_pos[1], jupiter_velocity[0], jupiter_velocity[1]])

        time += dt
        
    return -planet_position[1][0], -planet_position[1][1], -planet_position[2][0], -planet_position[2][1]

print(earthEuler())
