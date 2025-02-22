from kavenegar import KavenegarAPI


def send_sms(phone_number, code):
    try:
        api = KavenegarAPI('78323961326C677677354935544C79543059434A32363451334246456C77507779314F56653943536671633D')  # کلید API خود را اینجا وارد کنید
        params = {
            'sender': '2000660110',  # شماره ارسال‌کننده پیامک (اختیاری، بستگی به سرویس شما دارد)
            'receptor': f"{phone_number}",  # شماره گیرنده
            'message': f'کد تایید شما: {code}',  # پیام ارسال‌شده
        }
        api.sms_send(params)
    except Exception as e:
        print(f"Error sending SMS: {e}")
