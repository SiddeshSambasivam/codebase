#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict
  
class Graph:
  
    def __init__(self,numCities):
        self.V= numCities
        self.graph = defaultdict(list) 
  
    def addEdge(self,u,v):
        self.graph[u].append(v)
      
    def PathCheck(self, s, d):
        
        visited =[False]*(self.V)
        print(s, d)


        queue=[]

        queue.append(s)
        visited[s] = True

        while(queue):
            
            n = queue.pop(0)
            print('Popped',n,d)
            if n == d :
                return True
            
            for i in self.graph[n]:
                print(f"Source: {n}\nGraph: {self.graph[n]}, i= {i}, Visited: {visited[i]}")
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
            
            return False

def GCD(num1:int, num2:int): 
  
   while(num2): 
       num1, num2 = num2, num1 % num2 
  
   return num1 

def connectedCities(numCities, threshold, originCities, destinationCities):
    # Two possible scenarios
    # 1. direct path to the destination
    # 2. path with intermediate city
    
    vertices = list(set(originCities+destinationCities))
    
    encode = {vertices[i]:i for i in range(numCities)}

    print(encode)
    
    map_ = Graph(numCities)
    
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if GCD(vertices[i], vertices[j]) > threshold or vertices[i] == vertices[j]:
                if not vertices[i] == vertices[j]:
                    print( vertices[i], vertices[j])
                map_.addEdge(i, j)
    
    print(map_.graph)
    result = [0]*len(originCities)
    for i, (start, end) in enumerate(zip(originCities, destinationCities)):
        
        if map_.PathCheck(encode[start], encode[end]):
            result[i] = 1
        
    print(result)
    

# connectedCities(6, 0, [1,4,3,6], [3,6,2,5])
connectedCities(6, 2, [1,2,3], [4,5,6])
