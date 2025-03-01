import pytest
import os

if __name__ == '__main__':
    # pytest.main(['./testCase','-sv','--reruns=2'])
    pytest.main()
    os.system('allure serve ./report/temp')

    # pytest.main(['-sv', '--alluredir=./allure_report/'])
    # os.system('allure serve ./allure_report')

    # os.system('allure generate ./allure_report/ -o ./report/ --clean')


    # pytest -sv ./pytestdemo -m "maoyan"