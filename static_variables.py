ESTATE_IMAGE_UPLOAD_PATH = 'estates/'
ESTATE_PROPERTY_IMAGE_UPLOAD_PATH = 'estates/properties/'

AD_TYPE_CHOICES = (('R', 'اجاره'), ('S', 'فروش'))
AD_CATEGORY_CHOICES = (
    ('RESIDENTIAL', 'مسکونی'),
    ('BUSINESS', 'تجاری'),
    ('OFFICIAL', 'اداری'),
    ('VILLA', 'ویلایی'),
    ('KOLANGI', 'کلنگی'),
    ('REAL_ESTATE', 'مستغلات'),
)

USER_CONTACT_STATUS = (('CLUE', 'سرنخ'),
                       ('EVALUATED', 'ارزیابی شده'),
                       ('INTRODUCED', 'معرفی شده'),
                       ('SERVICED_PROVIDED', 'سرویس داده شده'),
                       ('NEGOTIATED', 'مذاکره شده'),
                       ('MEETING', 'جلسه گذاشته شد'),
                       ('CONTRACTING', 'قرار داد بسته شد'),
                       ('CANCELED', 'لغو شد'))


EXPORT_USER_XLSX_CELL_FIELDS = ['id', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined',
                                'country_code', 'phone_number', 'is_phone_number_verified', 'is_consultant', 'ad_monthly_quota', 'ladder_monthly_quota', 'special_ad_monthly_quota']
