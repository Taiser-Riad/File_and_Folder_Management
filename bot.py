# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, CallbackQueryHandler, filters
# import logging
# import os

# # Enable logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Define file options
# file_options = [
#     ["file1.xlsx", "file2.xlsx", "file3.xlsx"]
# ]

# # Dictionary to keep track of user choices
# user_state = {}

# async def start(update: Update, context: CallbackContext) -> None:
#     keyboard = [
#         [InlineKeyboardButton("Order File", callback_data='order_file')],
#         [InlineKeyboardButton("Help", callback_data='help')],
#         [InlineKeyboardButton("Exit", callback_data='exit')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await update.message.reply_text('Choose a service:', reply_markup=reply_markup)

# async def help_command(update: Update, context: CallbackContext) -> None:
#     await update.message.reply_text('This bot can help you with the following:\n\n1. Order files\n2. Get help\n3. Exit\n\nTo start, use the /start command.')

# async def send_excel(update: Update, context: CallbackContext, file_name: str) -> None:
#     file_path = f'C:/Users/YourUsername/Desktop/{file_name}'
#     await update.message.reply_document(document=open(file_path, 'rb'))

# async def handle_menu(update: Update, context: CallbackContext) -> None:
#     query = update.callback_query
#     await query.answer()

#     user_id = query.from_user.id

#     if query.data == 'order_file':
#         keyboard = [[InlineKeyboardButton(file, callback_data=f'file_{file}') for file in files] for files in file_options]
#         keyboard.append([InlineKeyboardButton("Back", callback_data='back')])
#         reply_markup = InlineKeyboardMarkup(keyboard)
#         await query.edit_message_text(text="Choose a file to order:", reply_markup=reply_markup)
#     elif query.data == 'help':
#         await query.edit_message_text(text="This bot can help you with the following:\n\n1. Order files\n2. Get help\n3. Exit")
#     elif query.data == 'exit':
#         await query.edit_message_text(text="Goodbye!")
#     elif query.data == 'back':
#         await start(update, context)
#     elif query.data.startswith('file_'):
#         file_name = query.data.split('_')[1]
#         user_state[user_id] = file_name
#         keyboard = [
#             [InlineKeyboardButton("Confirm", callback_data='confirm')],
#             [InlineKeyboardButton("Cancel", callback_data='cancel')]
#         ]
#         reply_markup = InlineKeyboardMarkup(keyboard)
#         await query.edit_message_text(text=f"You chose {file_name}. Confirm?", reply_markup=reply_markup)
#     elif query.data == 'confirm':
#         if user_id in user_state:
#             file_name = user_state.pop(user_id)
#             await send_excel(update, context, file_name)
#             await query.edit_message_text(text=f"{file_name} has been sent!")
#         else:
#             await query.edit_message_text(text="No file chosen. Please start again.")
#     elif query.data == 'cancel':
#         await query.edit_message_text(text="Order cancelled. Please choose a service again.")
#         await start(update, context)

# async def error(update: Update, context: CallbackContext) -> None:
#     logger.warning('Update "%s" caused error "%s"', update, context.error)

# async def unknown_command(update: Update, context: CallbackContext) -> None:
#     await update.message.reply_text("Sorry, I didn't understand that command. Please use /start to choose a service.")

# def main() -> None:
#     # Retrieve the token from the environment variable
#     token = "7501261929:AAGLRxf2cuDf2F0b7Sx74pwkGDPR0EMLBzc"

#     if token is None:
#         raise ValueError("No TELEGRAM_BOT_TOKEN found. Please set the environment variable.")

#     # Create the Application object
#     application = Application.builder().token(token).build()

#     # Add handlers
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(CommandHandler("help", help_command))
#     application.add_handler(CallbackQueryHandler(handle_menu))
#     application.add_handler(MessageHandler(filters.COMMAND, unknown_command))

#     # Log all errors
#     application.add_error_handler(error)

#     # Start the bot
#     application.run_polling()

# if __name__ == '__main__':
#     main()





# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler
# import os
# import logging


# async def start(update: Update, context: CallbackContext) -> None:
#     keyboard = [
#         [InlineKeyboardButton("Browse Folders", callback_data='browse_folders')],
#         [InlineKeyboardButton("Help", callback_data='help')],
#         [InlineKeyboardButton("Exit", callback_data='exit')]]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     if update.message:
#         await update.message.reply_text('Choose an option:', reply_markup=reply_markup)
    
# async def list_files_and_folders(user_id: int, path: str) -> InlineKeyboardMarkup:
#     items = os.listdir(path)
#     keyboard = [[InlineKeyboardButton(item, callback_data=f'item_{item}')] for item in items if os.path.isdir(os.path.join(path, item))] 
#     files = [[InlineKeyboardButton(item, callback_data=f'download_{item}')] for item in items if os.path.isfile(os.path.join(path, item))] 
#     keyboard.extend(files)
#     keyboard.append([InlineKeyboardButton("Back", callback_data='back')])
#     # if path != base_path:
#     #     keyboard.append([InlineKeyboardButton("Back", callback_data='back')]) 
#     return InlineKeyboardMarkup(keyboard)  

  
# async def handle_menu(update: Update, context: CallbackContext) -> None:
#     query = update.callback_query
#     await query.answer()
#     user_id = query.from_user.id
    
#     if user_id not in user_paths:
#         user_paths[user_id] = base_path
    
#     if query.data == 'browse_folders':
#         path = user_paths[user_id]
#         path1 = 'C:/Users/tkadilo/Desktop/' # Change this to your specific path
#         reply_markup = await list_files_and_folders(user_id,path)
#         await query.edit_message_text(text="Choose a folder or file:", reply_markup=reply_markup)
        
        
#     elif query.data == 'help':
#         await query.edit_message_text(text="This bot helps you manage files and folders on your PC. Use the buttons to navigate and download files.")
#     elif query.data == 'exit':
#         await query.edit_message_text(text="Goodbye!") 
#     elif query.data == 'back':
#         user_paths[user_id] = os.path.dirname(user_paths[user_id])
#         await start(update, context) 
#     elif query.data.startswith('item_'):
#         folder_name = query.data.split('_')[1] 
#         user_paths[user_id] = os.path.join(user_paths[user_id], folder_name)
#         path = user_paths[user_id] # Update the path
#         reply_markup = await list_files_and_folders(user_id,path)
#         await query.edit_message_text(text=f"Contents of {folder_name}:", reply_markup=reply_markup)
#     elif query.data.startswith('download_'):
#         file_name = query.data.split('_')[1]
#         file_path = os.path.join([user_id], file_name) # Update the path
#         await query.message.reply_document(document=open(file_path, 'rb'))
        
# async def error(update: Update, context: CallbackContext) -> None:
#     logger.warning('Update "%s" caused error "%s"', update, context.error)    
    
# # Enable logging
# logging.basicConfig(format='%(asctime)s - %(name=s - %(levelname)s - %(message)s', level=logging.INFO)
# logger = logging.getLogger(__name__)    


# # Update this to your base directory path 
# base_path = f'C:/Users/tkadilo/Desktop/'
# user_paths = {}
# path = f'C:/Users/tkadilo/Desktop/'
   

    
# def main() -> None:
#     # Retrieve the token from the environment variable
#     token = "7501261929:AAGLRxf2cuDf2F0b7Sx74pwkGDPR0EMLBzc"


#     # Create the Application object
#     application = Application.builder().token(token).build()

#     # Add handlers
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(CallbackQueryHandler(handle_menu))

#     # Log all errors
#     application.add_error_handler(error)

#     # Start the bot
#     application.run_polling()

# if __name__ == '__main__':
#     main()




# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler
# import os
# import logging

# # Enable logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Base directory path
# #C:/Users/tkadilo/Desktop
# base_path = '//DS2/Network$/Quality/Taiseer'  # Update this to your base directory path
# user_paths = {}

# async def start(update: Update, context: CallbackContext) -> None:
#     keyboard = [
#         [InlineKeyboardButton("Browse Folders", callback_data='browse_folders')],
#         [InlineKeyboardButton("Help", callback_data='help')],
#         [InlineKeyboardButton("Exit", callback_data='exit')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     if update.message:
#         await update.message.reply_text('Choose an option:', reply_markup=reply_markup)
    
# async def list_files_and_folders(user_id: int, path: str) -> InlineKeyboardMarkup:
#     items = os.listdir(path)
#     keyboard = [[InlineKeyboardButton(item, callback_data=f'item_{item}')] for item in items if os.path.isdir(os.path.join(path, item))]
#     files = [[InlineKeyboardButton(item, callback_data=f'download_{item}')] for item in items if os.path.isfile(os.path.join(path, item))]
#     keyboard.extend(files)
#     keyboard.append([InlineKeyboardButton("Back", callback_data='back')])
#     if path != base_path:
#          keyboard.append([InlineKeyboardButton("Back", callback_data='back')]) 
#     return InlineKeyboardMarkup(keyboard)  

#     return InlineKeyboardMarkup(keyboard)

# async def handle_menu(update: Update, context: CallbackContext) -> None:
#     query = update.callback_query
#     await query.answer()
    
#     user_id = query.from_user.id
    
#     if user_id not in user_paths:
#         user_paths[user_id] = base_path
    
#     if query.data == 'browse_folders':
#         path = user_paths[user_id]
#         reply_markup = await list_files_and_folders(user_id, path)
#         await query.edit_message_text(text="Choose a folder or file:", reply_markup=reply_markup)
#     elif query.data == 'help':
#         await query.edit_message_text(text="This bot helps you manage files and folders on your PC. Use the buttons to navigate and download files.")
#     elif query.data == 'exit':
#         await query.edit_message_text(text="Goodbye!")
#     elif query.data == 'back':
#         user_paths[user_id] = os.path.dirname(user_paths[user_id])
#         await start(update,context)
#         path = user_paths[user_id]
#         reply_markup = await list_files_and_folders(user_id, path)
#         await query.edit_message_text(text="Choose a folder or file:", reply_markup=reply_markup)
#     elif query.data.startswith('item_'):
#         folder_name = query.data.split('_', 1)[1]
#         user_paths[user_id] = os.path.join(user_paths[user_id], folder_name)
#         path = user_paths[user_id]
#         reply_markup = await list_files_and_folders(user_id, path)
#         await query.edit_message_text(text=f"Contents of {folder_name}:", reply_markup=reply_markup)
#     elif query.data.startswith('download_'):
#         file_name = query.data.split('_', 1)[1]
#         file_path = os.path.join(user_paths[user_id], file_name)
#         await query.message.reply_document(document=open(file_path, 'rb'))

# async def error(update: Update, context: CallbackContext) -> None:
#     logger.warning('Update "%s" caused error "%s"', update, context.error)

# def main() -> None:
#     # Your Telegram bot token
#     token = "7501261929:AAGLRxf2cuDf2F0b7Sx74pwkGDPR0EMLBzc"

#     # Create the Application object
#     application = Application.builder().token(token).build()

#     # Add handlers
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(CallbackQueryHandler(handle_menu))

#     # Log all errors
#     application.add_error_handler(error)

#     # Start the bot
#     application.run_polling()

# if __name__ == '__main__':
#     main()



from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler
from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname=s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Base directory path
base_path = '//DS2/Network$/Quality'  # Update this to your base directory path
user_paths = {}

async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Browse Folders", callback_data='browse_folders')],
        [InlineKeyboardButton("Help", callback_data='help')],
        [InlineKeyboardButton("Exit", callback_data='exit')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.message:
        await update.message.reply_text('Choose an option:', reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.edit_message_text('Choose an option:', reply_markup=reply_markup)

async def list_files_and_folders(user_id: int, path: str) -> InlineKeyboardMarkup:
    try:
        items = os.listdir(path)
        keyboard = []
        # Add directories
        for item in items:
            if os.path.isdir(os.path.join(path, item)):
                callback_data = f'item_{item}'
                if len(callback_data) > 64:
                    callback_data = callback_data[:64]
                keyboard.append([InlineKeyboardButton(item, callback_data=callback_data)])
        # Add files
        for item in items:
            if os.path.isfile(os.path.join(path, item)):
                callback_data = f'download_{item}'
                if len(callback_data) > 64:
                    callback_data = callback_data[:64]
                keyboard.append([InlineKeyboardButton(item, callback_data=callback_data)])
        # Add back button if not in base path
        if path != base_path:
            keyboard.append([InlineKeyboardButton("Back", callback_data='back')])
        return InlineKeyboardMarkup(keyboard)
    except Exception as e:
        logger.error(f"Error listing files and folders: {e}")
        return InlineKeyboardMarkup([[InlineKeyboardButton("Back", callback_data='back')]])

async def handle_menu(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    
    if user_id not in user_paths:
        user_paths[user_id] = base_path
    
    if query.data == 'browse_folders':
        path = user_paths[user_id]
        reply_markup = await list_files_and_folders(user_id, path)
        await query.edit_message_text(text="Choose a folder or file:", reply_markup=reply_markup)
    elif query.data == 'help':
        await query.edit_message_text(text="This bot helps you manage files and folders on your PC. Use the buttons to navigate and download files.")
    elif query.data == 'exit':
        await query.edit_message_text(text="Goodbye!")
    elif query.data == 'back':
        user_paths[user_id] = os.path.dirname(user_paths[user_id])
        path = user_paths[user_id]
        reply_markup = await list_files_and_folders(user_id, path)
        await query.edit_message_text(text="Choose a folder or file:", reply_markup=reply_markup)
    elif query.data.startswith('item_'):
        folder_name = query.data.split('_', 1)[1]
        user_paths[user_id] = os.path.join(user_paths[user_id], folder_name)
        path = user_paths[user_id]
        reply_markup = await list_files_and_folders(user_id, path)
        await query.edit_message_text(text=f"Contents of {folder_name}:", reply_markup=reply_markup)
    elif query.data.startswith('download_'):
        file_name = query.data.split('_', 1)[1]
        file_path = os.path.join(user_paths[user_id], file_name)
        try:
            await query.message.reply_document(document=open(file_path, 'rb'))
        except Exception as e:
            logger.error(f"Error downloading file: {e}")
            await query.message.reply_text("There was an error downloading the file. Please try again.")

async def error(update: Update, context: CallbackContext) -> None:
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main() -> None:
    
    # Retrieve the token from the environment variable
    token = os.getenv("BOT_TOKEN")
    
    
    # Create the Application object
    application = Application.builder().token(token).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_menu))

    # Log all errors
    application.add_error_handler(error)

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
