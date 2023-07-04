from linked_list import LinkedList
import pytest

@pytest.fixture()
def linked_list_1():
    my_list = LinkedList()
    for i in range(10):
        my_list.add_first(i)
    return my_list

@pytest.fixture()
def linked_list_2():
    my_list = LinkedList()
    for i in range(10):
        my_list.add_last(i)
    return my_list

@pytest.fixture()
def repeated_value():
    my_list = LinkedList()
    for i in range(3):
        my_list.add_first(7)
    return my_list


def test_add_first(linked_list_1):
    assert linked_list_1.head.data == 9
    assert linked_list_1.tail.data == 0
    assert linked_list_1.length == 10

def test_add_last(linked_list_2):
    assert linked_list_2.head.data == 0
    assert linked_list_2.tail.data == 9
    assert linked_list_2.length == 10


def test_remove_first(linked_list_1):
    for i in range(9, -1, -1):
        x = linked_list_1.remove_first()
        assert x == i



def test_remove_last(linked_list_1):
    for i in range(10):
        x = linked_list_1.remove_last()
        assert x == i


def test_reverse(linked_list_1):
    linked_list_1.reverse()
    assert linked_list_1.head.data == 0
    assert linked_list_1.tail.data == 9

def test_remove_and_find(linked_list_1):
    assert linked_list_1.remove_and_find(5) == 5
    assert linked_list_1.remove_and_find(12) == None
    assert linked_list_1.length == 9

def test_peek(linked_list_1):
    assert linked_list_1.peek_first() == 9
    assert linked_list_1.peek_last() == 0

def test_iterator(linked_list_1):
    assert [i for i in linked_list_1] == [i for i in range(9,-1,-1)]

def test_len(linked_list_1):
    assert len(linked_list_1) == 10

def test_has_cycle(linked_list_1):
    assert linked_list_1.has_cycle() == False