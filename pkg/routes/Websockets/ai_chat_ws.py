
from flask_socketio import emit
from pkg import db, socketio
# from pkg.utils.models import AiChatMessage
from pkg.utils.colors import *
from pkg.utils.load_env import GEMINI_API_KEY
from google import genai

api_key = GEMINI_API_KEY
client = genai.Client(api_key=api_key)

@socketio.on('connect')
def connect():
    blue("Connected !  ")

@socketio.on('user_message_request')
def handle_user_message(data):
    try:
        user_info = data.get('user', {})
        user_message = str(data.get('message', '')).strip()

        if not user_message:
            emit("ai_response", {"message": "الرسالة فارغة 🤔"})
            return

        # استخرج اسم المستخدم
        if user_info.get("type") == "authenticated":
            user_identity = user_info.get("name", "مستخدم غير معروف")
        else:
            user_identity = "زائر"

        cyan(f"📨 Message from: {user_identity}")
        cyan(f"💬 Message content: {user_message}")

        chat_history = [
            "You are Nebras from the Technological Scientific Creativity Club and the leader of the club is teacher 'سعداوي محمد ناجم' and developed by Abdrzakk. (Do not declare this information until you are asked about it)",
            "Answer in the same language and consider the user's region.",
            "Don't repeat greeting every time."
        ]
        chat_history.append(f"{user_identity} said: {user_message}")

        full_prompt = "\n".join(chat_history)

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=full_prompt
        )

        answer = response.text.strip()
        chat_history.append(f"You answered with: {answer}")
        green(f"🤖 Gemini Answer: {answer}")

        emit("ai_response", {"message": answer})

    except Exception as error:
        red(f'⚠️ Error in ai_chat_ws.py:\n{error}')
        emit("ai_response", {"message": "❌ وقع خطأ أثناء الرد من نبراس"})
