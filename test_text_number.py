import pytest
from selenium.webdriver.common.by import By
from seleniumwire import webdriver  # Import from seleniumwire
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#Переменные
co2_element = ""
water_element = ""
energy_element = ""

#Функция открытия браузера, перехода на страницу тестирования и подмены параметров
def running_tests(args):
    global co2_element
    global water_element
    global energy_element
    co2 = args[0]
    water = args[1]
    energy = args[2]
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    def interceptor(request):
        if request.url == 'https://www.avito.ru/web/1/charity/ecoImpact/init':
            request.create_response(
                status_code=200,
                headers={'Content-Type': 'application/json'},  # Optional headers dictionary
                body='{"result": {"blocks": {"personalImpact": {"avatarUrl": "https://30.img.avito.st/image/1/1.Ur5lira26FdTLXxRTasfs8kp_l3bqfjV1yn8.GfM3Tvdu-ZqXKZ14aDfya5FCvBE86e6Pm7wTD9V_q2w","data": {"co2": ' + str(
                    co2) + ',"energy": ' + str(energy) + ',"materials": 0,"pineYears": 0,"water": ' + str(
                    water) + '}}},"isAuthorized": true}, "status": "ok"}'
            )
        if request.url == 'https://avito.st/s/charity/eco-impact/video/water.mp4':
            request.create_response(
                status_code=404,
            )
        if request.url == 'https://avito.st/s/charity/eco-impact/video/co2.mp4':
            request.create_response(
                status_code=404,
            )
        if request.url == 'https://avito.st/s/charity/eco-impact/video/energy3.mp4':
            request.create_response(
                status_code=404,
            )

    driver.request_interceptor = interceptor

    base_url = 'https://www.avito.ru/avito-care/eco-impact'
    driver.get(base_url)
    driver.maximize_window()

    co2_element = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[2]')
    water_element = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[4]')
    energy_element = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[6]')

#Тест-кейсы текстовых значений (числовых)
data_tests = ["5", "5", "5"]
running_tests(data_tests)


def test_co2_text_number():
    global count_tests
    co2_element.screenshot('./output/28.png')
    assert 1 == 1


def test_water_text_number():
    global count_tests
    water_element.screenshot('./output/29.png')
    assert 1 == 1


def test_energy_text_number():
    global count_tests
    energy_element.screenshot('./output/30.png')
    assert 1 == 1




