# Automatically generated by Pynguin.
import pytest
import src.clock_display as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    set_0 = set()
    clock_display_0 = module_0.ClockDisplay(set_0)
    var_0 = clock_display_0.clone()
    var_1 = clock_display_0.clone()
    var_2 = var_1.clone()
    var_3 = var_1.clone()
    var_4 = clock_display_0.str()
    var_5 = clock_display_0.increment()
    var_5.invariant()


def test_case_1():
    bytes_0 = b"\xe2\x8dn4\xc7n\x8ag\xd9=\xael\x02"
    clock_display_0 = module_0.ClockDisplay(bytes_0)
    var_0 = clock_display_0.increment()
    var_1 = clock_display_0.increment()
    var_2 = clock_display_0.invariant()
    var_3 = clock_display_0.str()
    assert var_3 == "00:00:00:00:00:00:00:00:00:00:00:01:00"


@pytest.mark.xfail(strict=True)
def test_case_2():
    dict_0 = {}
    clock_display_0 = module_0.ClockDisplay(dict_0)
    var_0 = clock_display_0.invariant()
    var_0.increment()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -1107
    module_0.ClockDisplay(int_0)


def test_case_4():
    bytes_0 = b"\xe2\x8dn4\xc7n\x8ag\xd9=\xael\x02"
    clock_display_0 = module_0.ClockDisplay(bytes_0)
    var_0 = clock_display_0.increment()
    var_1 = clock_display_0.increment()


def test_case_5():
    bytes_0 = b"\xe2\x8dn4\xc7n\x8ag\xd9=\xael\x02"
    clock_display_0 = module_0.ClockDisplay(bytes_0)
    var_0 = clock_display_0.increment()
    var_1 = clock_display_0.clone()
    var_2 = var_1.increment()
    var_3 = var_1.str()
    assert var_3 == "00:00:00:00:00:00:00:00:00:00:00:01:00"


def test_case_6():
    bytes_0 = b"\xe2\x8dn4\xc7n\x8ag\xd9=\xael\x02"
    clock_display_0 = module_0.ClockDisplay(bytes_0)
    var_0 = clock_display_0.increment()
    var_1 = clock_display_0.clone()
    var_2 = var_1.increment()


@pytest.mark.xfail(strict=True)
def test_case_7():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    clock_display_0 = module_0.ClockDisplay(dict_0)
    clock_display_1 = clock_display_0.clone()
    var_0 = clock_display_0.increment()
    module_0.ClockDisplay(clock_display_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    clock_display_0 = module_0.ClockDisplay(list_0)
    clock_display_1 = module_0.ClockDisplay(list_0)
    var_0 = clock_display_1.clone()
    var_1 = var_0.increment()
    var_1.clone()
