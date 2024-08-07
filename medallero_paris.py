from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configura las opciones del navegador
chrome_options = Options()
chrome_options.add_argument("--headless")  # Opcional: Ejecuta en modo headless (sin interfaz gráfica)

# Ruta al ejecutable de ChromeDriver
service = Service('C:\\ruta\\a\\tu\\chromedriver.exe')  # Cambia esto a la ruta de tu ChromeDriver

# Crea una instancia del navegador
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # URL principal
    url_main = 'https://www.clarosports.com/en-vivo/'
    driver.get(url_main)

    # Espera a que la página cargue y encuentra el enlace al evento de pista y campo
    wait = WebDriverWait(driver, 10)
    event_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Pista y campo')))

    # Haz clic en el enlace para acceder a la página del evento
    event_link.click()

    # Espera a que la página del evento cargue
    wait.until(EC.title_contains('Pista y campo'))  # Puedes ajustar esto según el título de la página del evento

    # Imprime el título de la página para verificar
    print(f'Título de la página: {driver.title}')

    # Accede directamente a la URL del evento
    url_event = 'https://www.clarosports.com/olimpicos/paris-2024/eventos/ath/pista-y-campo-129922ba/'
    driver.get(url_event)

    # Espera a que la página del evento cargue y extrae información según sea necesario
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'selector-del-elemento')))  # Ajusta el selector según el contenido de la página

    # Imprime la URL actual para verificar
    print(f'URL actual: {driver.current_url}')

finally:
    # Cierra el navegador
    driver.quit()