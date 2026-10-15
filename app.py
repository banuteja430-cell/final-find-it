if request.form.get('captcha')!='8':
    return "<h3>Wrong Captcha! Type 8</h3><a href='/'>Back</a>"
