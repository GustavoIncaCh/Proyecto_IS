# Automatically generated by Pynguin.
import caso_covertura_005 as module0


def test_case_0():
    var0 = '#o>(P)\t *sWKoEn(}x'
    var1 = 'nI1-'
    var2 = module0.search(var0, var1)
    assert var2 == 0


def test_case_1():
    var0 = "v'o c\x0cPO)=9V\tea"
    var1 = '\n[|,B;j+7r2KV"v/5E7g'
    var2 = module0.search(var0, var1)
    assert var2 == 20


def test_case_2():
    var0 = "v'o c\x0cPO)=9V\tea"
    var1 = '\n[|,B;j+7r2KV"v/5E7g'
    var2 = module0.search(var0, var1)
    assert var2 == 20
    var3 = '#o>(P)\t *sWKoEn(}x'
    var4 = 'nI1-'
    var5 = module0.search(var3, var4)
    assert var5 == 0
    var6 = module0.search(var4, var4)
    assert var6 == 4


def test_case_3():
    var0 = 2972
    var1 = ''
    var2 = module0.search(var0, var1)
    assert var2 == 0
