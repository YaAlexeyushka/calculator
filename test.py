from unittest import TestCase
from calculator import *
class test_calc(TestCase):
    
    def test_add(self):
        
        stackk = ["10", "5"]
        
        push(stackk[0])
        push(stackk[1])
        performa()
        assert stack[0] == 15
        delfromstack()
        
    def test_sub(self):
        stackk = ["10", "5"]
        
        push(stackk[0])
        push(stackk[1])
        performs()
        assert stack[0] == 5
        delfromstack()
        
    def test_mul(self):
        stackk = ["10", "5"]
        
        push(stackk[0])
        push(stackk[1])
        performm()
        assert stack[0] == 50
        delfromstack()
        
    def test_div(self):
        stackk = ["10", "5"]
        
        push(stackk[0])
        push(stackk[1])
        performd()
        assert stack[0] == 2
        delfromstack()
        
    def test_fact(self):
        stackk = ["10", "5"]
        
        push(stackk[0])
        push(stackk[1])
        performf()
        assert stack == [10, 120]
        delfromstack()
        delfromstack()
        
    def test_pow(self):
        stackk = ["10", "5"]
        
        push(stackk[0])
        push(stackk[1])
        performp()
        assert stack[0] == 100000
        delfromstack()
        
    def test_root(self):
        stackk = ["10", "5"]
        
        push(stackk[0])
        push(stackk[1])
        performd()
        assert stack[0] == 2
        delfromstack()
        
    def test_mod(self):
        stackk = ["10", "5"]
        
        push(stackk[0])
        push(stackk[1])
        performmd()
        assert stack[0] == 0
        delfromstack()
        
        
        