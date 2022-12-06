from django.db import models


class FactoryChoice(models.TextChoices):
    ABK = 'ABK', 'АБК бетон'
    AKSY = 'AKSY', 'Аксу бетон'
    ALIANC = 'ALIANC', 'Альянс бетон'
    ALCAS = 'ALCAS', 'Алкас бетон'
    AKZHAR = 'AKZHAR', 'Акжар бетон'
    ALIANC_ASTANA = 'ALIANC_ASTANA', 'Альянс(Астана) бетон'
    BARAKAT = 'BARAKAT', 'Баракат бетон'
    BURUNDAI = 'BURUNDAI', 'Бурундай бетон'
    FAST_PROMO = 'FAST_PROMO', 'Фаст(Промо-С) бетон'
    FAST_KONKRIT = 'FAST_KONKRIT', 'Фаст(Конкрит) бетон'
    FAST_MELIOR = 'FAST_MELIOR', 'Фаст(Мелиор Логистик) бетон'
    FARHAT = 'FARHAT', 'Фархат Инженеринг бетон'
    KAZ = 'KAZ', 'Каз бетон'
    RBY = 'RBY', 'Рбу бетон'
    SALTANAT = 'SALTANAT', 'Салтанат бетон'
    SITI_LAIT = 'SITI_LAIT', 'Сити Лайт бетон'
    TAY = 'TAY', 'Тау бетон'
    TAYEKEL = 'TAYEKEL', 'Тауекел бетон'
    TASKILEM = 'TASKILEM', 'Таскилем бетон'
    TEMIR = 'TEMIR', 'Темир бетон'
    TSZH = 'TSZH', 'ТСЖ бетон'
    VOSTOK = 'VOSTOK', 'Восток бетон'
    ZHSN = 'ZHSN', 'ЖСН бетон'


class MarkConcreteChoice(models.TextChoices):
    M100 = 'М100', 'М100'
    M200 = 'М200', 'М200'
    M200_SUHOI = 'М200 suhoi', 'М200 сухой'
    M300 = 'М300', 'М300'
    M350 = 'М350', 'М350'
    M400 = 'М400', 'М400'


class ConstructiveChoice(models.TextChoices):
    PB = 'podbetonka', 'Подбетонка'
    FM = 'fundament', 'Фундамент'
    STM = 'stena', 'Стена Монолитная '
    PP = 'pp', 'Плита перекрытия'
    LSH = 'lsh', 'Лифтовая Шахта'
    LM = 'lm', 'Лестничный марш'
    PM = 'priyamok', 'Приямок'
    PA = 'parapet', 'Парапет'


class CustomUserRoleChoice(models.TextChoices):
    ADMIN = 'admin', 'Админ'
    DEPARTMENT_SUPPLY = 'otdel_snabjenie', 'Отдел Снабжение'
    DEPATRMENT_PTO = 'otdel_pto', 'Отдел ПТО'
    DEPATRMENT_LANDSCAPING = 'otdel_blagoustroistvo', 'Отдел Благоустройство'
    SECTION_MANAGER = 'Nach_ustka', 'Начальник Участка'
    FOREMAN = 'Prorab', 'Прораб'


class ObjectNameChoice(models.TextChoices):
    TEREMKI = 'Teremki', 'Теремки'
    TERRACOTA = 'Terracota', 'Терракота'
    KRISTAL = 'Kristal', 'Кристал'
    TOLEBI_1 = 'Tole bi 1', 'Толе би 1'
    TOLEBI_2 = 'Tole bi 2', 'Толе би 2'
    TOLEBI_3 = 'Tole bi 3', 'Толе би 3'
