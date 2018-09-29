import unittest
import os
import HTMLTestRunner

def all_case():
    case_path=os.getcwd()#"E:\\python\\PyCharm 2017.3.4\\unit_test\\testaaa"
    discover=unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
    return discover

report_path="E:\\A\\B\\C\\hhh.html"
f=open(report_path,"wb")
runner=HTMLTestRunner.HTMLTestRunner(stream=f,title="测试一下！",description="结果就是这样")
runner.run(all_case())
f.close()
