#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from led.led import main, get_response, parse_args
import sys

__author__ = "Peng Ye"
__copyright__ = "Peng Ye"
__license__ = "GPL3"


def test_get_response_001():
    # assertion_001:
    #	verify if the return value is None if input the
    #   correct filename or wrong url address
    assert get_response('worth_path_name') == None

def test_get_response_002(capsys):
    # assertion_002:
    #   Verify if the the output has expected information
    #   if input the correct filename or wrong url address
    get_response('worth_path_name')
    out,err = capsys.readouterr()
    assert "No such file or directory" in out

def test_main_003(capsys):
    # assertion_003:
    #   Verify when 'turn on' the light from (120,120) to
    #   (129,129), there will be 100 lights be turned on
    sys.argv = [" ", "--input", "./../data/input_test_003.txt"]
    main()
    out,err = capsys.readouterr()
    assert "100" in out

def test_main_004(capsys):
    # assertion_004:
    #   Verify when 'turn on' the light from (120,120) to
    #   (129,129), and 'turn off' the light from (110,110) to (120,120),
    #   then there will be 99 lights turning on
    sys.argv = [" ", "--input", "./../data/input_test_004.txt"]
    main()
    out,err = capsys.readouterr()
    assert "99" in out

def test_main_005(capsys):
    # assertion_005:
    #   Verify when 'switch' the light from (120,120) to
    #   (123,123), and 'switch' the light from (121,121) to (122,122),
    #   then there will be 12 lights turning on
    sys.argv = [" ", "--input", "./../data/input_test_005.txt"]
    main()
    out,err = capsys.readouterr()
    assert "12" in out

def test_main_006(capsys):
    # assertion_006:
    #   Verify incorrect keywords of handling on the light will do nothing
    #   but the program will not raise the error
    sys.argv = [" ", "--input", "./../data/input_test_006.txt"]
    main()
    out,err = capsys.readouterr()
    assert "0" in out
    assert err == ''

def test_main_007(capsys):
    # assertion_007:
    #   Verify when 'turn on' the light from (-1,-1) to
    #   (1,1), and 'turn on' the light from (999,999) to (1000,1000),
    #   then there will be 5 lights turning on, in which the outside
    #   of the grid will not be affected and there will NOT be Error message
    #   raised
    sys.argv = [" ", "--input", "./../data/input_test_007.txt"]
    main()
    out,err = capsys.readouterr()
    assert "5" in out
    assert err == ''

def test_parse_args_008(capsys):
    # assertion_008:
    # 	Verify passing parameters with "--input" and string could
    #   return the string successfully
    args = parse_args(["--input", "url or filename"])
    out,err = capsys.readouterr()
    assert args.input == 'url or filename'
    assert out == ''

def test_parse_args_009(capsys):
    # assertion_009:
    # 	Verify passing parameters with "--opt" and string could
    #   NOT return the string successfully
    with pytest.raises(SystemExit):
        args = parse_args(["--opt", "url or filename"])
    out,err = capsys.readouterr()
    assert 'unrecognized arguments' in err
