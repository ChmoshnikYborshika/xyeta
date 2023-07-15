# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene prosto

    show eline_smile

    e "Хули палишь уёба?"
    
    e "Бля, уёбывай давай. Тут нет нихуя интресного. Ты вообще чё тут увидеть то хочешь? ебейшие плоды моих усилий?"

    e "Не смеши..."

    e "ну ладно"

label what:

    scene street_night

    show eline_smile

    e "Ладно, сюжета тут пока что не жди особо. Я просто буду пытаться вспомниты всё что там насмотрел"

    menu:
        "Что делать?"

        "Продолжать смотреть на не интересную хуету":

            jump dalee

        "Забить хуй, потому что блядь не интересно":

            jump poxyi

label dalee:

    "Хмм, тебе и правда интересно..."

    jump itogo

label poxyi:

    e "Ну и иди нахуй("



label itogo:

    scene room_night

    show eline_smile

    e "Уютненькая комнатка, да?"
    menu:
        "Как тебе"

        "Да":
            jump ebatsa

        "Нет":
            jump ladno

label ebatsa:

    scene room_night

    show eline_ydivlena

    e "Может тогда поебёмся?))"
    menu:
        "?"

        "Окс":
            jump da

label ladno:

    scene room_night

    show eline_pain

    e "Ну ладно("
    e "Чем тогда займёмся?"
    menu:
        "?"

        "Поебёмся!":
            jump da 


label da:

    scene room_night

    show eline_smile

    e "Зоебис"

    return

