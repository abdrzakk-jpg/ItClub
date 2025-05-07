
from flask import render_template, Blueprint
from pkg.utils.colors import *
from pkg.utils.forms import AiChatForm
ai_chat_bp = Blueprint('ai_chat', __name__)

@ai_chat_bp.route('/nibras_ai', methods=['GET', 'POST'])
def ai_chat():
    try:
        form = AiChatForm()
        if form.validate_on_submit():
            yellow(form.data)
        return render_template('nibrasAi.html', form=form)
    except Exception as error:
        red(error)

from pkg.routes.Websockets.ai_chat_ws import handle_user_message