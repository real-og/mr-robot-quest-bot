from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


trapped_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
btn_tr_1 = KeyboardButton('Подвинуть бочку')
btn_tr_2 = KeyboardButton('Сесть рядом с другом')
trapped_kb.add(btn_tr_1, btn_tr_2)

barrel_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
btn_br_1 = KeyboardButton('Войти в туннель')
btn_br_2 = KeyboardButton('мок')
barrel_kb.add(btn_br_1, btn_br_2)

friend_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
btn_fr_1 = KeyboardButton('Прочесть записку')
btn_fr_2 = KeyboardButton('Зажечь спичку')
friend_kb.add(btn_fr_1, btn_fr_2)

note_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
btn_nt_1 = KeyboardButton('Уйти')
btn_nt_2 = KeyboardButton('мок')
note_kb.add(btn_nt_1, btn_nt_2)

beach_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
btn_bc_1 = KeyboardButton('Изучить')
btn_bc_2 = KeyboardButton('мок')
beach_kb.add(btn_bc_1, btn_bc_2)

boat_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
btn_bt_1 = KeyboardButton('Взайти на судно')
btn_bt_2 = KeyboardButton('мок')
boat_kb.add(btn_bt_1, btn_bt_2)

congrats_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
btn_cg_1 = KeyboardButton('Да')
btn_cg_2 = KeyboardButton('мок')
congrats_kb.add(btn_cg_1, btn_cg_2)

light_note_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
btn_ln_1 = KeyboardButton('Остаться')
btn_ln_2 = KeyboardButton('Уйти')
light_note_kb.add(btn_ln_1, btn_ln_2)
