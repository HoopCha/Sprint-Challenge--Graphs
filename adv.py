from room import Room
from player import Player
from world import World
from util import Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def dft_traversal(traversal_path):
    #Depth First Traversal faster?
    s = Stack()
    visited = set()
    s.push(0)

    #Keep Searching until every room is visited
    #print("How many Rooms: ", len(room_graph))
    while len(visited) < len(room_graph):
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
            #add to the stack the room id of the first item of the not visited array
            s.push(not_visited[0][0])
            #Add to the traversal path the direction you took to go there
            traversal_path.append(not_visited[0][1])
            #print(not_visited[0][1])
        #Else if all currently possible rooms have been visisted
        else:
            #remove that room from the stack
            s.pop()
            #For each item in neighbors
            for direction, room_id in neighbors.items():
                #If the room id is the room we just came from (aka backwords)
                #print("roomid ", room_id," stack",s.stack[-1])
                if room_id == s.stack[-1]:
                    #go to the room you were last in
                    traversal_path.append(direction)
                    #print(direction)
    #Remove last unessicary move
    traversal_path.pop()
    
dft_traversal(traversal_path)
#**********************************#

# s = Stack()
# s.push(0)

# def dft_recursive(traversal_path, s, visited=set()):
    
#     current_room = s.stack[-1]
#     visited.add(current_room)
#     neighbors = room_graph[current_room][1]

#     not_visited = []
#     for direction, room_id in neighbors.items():
#         if room_id not in visited:
#             not_visited.append((room_id, direction))
#     if len(not_visited) > 0:
#         print("a", len(not_visited), len(visited), len(room_graph))
#         for i in not_visited:
#             s.push(not_visited[0][0])
#             traversal_path.append(not_visited[0][1])
#             path = dft_recursive(traversal_path, s, visited)
#             if path is not None and len(visited) == len(room_graph):
#                 print([current_room, *path])
#                 return [current_room, *path]
#     elif len(not_visited) == 0 and len(visited) != len(room_graph):
#         print("b", len(not_visited), len(visited), len(room_graph))
#         s.pop()
#         for direction, room_id in neighbors.items():
#             if room_id == s.stack[-1]:
#                 traversal_path.append(direction)
#                 path = dft_recursive(traversal_path, s, visited)
#                 if path is not None and len(visited) == len(room_graph):
#                     return [current_room, *path]



# traversal_path2 = []
# dft_recursive(traversal_path2, s)
# print(traversal_path2)



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

# for move in traversal_path:
#     print(move)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")