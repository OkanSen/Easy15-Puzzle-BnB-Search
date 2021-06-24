from Board import goal, find_indexOf, find_possible_moves, calculate_h2, success, move, print_board
import math
import copy
from copy import deepcopy
import time


def printPath(board, node_root):
    if not node_root:
        return
    
    print_board(board)

def BnB_Search(board):

    # Store current board as starting state
    starting_state = deepcopy(board)

    # If somehow the garbled board is equal to the goal, then complete the game.
    if starting_state == goal:
        success(board,node_dict={}, numOf_nodes_generated=0)

    # store starting state's heuristic score
    starting_score = calculate_h2(starting_state)   

    # for a loop
    finish = False

    # Create an empty dictionary for all nodes
    # we used dictionary which are really similar to queues, but we can also store multiple values in it
    # for easier problem solving
    # dictionaries are very dynamic compared to lists or arrays
    all_nodes = {}
  
    node_index = 0

    # First index of dictionary is starting board we have generated
    # A node stores; State: its current puzzle
    # Parent: its parent node, # action: which action we take to get to this state
    # h_Score: cumulative score of heuristc/manhattan distance, dynamic_tag: boolean to state if it has dynamic appearance
    all_nodes[node_index] = {"state": starting_state, "parent": "root", "action": "start", "h_score": starting_score, "Dynamic_Tag": False} 
    

    # keep looping through    
    failure = False
    while not failure:
        # iterate through all nodes in the dictionary
        for node in all_nodes.copy():
            repeat = False   

            # the current state that we are going to get moves from
            current_state = all_nodes[node]["state"]
            score_parent = all_nodes[node]["h_score"] #store its score too
            
            # Find the actions corresponding to the state
            available_moves = find_possible_moves(current_state)
            

            # Iterate through each action that is allowed
            for action in available_moves:
                # Find the successor state for each action
                successor_state = move(current_state, action)
                # Calculate this state's score as well
                temp_score = calculate_h2(successor_state)

                # Check if the state has already been seen
                for node_num, node in all_nodes.items():
                    # if the same state is in the list
                    if node["state"] == successor_state:
                        # if parents are same states
                        if node["parent"] == current_state: # then it is a loop and do not add this
                            repeat = True

                        # Here we augment the search algo with dynamic coding. 
                        # We check if the state has the same state in the tree and remove the one with worse cost
                        # check for dynamic addition 

                        # if parents are different
                        else: # then we know this state is already inside the list, and we should compare which has a better score/cost
                            if temp_score < node["h_score"]:
                                # If the new state has a better score then we tag the node added before to know it has a better one
                                node["Dynamic_Tag"] = True # tag old node true
                                break
                            else:
                                # If the new state has a score worse than the other state, simply do not add it
                                repeat = True
                                break

                
                # Check if the state is the goal state
                # If the best state is the goal, stop iteration
                if successor_state == goal:
                    all_nodes[node_index] = {"state": successor_state, "parent": current_state, "action": action, "h_score": 0, "Dynamic_Tag": False}
                    
                    # Complete the game
                    success(board, all_nodes, node_index, True)
                    finish = True
                    break
                
                # If the current state has not been tagged as repeat, now we can add this to the tree
                if not repeat:
                    node_index += 1
                    
                    score = calculate_h2(successor_state)   

                    # add node's parent's score to its score so when we need it we don't have to traverse all the way up
                    score = score + score_parent
                    
                    all_nodes[node_index] = {"state": successor_state, "parent": current_state, "action": action, "h_score": score, "Dynamic_Tag": False}


                else:
                    continue
        
            if finish:
                break
        # The available nodes are now all the successor nodes sorted by score
        sorted(all_nodes.items(), key=lambda k_v: k_v[1]['h_score'])

        # If completed break loop
        if finish:
            break

    return



