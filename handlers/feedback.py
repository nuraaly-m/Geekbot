from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from config import database

feedback_router = Router()


class Feedback(StatesGroup):
    name = State()
    contact = State()
    date = State()
    food = State()
    cleanliness = State()
    comments = State()


@feedback_router.message(Command("stop"))
@feedback_router.message(F.text.lower() == "стоп")
async def stop(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Спасибо за прохождение опроса!")


@feedback_router.callback_query(F.data == 'feedback')
async def start_feedback(cb: types.CallbackQuery, state: FSMContext):
    await cb.answer()
    await state.set_state(Feedback.name)
    await cb.message.answer('как вас зовут?')


@feedback_router.message(Feedback.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Feedback.contact)
    await message.answer('ваш номер телефона:')


@feedback_router.message(Feedback.contact)
async def process_contact(message: types.Message, state: FSMContext):
    await state.update_data(contact=message.text)
    await state.set_state(Feedback.date)
    await message.answer('когда вы были у нас?')


@feedback_router.message(Feedback.date)
async def process_date(message: types.Message, state: FSMContext):
    date = message.text
    if not date.isdigit():
        await message.answer('вводите цифры')
        return
    await state.update_data(date=date)
    await state.set_state(Feedback.food)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='хорошее'),
                types.KeyboardButton(text='удовлетворительное'),
                types.KeyboardButton(text='плохое')
            ]
        ],
        resize_keyboard=True
    )
    await message.answer('какое было качество еды?', reply_markup=kb)


@feedback_router.message(Feedback.food)
async def process_food(message: types.Message, state: FSMContext):
    await state.update_data(food=message.text)
    await state.set_state(Feedback.cleanliness)
    await message.answer('как оцениваете чистоту заведения? (от 1 до 10)')


@feedback_router.message(Feedback.cleanliness)
async def process_cleanlines(message: types.Message, state: FSMContext):
    cleanliness = message.text
    if not cleanliness.isdigit():
        await message.answer('вводите цифру от 1 дот 10')
        return
    if int(cleanliness) < 1 or int(cleanliness) > 10:
        await message.answer('вводите цифру от 1 до 10')
        return
    await state.update_data(cleanliness=cleanliness)
    await state.set_state(Feedback.comments)
    data = await state.get_data()
    print('!', data)
    await message.answer('дополноительные комментарии:')


@feedback_router.message(Feedback.comments)
async def process_comments(message: types.Message, state: FSMContext):
    await state.update_data(comments=message.text)
    data = await state.get_data()
    print('~', data)
    await database.execute(
        "INSERT INTO feedback (name, contact, date, food, cleanliess, comments) VALUES (?, ?, ?, ?, ?, ?)",
        (data['name'], data['contact'], data['date'], data['food'], data['cleanliness'], data['comments'])
    )
    await message.answer('спасибо за отзыв')
    await state.clear()
