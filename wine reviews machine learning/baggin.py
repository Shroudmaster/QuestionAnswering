import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

data = pd.read_csv('Behavior of the urban traffic of the city of Sao Paulo in Brazil.csv', sep = ';')
#print(data.Immobilized_bus)
#hour = plt.plot(data.Hour_Coded, ls = '', marker = 'o', label = "hour")



bu1 = plt.plot(data.Immobilized_bus, ls = '', marker = 'o', label = "Immobilized_bus")
broken = plt.plot(data.Broken_Truck, ls = '', marker = 'o', label = "Broken_Truck")
vehicle = plt.plot(data.Vehicle_excess, ls = '', marker = 'o', label = "Vehicle_excess")
accident = plt.plot(data.Accident_victim, ls = '', marker = 'o', label = "Accident_victim")
running = plt.plot(data.Running_over, ls = '', marker = 'o', label = "Running_over")
fayahbusses = plt.plot(data.Fire_vehicles, ls = '', marker = 'o', label = "Fire_vehicles")
occur = plt.plot(data.Occurrence_involving_freight, ls = '', marker = 'o', label = "Occurrence_involving_freight")
incident = plt.plot(data.Incident_involving_dangerous_freight, ls = '', marker = 'o', label = "Incident_involving_dangerous_freight")
electricity = plt.plot(data.Lack_of_electricity, ls = '', marker = 'o', label = "Lack_of_electricity")
fayah = plt.plot(data.Fire, ls = '', marker = 'o', label = "Fire")
flooding = plt.plot(data.Point_of_flooding, ls = '', marker = 'o', label = "Point_of_flooding")
manifest = plt.plot(data.Manifestations, ls = '', marker = 'o', label = "Manifestations")
defects = plt.plot(data.Defect_in_the_network_of_trolleybuses, ls = '', marker = 'o', label = "Defect_in_the_network_of_trolleybuses")
tree = plt.plot(data.Tree_on_the_road, ls = '', marker = 'o', label = "Tree_on_the_road")
semaphore = plt.plot(data.Semaphore_off, ls = '', marker = 'o', label = "Semaphore_off")
intsemaphore =plt.plot(data.Intermittent_Semaphore, ls = '', marker = 'o', label = "Intermittent_Semaphore")
#slow = plt.plot(data.Slowness_in_traffic, ls = '', marker = 'o', label = "Slowness_in_traffic")
plt.legend((bu1[0], broken[0], vehicle[0], accident[0], running[0], fayahbusses[0], occur[0], incident[0], electricity[0], fayah[0], flooding[0], manifest[0], defects[0], tree[0], semaphore[0], intsemaphore[0]),
           ('Immobilized_bus', 'Broken_Truck', 'Vehicle_excess', 'Accident_victim', 'Running_over', 'Fire_vehicles', 'Occurrence_involving_freight', 'Incident_involving_dangerous_freight',
            'Lack_of_electricity', 'Fire', 'Point_of_flooding', 'Manifestations', 'Defect_in_the_network_of_trolleybuses', 'Tree_on_the_road', 'Semaphore_off', 'Intermittent_Semaphore'))
plt.show()
