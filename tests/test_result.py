import pytest
from   algo import Calculator



class TestCalculator:


    def setup_class(self):
        self.calc = Calculator()
    def setup(self):
        print('开始计算')
    def teardown(self):
        print('结束计算')
    def teardown_class(self):
        print('结束测试')
    

    @pytest.mark.parametrize("a,b,expect",[
        (1,1,2)
    ])
    # @pytest.mark.P0
    def test_case_01(self,a,b,expect):
        assert self.calc.add(a,b) == expect




    @pytest.mark.parametrize("a,b,expect",[    
        (-0.01,0.02,0.01)
    ])
    # @pytest.mark.P0
    def test_case_02(self,a,b,expect):
        assert self.calc.add(a,b) == expect
        


    @pytest.mark.parametrize("a,b,expect",[  
        (10,0.02,10.02)
    ])
    # @pytest.mark.P0
    def test_case_03(self,a,b,expect):
        assert self.calc.add(a,b) == expect
        



    @pytest.mark.parametrize("a,b,expect",[   
        (98.99,99,197.99)
    ])
    # @pytest.mark.P1
    def test_case_04(self,a,b,expect):
        assert self.calc.add(a,b) == expect




    @pytest.mark.parametrize("a,b,expect",[ 
        (99,98.99,197.99)
    ])
    # @pytest.mark.P1
    def test_case_05(self,a,b,expect):
        assert self.calc.add(a,b) == expect




    @pytest.mark.parametrize("a,b,expect",[ 
        (-98.99,-99,-197.99)
    ])
    # @pytest.mark.P1
    def test_case_06(self,a,b,expect):
        assert self.calc.add(a,b) == expect




    @pytest.mark.parametrize("a,b,expect",[ 
        (-99,-98.99,-197.99)
    ])
    # @pytest.mark.P1
    def test_case_07(self,a,b,expect):
        assert self.calc.add(a,b) == expect




    @pytest.mark.parametrize("a,b,expect",[ 
        (99.01,0,'参数大小超出范围')
    ])
    # @pytest.mark.P1
    def test_case_08(self,a,b,expect):
        assert self.calc.add(a,b) == expect




    @pytest.mark.parametrize("a,b,expect",[ 
        (-99.01,-1,'参数大小超出范围')
    ])
    # @pytest.mark.P1
    def test_case_09(self,a,b,expect):
        assert self.calc.add(a,b) == expect




    @pytest.mark.parametrize("a,b,expect",[
        (2,99.01,'参数大小超出范围')
    ])
    # @pytest.mark.P1
    def test_case_10(self,a,b,expect):
        assert self.calc.add(a,b) == expect




    @pytest.mark.parametrize("a,b,expect",[
        (1,-99.01,'参数大小超出范围')
    ])
    # @pytest.mark.P1
    def test_case_11(self,a,b,expect):
        assert self.calc.add(a,b) == expect




    @pytest.mark.parametrize("a,b,expect",[
        ('文',9.3,'TypeError')
    ])
    # @pytest.mark.P1
    def test_case_12(self,a,b,expect):
        assert self.calc.add(a,b) == expect





    @pytest.mark.parametrize("a,b,expect",[ 
        (4,'字','TypeError')
    ])
    # @pytest.mark.P1
    def test_case_13(self,a,b,expect):
        assert self.calc.add(a,b) == expect





    @pytest.mark.parametrize("a,b,expect",[
        ('nu',0.2,'TypeError')
    ])
    # @pytest.mark.P1
    def test_case_14(self,a,b,expect):
        assert self.calc.add(a,b) == expect




    @pytest.mark.parametrize("a,b,expect",[  
        (30,'t','TypeError')
    ])
    # @pytest.mark.P1
    def test_case_15(self,a,b,expect):
        assert self.calc.add(a,b) == expect





    @pytest.mark.parametrize("a,b,expect",[  
        ('*&',0.2,'TypeError')
    ])
    # @pytest.mark.P1
    def test_case_16(self,a,b,expect):
        assert self.calc.add(a,b) == expect




    @pytest.mark.parametrize("a,b,expect",[ 
        (21.45,'@','TypeError')
    ])
    # @pytest.mark.P1
    def test_case_17(self,a,b,expect):
        assert self.calc.add(a,b) == expect




    @pytest.mark.parametrize("a,b,expect",[  
        ('',20.93,'TypeError')
    ])
    # @pytest.mark.P2
    def test_case_18(self,a,b,expect):
        assert self.calc.add(a,b) == expect




    @pytest.mark.parametrize("a,b,expect",[ 
        (-3,'','TypeError')
    ])
    # @pytest.mark.P2
    def test_case_19(self,a,b,expect):
        assert self.calc.add(a,b) == expect

    

