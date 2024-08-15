from selenium.webdriver.common.by import By


class Locators:
    #
    Reg_Name = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input")  # Поле Имя
    Reg_Password = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input")  # Поле Пароль
    Reg_Email = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")  # Поле Email
    # Кнопки
    Reg_button = (By.XPATH, "//button[text() = 'Зарегистрироваться']")  # Регистрация
    Entry_button = (By.XPATH, "//button[text() = 'Войти']")  # Вход
    Order_button = (By.XPATH, "//button[text() = 'Оформить заказ']")  # Оформление заказа
    Profile_button = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # Переход в личный кабинет
    Constructor_button = (By.XPATH, "//p[text() = 'Конструктор']")  # Переход в конструктор
    Logout_button = (By.XPATH, "//button[text() = 'Выход']")  # Выход
    Buns_button = (By.XPATH, "//span[text() = 'Булки']/parent::div")  # Переход к булкам
    Sauces_button = (By.XPATH, "//span[text() = 'Соусы']")  # Переход к соусам
    Toppings_button = (By.XPATH, "//span[text() = 'Начинки']")  # Переход к начинкам
    # Ингридиенты
    Buns = (By.XPATH, "//h2[text() = 'Булки']")  # Булки
    Sauces = (By.XPATH, "//h2[text() = 'Соусы']")  # Соуса
    Toppings = (By.XPATH, "//h2[text() = 'Начинки']")  # Начинки

    Order_history = (By.XPATH, "//a[text() = 'История заказов']")  # История Заказов
    Wrong_password_info = (By.XPATH, "//p[text() = 'Некорректный пароль']")  # Забыли пароль
    Entrance = (By.XPATH, "//h2[text() = 'Вход']")  # Вход
    Main_logo = (By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2']")  # Логотип
    Entrance_from_main = (By.XPATH, "//button[text() = 'Войти в аккаунт']")  # Войти в аккаунт
    Entrance_from_profile = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # Личный кабинет
    Entrance_from_reg = (By.XPATH, "//a[text() = 'Войти']")   # Войти
    Lost_Password = (By.XPATH, "//a[text() = 'Восстановить пароль']")  # Восстановить пароль
    Entrance_from_lost_password = (By.XPATH, "//a[text() = 'Войти']")  # Вспомнили пароль
