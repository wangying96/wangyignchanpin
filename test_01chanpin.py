from selenium import webdriver
import time
import unittest
from ddt import ddt,data,unpack
from HTMLTestRunnerNew import HTMLTestRunner
# from test_data.testExcel import DuExcel
# shuju=DuExcel()
# @ddt()
from log.deng_longin import DL
dl=DL()

class Test_dl(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        dl.Login()
    @classmethod
    def tearDownClass(self):
        dl.huohu.close()
        dl.huohu.quit()
    # @data(*shuju.du("Sheet2"))
    # @unpack
    #正用例
    def test_01xinzeng(self):
        try:
            dl.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            dl.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[1]/a").click()
            dl.huohu.find_element_by_name("pro_name").send_keys("糊糊士742")
            dl.huohu.find_element_by_name("cpbh").send_keys("N000018")
            dl.huohu.find_element_by_name("cptxm").send_keys("Pee76g9Hp284")
            dl.huohu.find_element_by_css_selector(".ke-edit-iframe").send_keys("ggg个头oo大pp，水分足")
            dl.huohu.find_element_by_css_selector(".btn.btn-danger").click()

            yuqi=dl.huohu.find_element_by_css_selector("#layui-layer1").text
            time.sleep(1)
            self.assertEqual(yuqi,"产品新增成功!",msg="成功")
            time.sleep(1)
        except Exception as e:
            print(e)
    #错误用例 产品编号重复
    def test_02xinzeng(self):
        try:
            dl.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            dl.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[1]/a").click()
            dl.huohu.find_element_by_name("pro_name").send_keys("陕西酥梨")
            dl.huohu.find_element_by_name("cpbh").send_keys("N00utyuy10")
            dl.huohu.find_element_by_name("cptxm").send_keys("HU7689Hutyuy3284")
            dl.huohu.find_element_by_css_selector(".ke-edit-iframe").send_keys("个头大，水分足")
            dl.huohu.find_element_by_css_selector(".btn.btn-danger").click()
            time.sleep(5)
            yuqi=dl.huohu.find_element_by_css_selector(".layui-layer-content").text
            time.sleep(1)
            self.assertEqual(yuqi,"产品编号有重复!",msg="编号重复")
            time.sleep(1)
        except Exception as e:
            print(e)
    #产品条码重复

    def test_03xinzeng(self):
        try:
            dl.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            dl.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[1]/a").click()
            dl.huohu.find_element_by_name("pro_name").send_keys("陕西蒲城酥梨")
            dl.huohu.find_element_by_name("cpbh").send_keys("N00112")
            dl.huohu.find_element_by_name("cptxm").send_keys("HU7689H3284")
            dl.huohu.find_element_by_css_selector(".ke-edit-iframe").send_keys("个头大，水分足")
            dl.huohu.find_element_by_css_selector(".btn.btn-danger").click()

            yuqi = dl.huohu.find_element_by_css_selector(".layui-layer-content").text
            time.sleep(1)
            self.assertEqual(yuqi, "产品条码有重复!", msg="条码有重复")
            time.sleep(1)
        except Exception as e:
            print(e)
    #修改正用例
    def test_004bianji(self):
        try:
            dl.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            dl.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()

            dl.huohu.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(9) > a:nth-child(1)").click()
            dl.huohu.find_element_by_name("pro_name").clear()
            dl.huohu.find_element_by_name("pro_name").send_keys("0oojm")
            dl.huohu.find_element_by_name("cpbh").send_keys("N00007998")
            dl.huohu.find_element_by_name("cptxm").send_keys("AAe76g9Hp284")
            dl.huohu.find_element_by_css_selector(".ke-edit-iframe").send_keys("bbb头oo大pp，水分足")
            dl.huohu.find_element_by_xpath("/html/body/section/section/section/div[2]/div/section/div/form/div[9]/div/button").click()

            yuqi = dl.huohu.find_element_by_xpath("//*[@id='layui-layer1']").text
            time.sleep(1)
            self.assertEqual(yuqi, "产品更新成功！", msg="修改成功")
            time.sleep(1)
        except Exception as e:
            print(e)
    #错误用例 产品名称没有填写
    def test_005bianji(self):
        try:
            dl.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            dl.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()

            dl.huohu.find_element_by_css_selector(
                ".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(9) > a:nth-child(1)").click()
            dl.huohu.find_element_by_name("pro_name").clear()
            dl.huohu.find_element_by_name("cpbh").send_keys("N000匹配07998")
            dl.huohu.find_element_by_name("cptxm").send_keys("AAe76g9gjhbp284")
            dl.huohu.find_element_by_css_selector(".ke-edit-iframe").send_keys("bbb头oo大pp，水分足")
            dl.huohu.find_element_by_xpath(
                "/html/body/section/section/section/div[2]/div/section/div/form/div[9]/div/button").click()

            yuqi = dl.huohu.find_element_by_xpath("//*[@id='layui-layer1']").text
            time.sleep(1)
            self.assertEqual(yuqi, "产品名称没有填写！", msg="断言成功")
            time.sleep(1)
        except Exception as e:
            print(e)
    def text_006shanchu(self):
        dl.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
        dl.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()
        dl.huohu.find_element_by_xpath("/html/body/section/section/section/form/div/div/section/table/tbody/tr[1]/td[8]/span").click()
        dl.huohu.find_element_by_xpath("/html/body/div[4]/div[3]/a[1]").click()
        yuqi=dl.huohu.find_element_by_xpath("//*[@id='layui-layer1']").text
        time.sleep(1)
        self.assertEqual(yuqi,"产品删除成功！",msg="删除成功")
        time.sleep(1)
    def text_007yulan(self):
        try:
            dl.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/a/span[1]").click()
            dl.huohu.find_element_by_xpath("/html/body/section/aside/div/ul/li[1]/ul/li[2]/a").click()
            dl.huohu.find_element_by_class_name("icon-eye-open").click()
            dl.huohu.find_element_by_xpath("/html/body/div[4]/span[1]/a").click()
            yuqi=dl.huohu.find_element_by_xpath("/html/body/div[4]/div[1]").text
            self.assertEqual(yuqi,"预览",msg="预览成功")
            time.sleep(1)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    # unittest.main()
    #实例化对象，创建测试集
    suite=unittest.TestSuite()
    suite.addTest(Test_dl("text_007yulan"))
    run=unittest.TextTestRunner()
    run.run(suite)





