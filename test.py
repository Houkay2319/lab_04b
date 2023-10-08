import lib

list = [ [2, 5, 5, 6, 7, 4] , [2, 5, 4, 7] , [2, 5] ]
def test_on_correct_n():
    assert lib.count_common_elements(list) == 4
