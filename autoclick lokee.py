from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Spécifiez le chemin vers le pilote OperaGX téléchargé
driver_path = 'C:/Users/Gabriel/Downloads/operadriver_win32/operadriver_win32/operadriver.exe'  # Mettez à jour le chemin selon votre configuration
driver = webdriver.Opera(executable_path=driver_path)

# Ouvrir la page web
url = 'https://lockee.fr/o/aiMX3A73'  # Mettez à jour l'URL de la page web
driver.get(url)

# Attendre que l'élément soit présent (ajoutez des délais selon les besoins)
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="your_element_id"]'))
)

# Suite de nombres à cliquer
suite_de_nombres = "1234567890"  # Mettez à jour avec votre suite de nombres

# Boucle pour cliquer sur chaque bouton numérique
for chiffre in suite_de_nombres:
    # Construire l'expression XPath pour le bouton numérique
    xpath_expression = f'//button[text()="{chiffre}"]'

    # Localiser le bouton numérique par XPath
    bouton_numerique = driver.find_element(By.XPATH, xpath_expression)

    # Cliquer sur le bouton numérique
    bouton_numerique.click()

# Fermer le navigateur à la fin
driver.quit()
