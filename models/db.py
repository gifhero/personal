db = DAL("sqlite://storage.sqlite")


phone_models = ['iPhone 4', 'iPhone 4s', 'iPhone 5', 'iPhone 5c', 'iPhone 5s', 'iPhone 6', 'iPhone 6 Plus', 'iPhone 6s', 'iPhone 6s Plus', 'iPhone SE', 'iPhone 7', 'iPhone 7 Plus', 'iPhone 8', 'iPhone 8 Plus']
screen_prices = [20, 20, 25, 25, 25, 30, 30, 30, 45, 45, 45, 45, 45, 45]
phone_screen_colors = ['Black', 'White']
spare_phone_options = ['Yes', 'No']

db.define_table('post',
    Field('name'),
    Field('email'),
    Field('phone_number'),
    Field('phone_model'),
    Field('phone_screen_color'),
    Field('spare_phone'),
    Field('price', type='string', default=request.vars.name),
    Field('notes', 'text'))

db.post.name.requires = IS_NOT_EMPTY(error_message="Enter name")
db.post.email.requires = IS_EMAIL(error_message="Invalid email")
db.post.phone_number.requires = IS_MATCH('^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$', error_message="Invalid Number")
db.post.phone_model.requires = IS_IN_SET(phone_models, zero='Select Option', error_message="Select model")
db.post.spare_phone.requires = IS_IN_SET(spare_phone_options, zero='Select Option', error_message="Select option")
db.post.phone_screen_color.requires = IS_IN_SET(phone_screen_colors, zero='Select Option', error_message="Select screen color")




db.define_table('comment',
                Field('comment', 'text'))

db.comment.comment.requires = IS_NOT_EMPTY(error_message="No comment entered")
