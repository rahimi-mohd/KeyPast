# Very simple password manager and generator

Inspired by keepassxc

## To Activate Database
1. `flask db init`
2. `flask db migrate -m "password table"`
3. `flask db upgrade`

TODO:
1. New page for all password
2. Login page
3. User registration page
3. Separate logic code & cleanup
4. Use base.html
5. Use hash password (Miguel)

## Reference
1. [Miguel's Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
