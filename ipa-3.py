'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    from_dict = social_graph [from_member]
    to_dict = social_graph [to_member]
    from_follows = from_dict ["following"]
    to_follows = to_dict ["following"]
    from_follows.count (to_member)
    to_follows.count (from_member)
    relationship_status_counter = from_follows.count (to_member) + to_follows.count (from_member)
    if relationship_status_counter == 2:
        return ("friends")
    elif relationship_status_counter == 0:
        return ("no relationship")
    else:
        if from_follows.count (to_member) == 1:
            return ("follower")
        else:
            return ("followed by")


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    board_size = len (board)

    vertical_set = []
    for i in range (board_size):    
        vertical_set.append([list[i] for list in board])
    
    diagonal_set_a = []
    for i in range (board_size):
        diagonal_set_a.append(board[i][i])
        
    diagonal_set_b = []
    for i in range (board_size):
        diagonal_set_b.append(board[i][board_size - 1 - i])
        
    player_1 = any(list.count("X") == board_size for list in board ) or any(list.count("X") == board_size for list in vertical_set) or diagonal_set_a.count("X") == board_size or diagonal_set_b.count("X") == board_size
    player_2 = any(list.count("O") == board_size for list in board ) or any(list.count("O") == board_size for list in vertical_set) or diagonal_set_a.count("O") == board_size or diagonal_set_b.count("O") == board_size
   
    if player_1:
        return ("X")
    elif player_2:
        return ("O")
    else:
        return ("NO WINNER")        


def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    new_list = []
    for list in route_map:
        new_elements = [list[0]]
        new_list = new_list + new_elements
    
    start = new_list.index(first_stop)
    end = new_list.index(second_stop)
    condition = start < end

    if condition == True:
        total_time = 0
        for number in range (0, end - start):
            start_name = new_list[start + number]
            end_name = new_list[start + 1 + number]
            time_finder = route_map [start_name,end_name]            
            travel_time = time_finder ["travel_time_mins"]
            total_time = total_time + travel_time
        return (total_time)
    
    else:
        total_time_1 = 0
        for number in range (0, len(new_list) - start - 1):
            start_name_a = new_list[start + number]
            end_name_a = new_list[start + 1 + number]
            time_finder_a = route_map [start_name_a,end_name_a]            
            travel_time_a = time_finder_a ["travel_time_mins"]
            total_time_1 = total_time_1 + travel_time_a

        start_name_b = new_list[len(new_list) - 1]
        end_name_b = new_list[0]
        time_finder_b = route_map [start_name_b,end_name_b]
        travel_time_b = time_finder_b ["travel_time_mins"]        
        total_time_2 = travel_time_b

        total_time_3 = 0
        for number in range (0, end):
            start_name_c = new_list[number]
            end_name_c = new_list[number + 1]
            time_finder_c = route_map [start_name_c,end_name_c]
            travel_time_c = time_finder_c ["travel_time_mins"]
            total_time_3 = total_time_3 + travel_time_c
        return (total_time_1 + total_time_2 + total_time_3)
