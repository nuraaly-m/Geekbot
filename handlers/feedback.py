from aiogram import Router, F, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


feedback_router = Router()

class Feedback(StatesGroup):
    name = State()
    contact = State()
    date = State()
    food = State()
    cleanliness = State()
    comments = State()



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
    await state.update_data(date=int(date))
    await state.set_state(Feedback.food)
    await message.answer('какое было качество еды?', reply_markup=kb)
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


@feedback_router.message(Feedback.food)
async def process_food(message: types.Message, state: FSMContext):
    await state.update_data(food=message.text)
    await state.set_state(Feedback.cleanliness)
    await message.answer('как оцениваете чистоту заведения?')


@feedback_router.message(Feedback.cleanliness)
async def process_cleanlines(message: types.Message, state: FSMContext):
    await state.update_data(cleanlines=message.text)
    await state.set_state(Feedback.comments)
    await message.answer('дополноительные комментарии:')


@feedback_router.message(Feedback.comments)
async def process_comments(message: types.Message, state: FSMContext):
    await state.update_data(comments=message.text)
    await message.answer('спасибо за отзыв')