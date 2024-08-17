from selenium.webdriver.common.by import By


class Locators:
    #
    REG_NAME = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input")  # Поле Имя
    REG_PASSWORD = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input")  # Поле Пароль
    REG_EMAIL = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")  # Поле Email
    # Кнопки
    REG_BUTTON = (By.XPATH, "//button[text() = 'Зарегистрироваться']")  # Регистрация
    ENTRY_BUTTON = (By.XPATH, "//button[text() = 'Войти']")  # Вход
    ORDER_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']")  # Оформление заказа
    PROFILE_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # Переход в личный кабинет
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']")  # Переход в конструктор
    LOGOUT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")  # Выход
    BUNS_BUTTON = (By.XPATH, "//span[text() = 'Булки']/parent::div")  # Переход к булкам
    SAUCES_BUTTON = (By.XPATH, "//span[text() = 'Соусы']")  # Переход к соусам
    TOPPINGS_BUTTON = (By.XPATH, "//span[text() = 'Начинки']")  # Переход к начинкам
    # Ингридиенты
    BUNS = (By.XPATH, "//h2[text() = 'Булки']")  # Булки
    SAUCES = (By.XPATH, "//h2[text() = 'Соусы']")  # Соуса
    TOPPINGS = (By.XPATH, "//h2[text() = 'Начинки']")  # Начинки

    ORDER_HISTORY = (By.XPATH, "//a[text() = 'История заказов']")  # История Заказов
    WRONG_PASSWORD_INFO = (By.XPATH, "//p[text() = 'Некорректный пароль']")  # Забыли пароль
    ENTRANCE = (By.XPATH, "//h2[text() = 'Вход']")  # Вход
    # MAIN_LOGO = (By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2']")
    MAIN_LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")  # Логотип
    ENTRANCE_FROM_MAIN = (By.XPATH, "//button[text() = 'Войти в аккаунт']")  # Войти в аккаунт
    ENTRANCE_FROM_PROFILE = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # Личный кабинет
    ENTRANCE_FROM_REG = (By.XPATH, "//a[text() = 'Войти']")   # Войти
    LOST_PASSWORD = (By.XPATH, "//a[text() = 'Восстановить пароль']")  # Восстановить пароль
    ENTRANCE_FROM_LOST_PASSWORD = (By.XPATH, "//a[text() = 'Войти']")  # Вспомнили пароль

