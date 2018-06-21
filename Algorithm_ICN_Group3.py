# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
import networkx as nx
import matplotlib.pyplot as plt
import random
import threading
import time

#Global variables
G = nx.Graph() 
T = nx.Graph()
path = []
block = 0
total_requests = 10000
lamda_var = 500
mu_var = 1
chosen_graph = G

"""
#test map
T.add_edges_from([('A','B'),('C','B'),('A','C'),('C','D')])
nx.draw(T, with_labels=True)
"""

#Real map
G.add_node('Hannover', pos=(0, 0))
G.add_node('Hamburg', pos=(1.5, 10))
G.add_node('Berlin', pos=(75, 1.5))
G.add_node('Bremen', pos=(-35, 5.5))
G.add_node('Norden', pos=(-72, 10.5))
G.add_node('Dortmund', pos=(-60, -10))
G.add_node('Essen', pos=(-72, -9))
G.add_node('Düsseldorf', pos=(-80, -17))
G.add_node('Köln', pos=(-73, -25))
G.add_node('Frankfurt', pos=(-37, -34))
G.add_node('Leipzig', pos=(55, -14))
G.add_node('Mannheim', pos=(-50, -42))
G.add_node('Karlsruhe', pos=(-56, -51))
G.add_node('Nürnberg', pos=(35, -43))
G.add_node('Stuttgart', pos=(-35, -58))
G.add_node('Ulm', pos=(-7, -68))
G.add_node('München', pos=(45, -75))
G.add_edges_from([('Hannover', 'Hamburg'), ('Hamburg', 'Bremen'), ('Hamburg', 'Berlin'), ('Berlin', 'Leipzig'), ('Leipzig', 'Hannover'), ('Leipzig', 'Nürnberg'), ('Nürnberg', 'München'), ('Hannover', 'Bremen'), ('Norden', 'Bremen'), ('Hannover', 'Dortmund'), ('Dortmund', 'Essen'), ('Norden', 'Dortmund'), ('Essen', 'Düsseldorf'), ('Köln', 'Düsseldorf'), ('Dortmund', 'Köln'), ('Köln', 'Frankfurt'), ('Frankfurt', 'Mannheim'), ('Karlsruhe', 'Mannheim'), ('Karlsruhe', 'Stuttgart'), ('Stuttgart', 'Ulm'), ('Ulm', 'München'), ('Stuttgart', 'Nürnberg'), ('Frankfurt', 'Nürnberg'), ('Frankfurt', 'Leipzig'), ('Frankfurt', 'Hannover'), ('Hannover', 'Berlin')])
pos=nx.get_node_attributes(G,'pos')
nx.draw(G, pos, with_labels=True)

#Show map
plt.show()

#Manage resources 
#all_nodes_test = { 1 :'A', 2 :'B', 3 :'C', 4 :'D'}
#all_nodes = { 1 :'Hannover', 2 :'Hamburg', 3 :'Berlin', 4 :'Bremen', 5 :'Norden', 6 :'Dortmund', 7 :'Essen', 8 :'Düsseldorf', 9 :'Köln', 10 :'Frankfurt', 11 : 'Leipzig', 12 :'Mannheim', 13 :'Karlsruhe', 14 :'Nürnberg', 15 :'Stuttgart', 16 :'Ulm', 17 :'München'}
all_nodes = ['Hannover', 'Hamburg', 'Berlin', 'Bremen', 'Norden', 'Dortmund', 'Essen', 'Düsseldorf', 'Köln', 'Frankfurt', 'Leipzig', 'Mannheim', 'Karlsruhe', 'Nürnberg', 'Stuttgart', 'Ulm', 'München']

#all_links_test = {'A, B': 'mot', 'A, C': 'hai', 'B, C': 'ba', 'C, D': 'tu', 'B, A': 'mot', 'C, A': 'hai', 'C, B': 'ba', 'D, C': 'tu'}
all_links = {'Hannover, Hamburg': 'mot', 'Hamburg, Bremen': 'hai', 'Hamburg, Berlin': 'ba', 'Berlin, Leipzig': 'tu', 'Leipzig, Hannover': 'nam', 'Leipzig, Nürnberg': 'sau', 'Nürnberg, München': 'bay', 'Hannover, Bremen': 'tam', 'Norden, Bremen': 'chin', 'Hannover, Dortmund': 'muoi', 'Dortmund, Essen': 'eleven', 'Norden, Dortmund': 'twelve', 'Essen, Düsseldorf': 'thirteen', 'Köln, Düsseldorf': 'forteen', 'Dortmund, Köln': 'fifteen', 'Köln, Frankfurt': 'sixteen', 'Frankfurt, Mannheim': 'seventeen', 'Karlsruhe, Mannheim': 'eighteen', 'Karlsruhe, Stuttgart': 'ninteen', 'Stuttgart, Ulm': 'twenty', 'Ulm, München': 'twenty-one', 'Stuttgart, Nürnberg': 'twenty-two', 'Frankfurt, Nürnberg': 'twenty-three', 'Frankfurt, Leipzig': 'twenty-four', 'Frankfurt, Hannover': 'twenty-five', 'Hannover, Berlin': 'twenty-six', 'Hamburg, Hannover': 'mot', 'Bremen, Hamburg': 'hai', 'Berlin, Hamburg': 'ba', 'Leipzig, Berlin': 'tu', 'Hannover, Leipzig': 'nam', 'Nürnberg, Leipzig': 'sau', 'München, Nürnberg': 'bay', 'Bremen, Hannover': 'tam', 'Bremen, Norden': 'chin', 'Dortmund, Hannover': 'muoi', 'Essen, Dortmund': 'eleven', 'Dortmund, Norden': 'twelve', 'Düsseldorf, Essen': 'thirteen', 'Düsseldorf, Köln': 'forteen', 'Köln, Dortmund': 'fifteen', 'Frankfurt, Köln': 'sixteen', 'Mannheim, Frankfurt': 'seventeen', 'Mannheim, Karlsruhe': 'eighteen', 'Stuttgart, Karlsruhe': 'ninteen', 'Ulm, Stuttgart': 'twenty', 'München, Ulm': 'twenty-one', 'Nürnberg, Stuttgart': 'twenty-two', 'Nürnberg, Frankfurt': 'twenty-three', 'Leipzig, Frankfurt': 'twenty-four', 'Hannover, Frankfurt': 'twenty-five', 'Berlin, Hannover': 'twenty-six'}
"""
color1    = {'mot': 2  , 'hai': 2  , 'ba' : 2 , 'tu': 2}
color2    = {'mot': 2  , 'hai': 2  , 'ba' : 2 , 'tu': 2}
color3    = {'mot': 2  , 'hai': 2  , 'ba' : 2 , 'tu': 2}
color4    = {'mot': 2  , 'hai': 2  , 'ba' : 2 , 'tu': 2}
color5    = {'mot': 2  , 'hai': 2  , 'ba' : 2 , 'tu': 2}
color6    = {'mot': 2  , 'hai': 2  , 'ba' : 2 , 'tu': 2}
color7    = {'mot': 2  , 'hai': 2  , 'ba' : 2 , 'tu': 2}
color8    = {'mot': 2  , 'hai': 2  , 'ba' : 2 , 'tu': 2}
"""
color1    = {'mot': 2  , 'hai': 2  , 'ba' : 2 , 'tu': 2 , 'nam': 2  , 'sau': 2  , 'bay' : 2 , 'tam': 2 , 'chin': 2  , 'muoi': 2  , 'eleven' : 2 , 'twelve': 2 ,'thirteen': 2  , 'forteen': 2  , 'fifteen' : 2 , 'sixteen': 2 , 'seventeen': 2  , 'eighteen': 2  , 'ninteen' : 2 , 'twenty': 2 , 'twenty-one': 2  , 'twenty-two': 2  , 'twenty-three' : 2 , 'twenty-four': 2 , 'twenty-five': 2 , 'twenty-six': 2}
color2    = {'mot': 2  , 'hai': 2  , 'ba' : 2 , 'tu': 2 , 'nam': 2  , 'sau': 2  , 'bay' : 2 , 'tam': 2 , 'chin': 2  , 'muoi': 2  , 'eleven' : 2 , 'twelve': 2 ,'thirteen': 2  , 'forteen': 2  , 'fifteen' : 2 , 'sixteen': 2 , 'seventeen': 2  , 'eighteen': 2  , 'ninteen' : 2 , 'twenty': 2 , 'twenty-one': 2  , 'twenty-two': 2  , 'twenty-three' : 2 , 'twenty-four': 2 , 'twenty-five': 2 , 'twenty-six': 2}
color3    = {'mot': 2  , 'hai': 2  , 'ba' : 2 , 'tu': 2 , 'nam': 2  , 'sau': 2  , 'bay' : 2 , 'tam': 2 , 'chin': 2  , 'muoi': 2  , 'eleven' : 2 , 'twelve': 2 ,'thirteen': 2  , 'forteen': 2  , 'fifteen' : 2 , 'sixteen': 2 , 'seventeen': 2  , 'eighteen': 2  , 'ninteen' : 2 , 'twenty': 2 , 'twenty-one': 2  , 'twenty-two': 2  , 'twenty-three' : 2 , 'twenty-four': 2 , 'twenty-five': 2 , 'twenty-six': 2}
color4    = {'mot': 2  , 'hai': 2  , 'ba' : 2 , 'tu': 2 , 'nam': 2  , 'sau': 2  , 'bay' : 2 , 'tam': 2 , 'chin': 2  , 'muoi': 2  , 'eleven' : 2 , 'twelve': 2 ,'thirteen': 2  , 'forteen': 2  , 'fifteen' : 2 , 'sixteen': 2 , 'seventeen': 2  , 'eighteen': 2  , 'ninteen' : 2 , 'twenty': 2 , 'twenty-one': 2  , 'twenty-two': 2  , 'twenty-three' : 2 , 'twenty-four': 2 , 'twenty-five': 2 , 'twenty-six': 2}
color5    = {'mot': 2  , 'hai': 2  , 'ba' : 2 , 'tu': 2 , 'nam': 2  , 'sau': 2  , 'bay' : 2 , 'tam': 2 , 'chin': 2  , 'muoi': 2  , 'eleven' : 2 , 'twelve': 2 ,'thirteen': 2  , 'forteen': 2  , 'fifteen' : 2 , 'sixteen': 2 , 'seventeen': 2  , 'eighteen': 2  , 'ninteen' : 2 , 'twenty': 2 , 'twenty-one': 2  , 'twenty-two': 2  , 'twenty-three' : 2 , 'twenty-four': 2 , 'twenty-five': 2 , 'twenty-six': 2}
color6    = {'mot': 2  , 'hai': 2  , 'ba' : 2 , 'tu': 2 , 'nam': 2  , 'sau': 2  , 'bay' : 2 , 'tam': 2 , 'chin': 2  , 'muoi': 2  , 'eleven' : 2 , 'twelve': 2 ,'thirteen': 2  , 'forteen': 2  , 'fifteen' : 2 , 'sixteen': 2 , 'seventeen': 2  , 'eighteen': 2  , 'ninteen' : 2 , 'twenty': 2 , 'twenty-one': 2  , 'twenty-two': 2  , 'twenty-three' : 2 , 'twenty-four': 2 , 'twenty-five': 2 , 'twenty-six': 2}
color7    = {'mot': 2  , 'hai': 2  , 'ba' : 2 , 'tu': 2 , 'nam': 2  , 'sau': 2  , 'bay' : 2 , 'tam': 2 , 'chin': 2  , 'muoi': 2  , 'eleven' : 2 , 'twelve': 2 ,'thirteen': 2  , 'forteen': 2  , 'fifteen' : 2 , 'sixteen': 2 , 'seventeen': 2  , 'eighteen': 2  , 'ninteen' : 2 , 'twenty': 2 , 'twenty-one': 2  , 'twenty-two': 2  , 'twenty-three' : 2 , 'twenty-four': 2 , 'twenty-five': 2 , 'twenty-six': 2}
color8    = {'mot': 2  , 'hai': 2  , 'ba' : 2 , 'tu': 2 , 'nam': 2  , 'sau': 2  , 'bay' : 2 , 'tam': 2 , 'chin': 2  , 'muoi': 2  , 'eleven' : 2 , 'twelve': 2 ,'thirteen': 2  , 'forteen': 2  , 'fifteen' : 2 , 'sixteen': 2 , 'seventeen': 2  , 'eighteen': 2  , 'ninteen' : 2 , 'twenty': 2 , 'twenty-one': 2  , 'twenty-two': 2  , 'twenty-three' : 2 , 'twenty-four': 2 , 'twenty-five': 2 , 'twenty-six': 2}

#Show current resources   
def show_current_resources():
    print ('Current status of the resources:')
    print ('Color1 =',color1)
    print ('Color2 =',color2)
    print ('Color3 =',color3)
    print ('Color4 =',color4)
    print ('Color5 =',color5)
    print ('Color6 =',color6)
    print ('Color7 =',color7)
    print ('Color8 =',color8)

#Find all paths
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if (start == end):
        return [path]
    paths = []
    for node in set(graph.neighbors(start)) - set(path):
        paths.extend(find_all_paths(graph, node, end, path))
    return paths
      
#Find all links for each path and check each link to find all possible paths
def find_optimum_path_and_assign_proper_wavelength(threadName,ttl,all_paths = []):
    final_possible_wavelengths = {}
    possible_paths = []
    possible_costs = []
    
    #check each path
    for x in range(0, len(all_paths)):
        #print ('---------') 
        temp_check_link = []
        check_path = all_paths[x]
        #print('Path',str(x+1),':', check_path)
        possible = ['color1', 'color2', 'color3', 'color4', 'color5', 'color6', 'color7', 'color8']
        
        #Check each link
        for y in range(0, len(check_path)-1):
                    dep = check_path[y]
                    des = check_path[y+1]
                    check_link = dep+', '+des
                    #print('Link',y+1,':',check_link)
                    temp_check_link.append(check_link)
                    
                    #Find number for each link in dict all_links
                    for key in all_links:
                        if (key == check_link):
                            #print ('Key found:',key)
                            link_number = all_links.get(key)
                            break
        
                    #determine all possible wavelengths   
                    if (color1[link_number]==0):  
                        if ('color1' in possible) == True:
                            possible.remove('color1')
                            #print ('remove color1')
            
                    if (color2[link_number]==0):
                        if ('color2' in possible) == True:
                            possible.remove('color2')
                            #print ('remove color2')
                                
                    if (color3[link_number]==0):
                        if ('color3' in possible) == True:
                            possible.remove('color3')
                            #print ('remove color3')
                                
                    if (color4[link_number]==0):
                        if ('color4' in possible) == True:
                            possible.remove('color4')
                            #print ('remove color4')
                                
                    if (color5[link_number]==0):
                        if ('color5' in possible) == True:
                            possible.remove('color5')
                            #print ('remove color5')
                                
                    if (color6[link_number]==0):
                        if ('color6' in possible) == True:
                            possible.remove('color6')
                            #print ('remove color6')
                                
                    if (color7[link_number]==0):
                        if ('color7' in possible) == True:
                            possible.remove('color7')
                            #print ('remove color7')
                                
                    if (color8[link_number]==0):
                        if ('color8' in possible) == True:
                            possible.remove('color8')
                            #print ('remove color8')
    
        #If could find a possible path  
        if (len(possible) > 0):
                    possible_paths.append(check_path)
                    """
                    print ('Possible wavelengths:',possible)
                    print ('Choose wavelength:',possible[0])
                    """
                    
                    #Assume that path is optimum by trying assigning it with one of possible wavelengths (possible[0])
                    for key in temp_check_link:
                        if (possible[0] == 'color1'):
                            color1[all_links.get(key)] -= 1
                        elif (possible[0] == 'color2'):
                            color2[all_links.get(key)] -= 1
                        elif (possible[0] == 'color3'):
                            color3[all_links.get(key)] -= 1
                        elif (possible[0] == 'color4'):
                            color4[all_links.get(key)] -= 1
                        elif (possible[0] == 'color5'):
                            color5[all_links.get(key)] -= 1
                        elif (possible[0] == 'color6'):
                            color6[all_links.get(key)] -= 1
                        elif (possible[0] == 'color7'):
                            color7[all_links.get(key)] -= 1
                        elif (possible[0] == 'color8'):
                            color8[all_links.get(key)] -= 1
                    
                    #show the current status of the resources (debug)
                    #show_current_resources()
                    
                    ###Calculate total cost in each case
                    cost = 0
                    for key in all_links:
                        if (key == 'Hamburg, Hannover'):
                            break
                        else:
                            if (color1[all_links.get(key)] == 1):
                                cost += 4
                            elif (color1[all_links.get(key)] == 0):
                                cost += 16
                            if (color2[all_links.get(key)] == 1):
                                cost += 4
                            elif (color2[all_links.get(key)] == 0):
                                cost += 16
                            if (color3[all_links.get(key)] == 1):
                                cost += 4
                            elif (color3[all_links.get(key)] == 0):
                                cost += 16
                            if (color4[all_links.get(key)] == 1):
                                cost += 4
                            elif (color4[all_links.get(key)] == 0):
                                cost += 16
                            if (color5[all_links.get(key)] == 1):
                                cost += 4
                            elif (color5[all_links.get(key)] == 0):
                                cost += 16
                            if (color6[all_links.get(key)] == 1):
                                cost += 4
                            elif (color6[all_links.get(key)] == 0):
                                cost += 16
                            if (color7[all_links.get(key)] == 1):
                                cost += 4
                            elif (color7[all_links.get(key)] == 0):
                                cost += 16
                            if (color8[all_links.get(key)] == 1):
                                cost += 4
                            elif (color8[all_links.get(key)] == 0):
                                cost += 16
                            
                    possible_costs.append(cost)
                    final_possible_wavelengths[tuple(check_path)] = tuple(possible)[0]
                    
                    #Undo assigning to return to its initial status and prepare for other possbible assignings
                    for key in temp_check_link:
                        if (possible[0] == 'color1'):
                            color1[all_links.get(key)] += 1
                        elif (possible[0] == 'color2'):
                            color2[all_links.get(key)] += 1
                        elif (possible[0] == 'color3'):
                            color3[all_links.get(key)] += 1
                        elif (possible[0] == 'color4'):
                            color4[all_links.get(key)] += 1
                        elif (possible[0] == 'color5'):
                            color5[all_links.get(key)] += 1
                        elif (possible[0] == 'color6'):
                            color6[all_links.get(key)] += 1
                        elif (possible[0] == 'color7'):
                            color7[all_links.get(key)] += 1
                        elif (possible[0] == 'color8'):
                            color8[all_links.get(key)] += 1
        
    """
    #Print final results with optimum path
    print ('---------') 
    print ('IN SUMMARY:')                          
    """
    if (len(possible_paths)>0):
        
        optimum_path = possible_paths[possible_costs.index(min(possible_costs))] 
        #print ('Possible paths:',possible_paths)
        """
        print ('\nPossible costs:',possible_costs)
        print ('\nOptimum cost:',min(possible_costs))
        print ('\nOptimum path:',optimum_path)
        print ('\nChosen wavelength for assigning the optimum path:',final_possible_wavelengths[tuple(optimum_path)])
        """
        #Officially assigning optimum path to the system
        official_links = []
        for y in range(0, len(optimum_path)-1):
                        dep = optimum_path[y]
                        des = optimum_path[y+1]
                        official_links.append(dep+', '+des)
                        
        for key in official_links:
            chosen_wavelength = final_possible_wavelengths[tuple(optimum_path)]                
            if (chosen_wavelength == 'color1'):
                color1[all_links.get(key)] -= 1
            elif (chosen_wavelength == 'color2'):
                color2[all_links.get(key)] -= 1
            elif (chosen_wavelength == 'color3'):
                color3[all_links.get(key)] -= 1
            elif (chosen_wavelength == 'color4'):
                color4[all_links.get(key)] -= 1
            elif (chosen_wavelength == 'color5'):
                color5[all_links.get(key)] -= 1
            elif (chosen_wavelength == 'color6'):
                color6[all_links.get(key)] -= 1
            elif (chosen_wavelength == 'color7'):
                color7[all_links.get(key)] -= 1
            elif (chosen_wavelength == 'color8'):
                color8[all_links.get(key)] -= 1
        #print("\nStarting TTL: "+ str(ttl) + "s")
        time.sleep(ttl)
        #Release back the resources
        for key in official_links:
            chosen_wavelength = final_possible_wavelengths[tuple(optimum_path)]                
            if (chosen_wavelength == 'color1'):
                color1[all_links.get(key)] += 1
            elif (chosen_wavelength == 'color2'):
                color2[all_links.get(key)] += 1
            elif (chosen_wavelength == 'color3'):
                color3[all_links.get(key)] += 1
            elif (chosen_wavelength == 'color4'):
                color4[all_links.get(key)] += 1
            elif (chosen_wavelength == 'color5'):
                color5[all_links.get(key)] += 1
            elif (chosen_wavelength == 'color6'):
                color6[all_links.get(key)] += 1
            elif (chosen_wavelength == 'color7'):
                color7[all_links.get(key)] += 1
            elif (chosen_wavelength == 'color8'):
                color8[all_links.get(key)] += 1
        #show_current_resources()
        
    else:
        #print ('\nThere are not any possible paths for this request - This connection will be blocked.')
        global block
        block += 1
        #print ('\nNumber of blocked connections: '+ str(block))   

#Multithread  
class myThread (threading.Thread):
   def __init__(self, ID, name, start1, end, ttl):
      threading.Thread.__init__(self)
      self.ID = ID
      self.name = name
      self.start1 = start1
      self.end = end
      self.ttl = ttl
   def run(self):
      #print ("\nStarting " + self.name)
      find_optimum_path_and_assign_proper_wavelength(self.name,self.ttl,find_all_paths(chosen_graph, self.start1, self.end, path))
      #print ("\nExiting " + self.name)

#Create new threads pools
i=0
threads = []

#Initiator 
while (i<total_requests):
    lamda = random.expovariate(lamda_var)
    mu = random.expovariate(mu_var)
    start = random.choice(all_nodes)
    all_nodes.remove(start)
    #print (all_nodes1)
    end = random.choice(all_nodes)
    all_nodes.append(start)
    #print (all_nodes1)
    time.sleep(lamda)
    #print("\nWaited " + str(lamda) + "s"+ " for request-" + str(i+1))
    print ("\nIncoming request-" + str(i+1) + ": " + start + " -> " + end)      
    thread = myThread(i+1, "Request-"+str(i+1),start,end,mu)
    threads.append(thread)
    thread.start()
    i += 1
    
#Summary   
for x in threads:
    x.join()
print ("\nDone!")
print ('\nNumber of blocked connections: '+ str(block))
#show_current_resources()
print ("\nTotal requests: " + str(total_requests))
print ("\nLamda: " + str(lamda_var) + "; Mu: " + str(mu_var))
 

"""
#find all paths 
#start = 'C'
#end = 'D'
start = 'Hamburg'
end = 'Karlsruhe'
#all_paths = cp.copy(find_paths(chosen_graph, start, end, path))
print('FROM',start,'TO',end,':')
print('There are intuitively total',len(find_all_paths(chosen_graph, start, end, path)),'path(s) :')
find_optimum_path_and_assign_proper_wavelength("Thread",0.01,find_all_paths(chosen_graph, start, end, path))
""" 

