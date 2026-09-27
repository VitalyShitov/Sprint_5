from selenium.webdriver.common.by import By

class Locators:
    HEADER_CONSTRUCTOR = (
        By.XPATH,
        '//p[text()="Конструктор"]/parent::a'
    )  # Кнопка «Конструктор» в шапке — ведёт на главную (конструктор)

    HEADER_PERSONAL_CABINET = (
        By.XPATH,
        '//p[text()="Личный Кабинет"]/parent::a'
    )  # Кнопка «Личный кабинет» в шапке

    LOGO = (
        By.XPATH,
        '//div[contains(@class,"AppHeader_header__logo")]'
    )  # Логотип Stellar Burgers — ссылка на главную

    LOGO_ALT = (
        By.XPATH,
        '//a[@href="/"]'
    ) # Альтернатива логотипа, если класс изменится: ссылка по href="/"


    LOGIN_BUTTON_MAIN = (
        By.XPATH,
        '//button[text()="Войти в аккаунт"]'
    )  # Кнопка «Войти в аккаунт» на главной

    ORDER_BUTTON = (
        By.XPATH,
        '//button[text()="Оформить заказ"]'
    )  # Кнопка «Оформить заказ» — маркер успешного входа

    TAB_BUNS = (
        By.XPATH,
        '//div[contains(@class,"tab_tab") and contains(.,"Булки")]'
    )  # Вкладка «Булки»

    TAB_SAUCES = (
        By.XPATH,
        '//div[contains(@class,"tab_tab") and contains(.,"Соусы")]'
    )  # Вкладка «Соусы»

    TAB_FILLINGS = (
        By.XPATH,
        '//div[contains(@class,"tab_tab") and contains(.,"Начинки")]'
    )  # Вкладка «Начинки»

    TAB_BUNS_CURRENT = (
        By.XPATH,
        '//div[contains(@class,"tab_tab_type_current") and contains(.,"Булки")]'
    )  # Активная вкладка «Булки» (подсвечена)

    TAB_SAUCES_CURRENT = (
        By.XPATH,
        '//div[contains(@class,"tab_tab_type_current") and contains(.,"Соусы")]'
    )  # Активная вкладка «Соусы»

    TAB_FILLINGS_CURRENT = (
        By.XPATH,
        '//div[contains(@class,"tab_tab_type_current") and contains(.,"Начинки")]'
    )  # Активная вкладка «Начинки»

    REG_NAME_INPUT = (
        By.XPATH,
        '//*[contains(text(),"Имя")]/parent::*/input'
    )  # Поле «Имя» в форме регистрации

    REG_EMAIL_INPUT = (
        By.XPATH,
        '//*[contains(text(),"Email")]/parent::*/input'
    )  # Поле «Email» в форме регистрации

    REG_PASSWORD_INPUT = (
        By.XPATH,
        '//*[contains(text(),"Пароль")]/parent::*/input'
    )  # Поле «Пароль» в форме регистрации

    REG_SUBMIT = (
        By.XPATH,
        '//button[text()="Зарегистрироваться"]'
    )  # Кнопка «Зарегистрироваться»

    REG_LOGIN_LINK = (
        By.XPATH,
        '//a[text()="Войти"]'
    )  # Ссылка «Войти» внутри формы регистрации

    PASSWORD_ERROR = (
        By.XPATH,
        '//*[contains(text(),"Пароль")]'
        '/ancestor::div[contains(@class,"input__container")]'
        '//p[contains(@class,"input__error")]'
    )  # Сообщение об ошибке валидации пароля («Некорректный пароль»)

    LOGIN_EMAIL_INPUT = (
        By.XPATH,
        '//*[contains(text(),"Email")]/parent::*/input'
    )  # Поле «Email» на странице входа

    LOGIN_PASSWORD_INPUT = (
        By.XPATH,
        '//*[contains(text(),"Пароль")]/parent::*/input'
    )  # Поле «Пароль» на странице входа

    LOGIN_SUBMIT = (
        By.XPATH,
        '//button[text()="Войти"]'
    )  # Кнопка «Войти» на странице входа

    LOGIN_REGISTER_LINK = (
        By.XPATH,
        '//a[text()="Зарегистрироваться"]'
    )  # Ссылка «Зарегистрироваться» на странице входа

    LOGIN_RESTORE_LINK = (
        By.XPATH,
        '//a[text()="Восстановить пароль"]'
    )  # Ссылка «Восстановить пароль» на странице входа

    RESTORE_EMAIL_INPUT = (
        By.XPATH,
        '//*[contains(text(),"Email")]/parent::*/input'
    )  # Поле «Email» для восстановления пароля

    RESTORE_SUBMIT = (
        By.XPATH,
        '//button[text()="Восстановить"]'
    )  # Кнопка «Восстановить»

    RESTORE_LOGIN_LINK = (
        By.XPATH,
        '//a[text()="Войти"]'
    )  # Ссылка «Войти» из формы восстановления

    PROFILE_FORM = (
        By.XPATH,
        '//div[contains(@class,"Profile_profileList_")]'
    )  # Форма профиля (список полей) — маркер страницы ЛК

    LOGOUT_BUTTON = (
        By.XPATH,
        '//button[text()="Выход"]'
    )  # Кнопка «Выход» в личном кабинете
