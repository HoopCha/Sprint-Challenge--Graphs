def dft_traversal(traversal_path):
    #Depth First Traversal faster?
    s = Stack()
    visited = set()
    s.push(0)
    test=False
    test_room = ''
    s2 = Stack()
    #Keep Searching until every room is visited
    #print("How many Rooms: ", len(room_graph))
    while len(visited) < len(room_graph):
        print(len(traversal_path))
        #Set the current room to the starting Room
        current_room = s.stack[-1]
        #print("Current Room: ", current_room)
        #Add that to visited... because we are there
        visited.add(current_room)
        ##print("Visited Rooms: ", len(visited))
        #Gets all the available directions to go and what rooms they are
        neighbors = room_graph[current_room][1]
        #Create a not visited array. 
        not_visited = []
        #For each item in neighbors
        for direction, room_id in neighbors.items():
            #If the room has not been visited
            if room_id not in visited:
                #Add it to the not visited list
                not_visited.append((room_id, direction))
        #If there is a room that has not been visisted
        if len(not_visited) > 0:
            if len(not_visited) == 1 and test == False and len(s.stack) > 2:
                test = True
                test_room = s.stack[-3]
                s2.push(s.stack[-3])
            #add to the stack the room id of the first item of the not visited array
            s.push(not_visited[0][0])
            #Add to the traversal path the direction you took to go there
            traversal_path.append(not_visited[0][1])
            #print(not_visited[0][1])
        #Else if all currently possible rooms have been visisted
        else:
            #remove that room from the stack
            s.pop()
            checker = False
            #For each item in neighbors
            for direction, room_id in neighbors.items():
                #If the room id is the room we just came from (aka backwords)
                #print("roomid ", room_id," stack",s.stack[-1])
                if room_id == test_room and test == True:
                    test = False
                    checker = True
                    traversal_path.append(direction)
                    s.stack = s2.stack.copy()

            if checker == False:
                for direction, room_id in neighbors.items():
                    if room_id == s.stack[-1]:
                        #go to the room you were last in
                        traversal_path.append(direction)
    #Remove last unessicary move
    traversal_path.pop()
    
dft_traversal(traversal_path)