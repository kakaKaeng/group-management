from django.db import models

NULL_BLANK = {'null': True, 'blank': True}
CHAR_NULL_BLANK = {'max_length': 255, **NULL_BLANK}
DEFAULT_NONE_NULL_BLANK = {'default': None, **NULL_BLANK}
READ_ONLY_REQUIRED_FALSE = {'read_only': True, 'required': False}
NULL_DEFAULT_NONE = {"null": True, "default": None}
FK_NULL_BLANK_DO_NOTING = {"on_delete": models.DO_NOTHING, "db_index": True, **NULL_DEFAULT_NONE}
FK_NULL_BLANK_SET_NULL = {"on_delete": models.SET_NULL, **NULL_DEFAULT_NONE}
FK_NULL_BLANK_CASCADE = {"on_delete": models.CASCADE, **NULL_DEFAULT_NONE}
DECIMAL_PRICE = {"max_digits": 20, "decimal_places": 2, "default": 0}

EXCLUDE_COMMON_FIELDS = ('created_at', 'updated_at', 'created_user', 'updated_user')
REQUIRED_FALSE = {'required': False, 'allow_null': True}
