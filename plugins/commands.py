import os
import sys
import asyncio 
from database import db, mongodb_version
from config import Config, temp
from platform import python_version
from translation import Translation
from pyrogram import Client, filters, enums, __version__ as pyrogram_version
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaDocument

main_buttons = [[
        InlineKeyboardButton('❣️ ᴅᴇᴠᴇʟᴏᴘᴇʀ ❣️', url='https://t.me/IM_JISSHU')
        ],[
        InlineKeyboardButton('📜𝗎𝗉𝖽𝖺𝗍𝖾 𝖼𝗁𝖺𝗇𝗇𝖾𝗅 ', callback_data='aman'),
        InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ  ', callback_data='amanji')
        ],[
        InlineKeyboardButton('🙋‍♂️ ʜᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('💁‍♂️ ᴀʙᴏᴜᴛ ', callback_data='about')
        ],[
        InlineKeyboardButton('⚙️ sᴇᴛᴛɪɴɢs ⚙️', callback_data='settings#main')
        ]]
#===================Start Function===================#

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    user = message.from_user
    if not await db.is_user_exist(user.id):
      await db.add_user(user.id, user.first_name)
    reply_markup = InlineKeyboardMarkup(main_buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=InlineKeyboardMarkup(main_buttons),
        text=Translation.START_TXT.format(message.from_user.first_name))

#==================Restart Function==================#

@Client.on_message(filters.private & filters.command(['restart']) & filters.user(Config.BOT_OWNER_ID))
async def restart(client, message):
    msg = await message.reply_text(
        text="<i>Trying to restarting.....</i>"
    )
    await asyncio.sleep(5)
    await msg.edit("<i>Server restarted successfully ✅</i>")
    os.execl(sys.executable, sys.executable, *sys.argv)
    
#==================Callback Functions==================#

@Client.on_callback_query(filters.regex(r'^help'))
async def helpcb(bot, query):
    await query.message.edit_text(
        text=Translation.HELP_TXT,
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ❓', callback_data='how_to_use')
            ],[
            InlineKeyboardButton('⚙️ sᴇᴛᴛɪɴɢs ', callback_data='settings#main'),
            InlineKeyboardButton('📜 sᴛᴀᴛᴜs ', callback_data='status')
            ],[
            InlineKeyboardButton('↩ ʙᴀᴄᴋ', callback_data='back')
            ]]
        ))

@Client.on_callback_query(filters.regex(r'^aman'))
async def helpcb(bot, query):
    await query.message.edit_text(
        text=Translation.CHANNELS_TXT,
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('𝑺𝒖𝒃𝒔𝒄𝒓𝒊𝒃𝒆 𝒎𝒚 𝒀𝑻 𝒄𝒉𝒂𝒏𝒏𝒆𝒍', url='https://youtube.com/@ytdautobotz?si=gVP9stGBDZKueRVz')
        ],[
            InlineKeyboardButton('𝑮𝒓𝒐𝒖𝒑', url='https://t.me/+X3uoMkIHhco1YTY1'),
            InlineKeyboardButton('𝑪𝒉𝒂𝒏𝒏𝒆𝒍', url='https://t.me/Latestmoviesupdates0')
        ],[
            InlineKeyboardButton('𝑺𝒖𝒑𝒑𝒐𝒓𝒕', url='https://t.me/+cZGisR7lHeg1ZDdl'),
            InlineKeyboardButton('𝑼𝒑𝒅𝒂𝒕𝒆', url='https://t.me/Moviesofficialchannel0')
        ],[
            InlineKeyboardButton('𝑩𝒂𝒄𝒌', callback_data='back')
        ]]

        ))

@Client.on_callback_query(filters.regex(r'^amanji'))
async def helpcb(bot, query):
    await query.message.edit_text(
        text=Translation.CHANNELS_TXT,
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('Bᴏᴛ¹', url='https://t.me/Movie_000_bot')
        ],[
            InlineKeyboardButton('Bᴏᴛ²', url='https://t.me/YDFileStoreBot'),
            InlineKeyboardButton('Bᴏᴛ³', url='https://t.me/YD_Renema_Bot')
        ],[
            InlineKeyboardButton('Bᴏᴛ⁴', url='https://t.me/YD_String_Generator_Bot'),
            InlineKeyboardButton('Bᴏᴛ⁵', url='https://t.me/YD_2GPT_BOT')
        ],[
            InlineKeyboardButton('𝑩𝒂𝒄𝒌', callback_data='back'),
            InlineKeyboardButton('Bᴏᴛ¹', callback_data='aman')
        ]]

        ))

@Client.on_callback_query(filters.regex(r'^how_to_use'))
async def how_to_use(bot, query):
    await query.message.edit_text(
        text=Translation.HOW_USE_TXT,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('↩ Back', callback_data='help')]]),
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex(r'^back'))
async def back(bot, query):
    reply_markup = InlineKeyboardMarkup(main_buttons)
    await query.message.edit_text(
       reply_markup=reply_markup,
       text=Translation.START_TXT.format(
                query.from_user.first_name))

@Client.on_callback_query(filters.regex(r'^about'))
async def about(bot, query):
    await query.message.edit_text(
        text=Translation.ABOUT_TXT.format(my_name='Public Forward',python_version=python_version(),pyrogram_version=pyrogram_version,mongodb_version=await mongodb_version()),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('↩ Back', callback_data='back')]]),
        disable_web_page_preview=True,
        parse_mode=enums.ParseMode.HTML,
    )

@Client.on_callback_query(filters.regex(r'^status'))
async def status(bot, query):
    users_count, bots_count = await db.total_users_bots_count()
    total_channels = await db.total_channels()
    await query.message.edit_text(
        text=Translation.STATUS_TXT.format(users_count, bots_count, temp.forwardings, total_channels, temp.BANNED_USERS ),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('↩ Back', callback_data='help')]]),
        parse_mode=enums.ParseMode.HTML,
        disable_web_page_preview=True,
    )
