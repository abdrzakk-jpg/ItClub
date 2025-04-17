from pkg import app, db, socketio
from pkg.routes import *
import os
from datetime import datetime

import logging

if __name__ == '__main__':
    # stop logging in production
    if os.environ.get("FLASK_ENV") == "production":
        logging.getLogger('werkzeug').disabled = True
    
    port = int(os.environ.get("PORT", 10000))   

    # التأكد من إنشاء قاعدة البيانات وتهيئة المسؤول الافتراضي فقط في بيئة التطوير
    if os.environ.get("FLASK_ENV") != "production":
        with app.app_context():
            db.create_all()
            initilaize_default_admins(
                full_name='حاج قويدر عبد الرزاق',
                email = 'abdrzakk.dz@gmail.com',
                password = 'abdo123',
                birth_date= datetime.strptime('02/05/2008', '%d/%m/%Y'),
                acadimic_year='سنة ثانية ثانوي'
            )

            initilaize_default_admins(
                full_name='سعداوي ناجم',
                email = 'najibsaadaoui1999@gmail.com',
                password = 'Nadjem1995',
                birth_date= datetime.strptime('26/11/1995', '%d/%m/%Y'),
                acadimic_year='غير محدد'
            )

    # إعدادات التشغيل
    if os.environ.get("FLASK_ENV") == "production":
        # إعدادات الإنتاج
        app.run(host='0.0.0.0', port=port)
    else:
        # إعدادات التطوير
        socketio.run(
            app,
            host='0.0.0.0',
            port=port,
            debug=False,
            use_reloader=False,
            allow_unsafe_werkzeug=True
        )