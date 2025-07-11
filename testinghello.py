from hello import square
import pytest

def test_positive() :
   assert square(2) == 4
   assert square(3) == 9
def test_neg():
   assert square(-2) == 4
   assert square(-3) == 9
def test_zero():
   assert square(0) == 0





