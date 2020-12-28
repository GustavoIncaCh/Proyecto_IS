import unittest
import pytest
import caso_covertura_010 as module0


class PruebasFunciones(unittest.TestCase):
    def test_case_0(self):
        var0 = '3AXl=cxV4w'
        var1 = module0.search(var0, var0)
        assert var1 == 1


    def test_case_1(self):
        var0 = '3AXl=cxV4w'
        var1 = module0.search(var0, var0)
        assert var1 == 1
        var2 = 'l`$GH"F_>zG|#M`'
        var3 = 'K'
        var4 = module0.search(var2, var3)
        assert var4 == 1


    def test_case_2(self):
        var0 = '=*'
        var1 = '|Y$I'
        var2 = module0.search(var0, var1)
        assert var2 == 0


    def test_case_3(self):
        var0 = '3AXl=cxV4w'
        var1 = module0.search(var0, var0)
        assert var1 == 1
        var2 = 'j$cm:"|3Ezi;Egn'
        var3 = 'lB>=nYZ'
        var4 = module0.search(var2, var3)
        assert var4 == 0


    def test_case_4(self):
        var0 = '3AXl=cxV4w'
        var1 = module0.search(var0, var0)
        assert var1 == 1
        var2 = 'j$cm:"|3Ezi;Egn'
        var3 = 'lB>=nYZ'
        var4 = module0.search(var2, var3)
        assert var4 == 0
        var5 = '3AXl=cxV4w'
        var6 = module0.search(var5, var5)
        assert var6 == 1
        var7 = 'l`$GH"F_>zG|#M`'
        var8 = 'K'
        var9 = module0.search(var7, var8)
        assert var9 == 1
        var10 = '/ZqaEqayVJ'
        var11 = module0.search(var10, var10)
        assert var11 == 1


    def test_case_5(self):
        var0 = '3AXl=cxV4w'
        var1 = module0.search(var0, var0)
        assert var1 == 1
        var2 = 'AUl^K\nv\\_['
        var3 = 'JXKN'
        var4 = module0.search(var2, var3)
        assert var4 == 0


    def test_case_6(self):
        var0 = '3AXl=cxV4w'
        var1 = module0.search(var0, var0)
        assert var1 == 1
        var2 = 'j$cm:"|3Ezi;Egn'
        var3 = 'lB>=nYZ'
        var4 = module0.search(var2, var3)
        assert var4 == 0
        var5 = '3AXl=cxV4w'
        var6 = module0.search(var5, var5)
        assert var6 == 1
        var7 = 'AUl^K\nv\\_['
        var8 = 'JXKN'
        var9 = module0.search(var7, var8)
        assert var9 == 0
        var10 = '=*'
        var11 = '|Y$I'
        var12 = module0.search(var10, var11)
        assert var12 == 0
        var13 = '3AXl=cxV4w'
        var14 = module0.search(var13, var13)
        assert var14 == 1
        var15 = module0.search(var7, var2)
        assert var15 == 0


    def test_case_7(self):
        var0 = '3AXl=cxV4w'
        var1 = module0.search(var0, var0)
        assert var1 == 1
        var2 = 'l`$GH"F_>zG|#M`'
        var3 = 'K'
        var4 = module0.search(var2, var3)
        assert var4 == 1
        var5 = '3AXl=cxV4w'
        var6 = module0.search(var5, var5)
        assert var6 == 1
        var7 = 'AUl^K\nv\\_['
        var8 = 'JXKN'
        var9 = module0.search(var7, var8)
        assert var9 == 0
        var10 = '=*'
        var11 = '|Y$I'
        var12 = module0.search(var10, var11)
        assert var12 == 0
        var13 = '3AXl=cxV4w'
        var14 = module0.search(var13, var13)
        assert var14 == 1
        var15 = 'j$cm:"|3Ezi;Egn'
        var16 = 'lB>=nYZ'
        var17 = module0.search(var15, var16)
        assert var17 == 0
        var18 = '(z/\t"FnL5g\rF;'
        var19 = module0.search(var15, var18)
        assert var19 == 1


    def test_case_8(self):
        var0 = '=*'
        var1 = '|Y$I'
        var2 = module0.search(var0, var1)
        assert var2 == 0
        var3 = '\\A`I5b'
        var4 = '\x0c[Q<Y&.SA3vw'
        var5 = module0.search(var3, var4)
        assert var5 == 10


    def test_case_9(self):
        var0 = '=*'
        var1 = '|Y$I'
        var2 = module0.search(var0, var1)
        assert var2 == 0
        var3 = '\\A`I5b'
        var4 = '\x0c[Q<Y&.SA3vw'
        var5 = module0.search(var3, var4)
        assert var5 == 10
        var6 = '3AXl=cxV4w'
        var7 = module0.search(var6, var6)
        assert var7 == 1
        var8 = '3AXl=cxV4w'
        var9 = module0.search(var8, var8)
        assert var9 == 1
        var10 = 'l`$GH"F_>zG|#M`'
        var11 = 'K'
        var12 = module0.search(var10, var11)
        assert var12 == 1
        var13 = ':}J`>5 GTZ'
        var14 = 'iHK6QXd/50U/1"\x0b0i[`^'
        var15 = module0.search(var13, var14)
        assert var15 == 0


    def test_case_10(self):
        var0 = '"x\'BHi]yi2'
        var1 = "RI\\<\x0b$W!T'"
        var2 = module0.search(var0, var1)
        assert var2 == 0


    def test_case_11(self):
        var0 = '"x\'BHi]yi2'
        var1 = "RI\\<\x0b$W!T'"
        var2 = module0.search(var0, var1)
        assert var2 == 0
        var3 = '3AXl=cxV4w'
        var4 = module0.search(var3, var3)
        assert var4 == 1
        var5 = 'l`$GH"F_>zG|#M`'
        var6 = 'K'
        var7 = module0.search(var5, var6)
        assert var7 == 1
        var8 = '3AXl=cxV4w'
        var9 = module0.search(var8, var8)
        assert var9 == 1
        var10 = 'j$cm:"|3Ezi;Egn'
        var11 = 'lB>=nYZ'
        var12 = module0.search(var10, var11)
        assert var12 == 0
        var13 = '=*'
        var14 = '|Y$I'
        var15 = module0.search(var13, var14)
        assert var15 == 0
        var16 = '3AXl=cxV4w'
        var17 = module0.search(var16, var16)
        assert var17 == 1
        var18 = '3AXl=cxV4w'
        var19 = module0.search(var18, var18)
        assert var19 == 1
        var20 = 'AUl^K\nv\\_['
        var21 = 'JXKN'
        var22 = module0.search(var20, var21)
        assert var22 == 0
        var23 = '=*'
        var24 = '|Y$I'
        var25 = module0.search(var23, var24)
        assert var25 == 0
        var26 = '\\A`I5b'
        var27 = '\x0c[Q<Y&.SA3vw'
        var28 = module0.search(var26, var27)
        assert var28 == 10
        var29 = False
        var30 = ''
        var31 = module0.search(var29, var30)
        assert var31 == 0

if __name__ == '__main__':
    unittest.main()
