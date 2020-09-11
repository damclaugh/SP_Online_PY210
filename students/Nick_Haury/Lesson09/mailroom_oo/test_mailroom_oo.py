#!/usr/bin/env python3
import pytest
import donor_models as dm
import cli_main as cm

'''
Test for the object oriented version of the mailroom program.
'''

d1 = dm.Donor("Dude1")
d2 = dm.Donor("Dude2", [100.00])
d3 = dm.Donor("Dude3", [100.00, 200.00])
dc = dm.DonorCollection({
    d1.name:d1,
    d2.name:d2,
    d3.name:d3
})

def test_create_donor():
    assert d1.name == "Dude1"
    assert d1.donations == []
    assert d2.donations == [100.00]
    assert d3.donations == [100.00, 200.00]

def test_add_donation():
    with pytest.raises(TypeError):
        d1.add_donation("hello")
    with pytest.raises(ValueError):
        d1.add_donation(-200)
    d1.add_donation(10)
    d1.add_donation(20.0)
    assert d1.donations == [10, 20.0]

def test_donorcollection():
    with pytest.raises(TypeError):
        dm.DonorCollection("invalid")
    assert dc.get_names() == [d1.name, d2.name, d3.name]
    assert dc.donors[d1.name] == d1
    with pytest.raises(TypeError):
        dc.add_donor("not a Donor")
    d4 = dm.Donor("Dude4")
    dc.add_donor(d4)
    assert d4.name in dc.get_names()
    