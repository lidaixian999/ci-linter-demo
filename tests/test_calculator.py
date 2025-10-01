# tests/test_calculator.py
import pytest
from calculator import add


def test_add_normal():
    """正常情况：两个正整数相加"""
    assert add(2, 3) == 5


def test_add_boundary():
    """边界情况：0、负数、浮点数"""
    assert add(0, 0) == 0
    assert add(-5, 3) == -2
    assert add(1.2, 2.8) == 4.0
    assert add(1.2, 2.8) == 4.0


def test_add_exception():
    """异常情况：传入不支持的类型（如字符串）应抛出 TypeError"""
    with pytest.raises(TypeError):
        add("hello", 2)
