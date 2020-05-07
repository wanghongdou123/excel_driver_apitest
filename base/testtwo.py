import unittest
from base.apidemotest import RunMain
from base import HTMLTestRunner
import mock
from base.mock_demo import mock_test


class testtwo(unittest.TestCase):

    def setUp(self):
        self.run = RunMain()
        print('setup')

    def tearDown(self):
        print('tearDown')

    # # @unittest.skip('no')
    # def test_01(self):
    #     url = 'http://127.0.0.1:10086/'
    #     print(url)
    #     res = self.run.run_main(url=url,method='GET')
    #     print(res)
    #     self.assertEqual(res[1],200,"测试失败")


    def test_02(self):

        url = 'http://127.0.0.1:10086/add/'
        print(url)
        json = {
            "username": "admin",
            "password": "admin",
            "code":200
        }
        headers = {
            "content-type": "application/json"
        }

        # self.run.run_main = mock.Mock(return_value=json)
        res = mock_test(self.run.run_main,json,url,'POST',json)

        # res = self.run.run_main(url=url,method='POST',json=json,headers=headers)
        # print(res)
        self.assertEqual(res['code'], 200, "测试失败")


if __name__ == '__main__':
    # file_path = '../report/htmlreport.html'
    # fp = open(file_path,'wb')
    unittest.main()
    # suit = unittest.TestSuite()
    # suit.addTest(testtwo('test_02'))
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is first report')
    # runner.run(suit)
    # fp.close()

