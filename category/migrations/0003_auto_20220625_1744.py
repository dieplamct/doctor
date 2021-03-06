# Generated by Django 4.0.4 on 2022-06-25 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20220625_1729'),
        ('language', '0002_auto_20220616_2223')
    ]

    def insertData(apps, schema_editor):
        CategoryTranslation = apps.get_model('category', 'CategoryTranslation')
        data = ("过敏",
                 "男科",
                 "心脏病学",
                 "皮肤科",
                 "营养学",
                 "诊断影像科",
                 "内分泌学",
                 "妇科",
                 "肠胃病学",
                 "老年病学",
                 "血液学",
                 "内科",
                 "住院部",
                 "肾脏病学",
                 "神经病学",
                 "肿瘤学",
                 "牙科学",
                 "骨科")

        for i in range(len(data)):
            category_translation = CategoryTranslation(category_id=(i+1), name=data[i], language_id=1)
            category_translation.save()

        data = ("Allergy",
                "Andrology",
                "Cardiology",
                "Dermatology",
                "Dietetics",
                "Diagnostic imaging department",
                "Endocrinology",
                "Gynecology",
                "Gastroenterology",
                "Geriatrics",
                "Haematology",
                "Internal medicine",
                "Inpatient department",
                "Nephrology",
                "Neurology",
                "Oncology",
                "Odontology",
                "Orthopaedics")
        
        for i in range(len(data)):
            category_translation = CategoryTranslation(category_id=(i+1), name=data[i], language_id=2)
            category_translation.save()

    operations = [
        migrations.RunPython(insertData),
    ]
