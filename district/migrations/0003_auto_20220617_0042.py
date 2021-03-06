# Generated by Django 4.0.4 on 2022-06-17 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0002_auto_20220616_2240'),
    ]

    def insertData(apps, schema_editor):
        DistrictTranslation = apps.get_model('district', 'DistrictTranslation')
        data = ("離島區",
                "葵青區",
                "北區",
                "西貢區",
                "沙田區",
                "大埔區",
                "荃灣區",
                "屯門區",
                "元朗區",
                "九龍城區",
                "觀塘區",
                "深水埗區",
                "黃大仙區",
                "油尖旺區",
                "中西區",
                "東區",
                "南區",
                "灣仔區")

        for i in range(len(data)):
            district_translation = DistrictTranslation(district_id=(i+1), name=data[i], language_id=1)
            district_translation.save()

        data = ("Islands",
                "Kwai Tsing",
                "North",
                "Sai Kung",
                "Sha Tin",
                "Tai Po",
                "Tsuen Wan",
                "Tuen Mun",
                "Yuen Long",
                "Kowloon City",
                "Kwun Tong",
                "Sham Shui Po",
                "Wong Tai Sin",
                "Yau Tsim Mong",
                "Central and Western",
                "Eastern",
                "Southern",
                "Wan Chai")
        
        for i in range(len(data)):
            district_translation = DistrictTranslation(district_id=(i+1), name=data[i], language_id=2)
            district_translation.save()

    operations = [
        migrations.RunPython(insertData),
    ]
