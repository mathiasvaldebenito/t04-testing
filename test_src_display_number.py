# Automatically generated by Pynguin.
import pytest
import src.display_number as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    number_display_0 = module_0.NumberDisplay(bool_0, bool_0)
    var_0 = number_display_0.clone()
    var_1 = var_0.invariant()
    assert var_1 is False
    var_2 = number_display_0.str()
    assert var_2 == "0True"
    var_1.increase()


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    number_display_0 = module_0.NumberDisplay(none_type_0, none_type_0)
    number_display_0.increase()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -355
    number_display_0 = module_0.NumberDisplay(int_0, int_0)
    var_0 = number_display_0.reset()
    assert number_display_0.value == 0
    var_0.increase()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1068
    number_display_0 = module_0.NumberDisplay(int_0, int_0)
    var_0 = number_display_0.invariant()
    assert var_0 is False
    var_0.reset()


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = -5390
    bool_0 = True
    number_display_0 = module_0.NumberDisplay(int_0, bool_0)
    var_0 = number_display_0.clone()
    var_1 = var_0.invariant()
    assert var_1 is True
    var_1.clone()


@pytest.mark.xfail(strict=True)
def test_case_5():
    float_0 = 108.8316
    number_display_0 = module_0.NumberDisplay(float_0, float_0)
    var_0 = number_display_0.clone()
    var_1 = var_0.clone()
    var_2 = var_1.reset()
    assert var_1.value == 0
    var_3 = var_0.str()
    assert var_3 == "108.8316"
    var_3.clone()
