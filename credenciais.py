import keyring

smtp_user = 'seu_email@gmail.com'
smtp_password = 'sua_senha_gerada_app'  

keyring.set_password('smtp', smtp_user, smtp_password)