
#False = 0 and True = 1

import conways_game_of_life as life

def test_life_grid_empty():
    out = [[0, 0, 0, 0],[ 0, 0, 0, 0],[ 0, 0, 0, 0],[0, 0, 0, 0]]
    assert out == life.grid_view([])

def test_life_grid_input():
    out = [[0, 1, 0,1],[ 0, 1,0, 0],[ 0,0, 0, 0],[0, 0, 0,0]]
    assert out == life.grid_view([1,3,5])

def test_life_grid_repeat_input():
    out = [[0, 1, 0,1],[ 0, 1,0, 0],[ 0,0, 0, 0],[0, 0, 0,0]]
    assert out == life.grid_view([1,3,5,1])

def test_position_true_value():
    assert life.position_true([[0,0,0,0]*4]*4) == []

def test_position_true_multiple(): 
    assert life.position_true([[ 1, 0,1, 0],[ 0, 0, 0, 0],[ 0, 1, 0, 0], [0, 0, 0, 0]]) == [[0,0],[0,2],[2,1]]

def test_no_neighbour():
    neighbour, zero_neighbour = life.neighbours( [[ 1, 0,1, 0],[ 0,0, 0, 0],[ 0, 1, 0, 0],[0, 0, 0,0]], [0,0])
    assert neighbour == 0
    assert  zero_neighbour == [[0,1],[1,0],[1,1]]

def test_three_neighbours():
   neighbour, zero_neighbour = life.neighbours( [[ 1, 0,1, 0],[ 0,1, 0, 0],[ 0, 1, 0, 0],[0, 0, 0,0]], [1,1])
   assert neighbour == 3
   assert  zero_neighbour == [[0,1],[1,0],[1,2],[2,0],[2,2]]

def test_no_status_change():
    assert life.status_change( [[ 1, 1, 0, 0],
                            [ 1,1, 0, 0],
                            [ 0, 0, 0, 0],
                            [0, 0, 0,0]]) == [[ 1, 1, 0, 0],
                            [ 1,1, 0, 0],
                            [ 0, 0, 0, 0],
                            [0, 0, 0,0]]
#fail 
def test_status_change():
    assert life.status_change( [[ 0, 0, 0, 0],[ 1, 1, 1, 0],[ 0, 0, 0, 0],[0, 0, 0,0]]) == [[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,0,0,0]]

def test_view_no_true_value():
    out = [[0, 0, 0, 0],[ 0, 0, 0, 0],[ 0, 0, 0, 0],[0, 0, 0, 0]]
    assert out == life.grid_view([[ 0, 0, 0, 0]*4]*4) 
    
#fail
def test_multiple_true_value():
    out = [[ 0, 0, 0, 0], [ 1, 1, 1, 0], [ 0, 0, 0, 0], [0, 0, 0, 0]]
    assert out == life.grid_view([[ 0, 0, 0, 0],[ 1, 1, 1, 0],[ 0, 0, 0, 0],[0, 0, 0,0]])