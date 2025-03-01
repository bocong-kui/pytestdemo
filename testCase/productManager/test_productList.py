import allure
import pytest
from pytestdemo.common.readyaml import get_testcase_yaml
from pytestdemo.base.apiutil import BaseRequests



@allure.feature('获取商品列表')
class TestLogin:
    @allure.story('获取商品列表')
    @pytest.mark.parametrize('params',get_testcase_yaml('./testCase/productManager/getProductList.yaml'))
    def test_get_product_list(self,params):
        BaseRequests().specification_yaml(params)

    @allure.story('获取商品详情信息')
    @pytest.mark.parametrize('params', get_testcase_yaml('./testCase/productManager/productDetail.yaml'))
    def test_get_product_detail(self, params):
        print(params)
        BaseRequests().specification_yaml(params)