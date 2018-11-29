"""# --- define acceleration function --- #
def acceleration(planet_data[n]):

    acceleration_vector = np.array([-((G*MSUN*body_one[0])/(distance(sun_pos, body_one)**3))-(
            G*MJUPITER*(body_one[0]-body_two[0])/((distance(body_one, body_two)**3))),-(G*MSUN*body_one[1])/(
                distance(sun_pos, body_one)**3)-(G*MJUPITER*(body_one[1]-body_two[1])/(distance(body_one, body_two)**3))])

    return acceleration_vector

# --- define the recalculations of velocity and position --- #

def iteration(changing_variable, update_variable):
                                   
    iterated_variable = np.add(changing_variable, update_variable*dt, out=changing_variable, casting='unsafe')

    return iterated_variable

# --- define both Approximations --- #
def earthEuler():
    time = 0
    
    earth_acceleration_vector = [0.0,0.0]
    jupiter_acceleration_vector = [0.0,0.0]
    
    for i in range(int(maxnsteps/dt)):
        
        earthsun_distance = distance(planet_data[], earth_pos)
        jupitersun_distance = distance(sun_pos, jupiter_pos)
        jupiterearth_distance = distance(earth_pos, jupiter_pos)
        
        earth_acceleration_vector = acceleration(earth_pos, jupiter_pos)
        jupiter_acceleration_vector = acceleration(jupiter_pos, earth_pos)

        
        earth_pos = iteration(earth_pos, earth_velocity_vector)
        jupiter_pos = iteration(jupiter_pos, jupiter_velocity_vector)


        earth_velocity_vector = iteration(earth_velocity_vector, earth_acceleration_vector)
        jupiter_velocity_vector = iteration(jupiter_velocity_vector, jupiter_acceleration_vector)
        
        #print(accelerationVector)
        #print(math.sqrt(np.dot(accelerationUnitVector, accelerationUnitVector)))
        e_list.append([time, earth_pos[0], earth_pos[1], earth_velocity_vector[0], earth_velocity_vector[1]])
        j_list.append([time, jupiter_pos[0], jupiter_pos[1], jupiter_velocity_vector[0], jupiter_velocity_vector[1]])

        time += dt
        
    return -earth_pos[0], -earth_pos[1], -jupiter_pos[0], -jupiter_pos[1]
        #E = 0.5*Mearth*(xval**2 + yval**2)
        #dlist.append([tval, xval, yval, vxval, vyval])
        #calculate the acceleration before any other value and in x-y parallel


def earthEulerCramer():
    time = 0
    
    earth_acceleration_vector = np.array([0.0,0.0])
    jupiter_acceleration_vector = np.array([0.0,0.0])
    
    for count in range(int(maxnsteps/dt)):
        
        earthsun_distance = distance(sun_pos, earth_pos)
        jupitersun_distance = distance(sun_pos, jupiter_pos)
        jupiterearth_distance = distance(earth_pos, jupiter_pos)

        
        earth_acceleration_vector = acceleration(earth_pos, jupiter_pos)
        jupiter_acceleration_vector = acceleration(jupiter_pos, earth_pos)


        earth_velocity_vector = iteration(earth_velocity_vector, earth_acceleration_vector)
        jupiter_velocity_vector = iteration(jupiter_velocity_vector, jupiter_acceleration_vector)

 
        earth_pos = iteration(earth_pos, earth_velocity_vector)
        jupiter_pos = iteration(jupiter_pos, jupiter_velocity_vector)

        
        #print(accelerationVector)
        #print(math.sqrt(np.dot(accelerationUnitVector, accelerationUnitVector)))
        e_list.append([time, earth_pos[0], earth_pos[1], earth_velocity_vector[0], earth_velocity_vector[1]])
        j_list.append([time, jupiter_pos[0], jupiter_pos[1], jupiter_velocity_vector[0], jupiter_velocity_vector[1]])

        time += dt
        
    return -earth_pos[0], -earth_pos[1], -jupiter_pos[0], -jupiter_pos[1]
        #print(xval, yval)
        #E = 0.5*Mearth*(xval**2 + yval**2)
        #dlist.append([tval, xval, yval, vxval, vyval])
        #calculate the acceleration before any other value and in x-y parallel

"""#Next we want to have a all the recorded data printed into a documents correspoding to each planet
"""


# --- Create a function to create the text documents when an approximation runs --- # 
def getData(choice):
    
    with open("earthPositions"+str(choice)+".txt", "w") as File: # This creates and opens a new text document
    #then labels the document "File"
        for n in range(0, len(e_list)):
        # Every value must be written in
            File.write(str(e_list[n][1])) # The time value is added first
            File.write("\t") # A white space is added so that data is split into two columns
            File.write(str(e_list[n][2])) # The acceleration value is added next
            File.write("\n") # a new line is added so this may repeat for all programs

    with open("jupiterPositions"+str(choice)+".txt", "w") as File: # This creates and opens a new text document
        #then labels the document "File"
        for n in range(0, len(j_list)):
        # Every value must be written in
            File.write(str(j_list[n][1])) # The time value is added first
            File.write("\t") # A white space is added so that data is split into two columns
            File.write(str(j_list[n][2])) # The acceleration value is added next
            File.write("\n") # a new line is added so this may repeat for all programs

    return "complete"

"""#Set an input for either Euler, Euler-Cramer approximations etc
"""
# --- Request user input on which approximation to use --- #

print("For a simple singlar body orbiting the sun we can approximate the orbit in multiple ways")
print("\t")
print("The options of Approximation are Euler and Euler-Cramer")
print("\t")
approximation = input("Enter 1 for Euler, enter 2 for Euler-Cramer or 3 to close the program:  ")
print("\t")


"""
#Once the approximation has been selected we have to make sure the program is able to run based on the input given.
#This is done using a simple if comparison against their approximation number choice.
#It must be such that if they haven't chosen an appropriate value that the program doesnt fail.

#This is solved below by removing all forbidden values (i.e. anything that isnt numeric)


"""
translation_table = dict.fromkeys(map(ord, '¬^£%!@#$qwertyuiopasdfghjklzxcvbnm,.\/|#@[]{}+=-_)(*&'), None)
approximation = approximation.translate(translation_table) 
choice = "blank"
if int(approximation) == 1:

        choice = "Euler"
        print("The Euler approximation will now run")
        print("\t")
        print(earthEuler())
        print("\t")
        print("A text file has been generated with the output values")
        print("\t")
        getData(choice)
        print("\t")
        input("Press any key to close the program")
        
elif int(approximation) == 2:

        choice = "Euler-Cramer"
        print("The Euler-Cramer approximation will now run")
        print("\t")
        print(earthEulerCramer())
        print("\t")
        print("A text file has been generated with the output values")
        print("\t")
        getData(choice)
        print("\t")
        input("Press any key to close the program")

elif int(approximation) == 3:

        print("The program will now close")
        time.sleep(3)

else:
        print("This input is invalid, please restart the program to obtain a value")
        print("\t")
        approximation = input("Press any key to exit")




