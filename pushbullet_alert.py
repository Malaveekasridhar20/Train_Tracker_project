from pushbullet import Pushbullet

def send_pushbullet_alert(api_key, title, message):
    try:
        pb = Pushbullet(api_key)
        push = pb.push_note(title, message)
        return True, push
    except Exception as e:
        return False, str(e)
