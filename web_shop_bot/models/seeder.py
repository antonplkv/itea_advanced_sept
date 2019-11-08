from mongoengine import connect
import models
connect("web_shop_bot")


subsucb_cat_example = {
    'title': 'Subcut of subcut',
    'description': 'i am the lowest in the current hierarchy'
}

subsubc_cat = models.Category(**subsucb_cat_example).save()
subcut_example = {
    'title': 'Subcut of root',
    'description': 'i am the subcut of root category',
    'subcategory': [subsubc_cat]
}

subcut = models.Category(**subcut_example).save()

cat_example = {
    'title': 'The root',
    'description': 'Root directory description',
    'is_root': True,
    'subcategory': [subcut]
}

cat = models.Category(**cat_example).save()





