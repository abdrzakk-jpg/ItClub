

from pkg.routes.login import login_bp
from pkg.routes.register import register_bp
from pkg.routes.chat import chat_bp
from pkg.routes.myaccount import myaccount_bp
from pkg.routes.adminpage import adminpage_bp
from pkg.routes.home import home_bp
from pkg.routes.ai_chat import ai_chat_bp

all_bps = [login_bp, register_bp, chat_bp, myaccount_bp, adminpage_bp, home_bp, ai_chat_bp]