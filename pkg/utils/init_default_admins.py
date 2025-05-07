from pkg.utils.helpers import initilaize_default_admin
from datetime import datetime
from pkg.utils.load_env import (ADMIN_1_EMAIL
                                ,ADMIN_1_PASSWORD
                                ,ADMIN_2_EMAIL
                                ,ADMIN_2_PASSWORD
                                )



initilaize_default_admin(
    full_name='حاج قويدر عبد الرزاق',
    email = ADMIN_1_EMAIL ,
    password = ADMIN_1_PASSWORD,
    birth_date= datetime.strptime('02/05/2008', '%d/%m/%Y'),
    academic_year= 'ثانية ثانوي'
)

initilaize_default_admin(
    full_name='سعداوي ناجم',
    email = ADMIN_2_EMAIL,
    password = ADMIN_2_PASSWORD,
    birth_date= datetime.strptime('26/11/1995', '%d/%m/%Y'),
    academic_year='غير محدد'
    )