import sys

import pytest
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class TestClass:

    def test_first(self):
        assert 5 not in [1,2,3,4]

    def test_second(self):
        local_str="abcdefgh"
        assert 'abc' in local_str


    @pytest.mark.stringtest
    def test_str_exist(self):
        s1="abcdefg"
        s2="wxyzabc"
        assert s2[-3:] in s1


    @pytest.mark.stringtest
    def test_actual(self):
        s1='abcdefg'
        s2='wxyzabc'
        assert len(s1)==len(s2)



    @pytest.mark.xfail(sys.platform=='linux',reason='Works only in windows 32')
    def test_pass(self):
        assert 2==2



