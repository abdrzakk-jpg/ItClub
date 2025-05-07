from pkg import app, db, socketio
from pkg.utils.load_env import PRODUCTION

if __name__ == '__main__':

    

        # initilaize default admin


        # إعدادات التطوير
    # system('kill -9 $(lsof -ti:5000)')
    # logging.getLogger('werkzeug').disabled = True
    socketio.run(
                app,    
                host='0.0.0.0',
                port=5000,
            )
