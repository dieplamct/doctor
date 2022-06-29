# doctor
Doctor API with Django REST framework

----
## 1. Choice of Framework & Library
> a. Acctualy I have a experience with **Tonado** Framework and a bit experience with **Django**, as you know **Tonado** is an non-blocking framework, in the requirement we do need an API collection therefore this case **Django** is more fit. **Django** Help us easy generate model, define model mapping with database, and do great migrate job.
>
> b. I assumpt this choice is the best choice in this case, and it fit with my experiences, fit with the requirement 
## 2. Potential Improvement
> a. Pagination for load all doctor or fiter by category, district ect.
> 
> b. Handling exeption friendly to response in case error or exeption happened
> 
> c. Validate input data 
> 
> d. Adding entity to transit data between layer
>
> e. Unit testing need to be done and add more unit testing

## 3. Production consideration
> I'll go with orchestration container service like docker swam or kubernetes for production infrastucture
> 
> Considering about caching for data to reduce DB request

## 4. Assumptions

### Get list doctor via API curl -X GET http://127.0.0.1:8000/doctor
```
[
    {
        "id": "5",
        "name": "diep lam 01",
        "address": "hoa hai 01",
        "phone": "0976129155",
        "fee": "55.00",
        "district": {
            "id": 2,
            "name": "Kwai Tsing",
            "translated": [
                {
                    "name": "葵青區",
                    "language": {
                        "id": 1,
                        "name": "Hong Kong",
                        "short_name": "hk"
                    }
                },
                {
                    "name": "Kwai Tsing",
                    "language": {
                        "id": 2,
                        "name": "English",
                        "short_name": "en"
                    }
                }
            ]
        },
        "category": {
            "id": 3,
            "active": true,
            "translated": [
                {
                    "name": "心脏病学",
                    "language": {
                        "id": 1,
                        "name": "Hong Kong",
                        "short_name": "hk"
                    }
                },
                {
                    "name": "Cardiology",
                    "language": {
                        "id": 2,
                        "name": "English",
                        "short_name": "en"
                    }
                }
            ]
        },
        "language": {
            "id": 2,
            "name": "English",
            "short_name": "en"
        }
    },
    {
        ...
    },
    ...
]
```
#### Create doctor with API 
```
curl -X POST \
  http://127.0.0.1:8000/doctor \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: 1c1a12d7-6b37-6768-cf9a-333db501c7ee' \
  -d '{
	"name": "diep.lam",
	"address": "hoa-hai",
	"fee": 55,
	"phone": "0976129155",
	"district": 2,
	"category": 3,
	"language": 2,
	"schedule": {
		"mon": "7-8",
		"tue": "8-9",
		"wend": "9-10",
		"thur":"10-11",
		"frid": "11-12",
		"satu": "12-13",
		"sun": "13-14"
	}
}'
```
The response is
```
{
    "id": "9",
    "name": "diep.lam",
    "address": "hoa-hai",
    "phone": "0976129155",
    "fee": "55",
    "district": {
        "id": 2,
        "name": "Kwai Tsing",
        "translated": [
            {
                "name": "葵青區",
                "language": {
                    "id": 1,
                    "name": "Hong Kong",
                    "short_name": "hk"
                }
            },
            {
                "name": "Kwai Tsing",
                "language": {
                    "id": 2,
                    "name": "English",
                    "short_name": "en"
                }
            }
        ]
    },
    "category": {
        "id": 3,
        "active": true,
        "translated": [
            {
                "name": "心脏病学",
                "language": {
                    "id": 1,
                    "name": "Hong Kong",
                    "short_name": "hk"
                }
            },
            {
                "name": "Cardiology",
                "language": {
                    "id": 2,
                    "name": "English",
                    "short_name": "en"
                }
            }
        ]
    },
    "language": {
        "id": 2,
        "name": "English",
        "short_name": "en"
    }
}
```
#### Get a doctor via API: curl -X GET http://127.0.0.1:8000/doctor/8 
```
{
    "id": "8",
    "name": "diep.lam",
    "address": "hoa-hai",
    "phone": "0976129155",
    "fee": "55.00",
    "district": {
        "id": 2,
        "name": "Kwai Tsing",
        "translated": [
            {
                "name": "葵青區",
                "language": {
                    "id": 1,
                    "name": "Hong Kong",
                    "short_name": "hk"
                }
            },
            {
                "name": "Kwai Tsing",
                "language": {
                    "id": 2,
                    "name": "English",
                    "short_name": "en"
                }
            }
        ]
    },
    "category": {
        "id": 3,
        "active": true,
        "translated": [
            {
                "name": "心脏病学",
                "language": {
                    "id": 1,
                    "name": "Hong Kong",
                    "short_name": "hk"
                }
            },
            {
                "name": "Cardiology",
                "language": {
                    "id": 2,
                    "name": "English",
                    "short_name": "en"
                }
            }
        ]
    },
    "language": {
        "id": 2,
        "name": "English",
        "short_name": "en"
    }
}
```

#### Filter by **district** via API: http://127.0.0.1:8000/doctor?district=1
#### Filter by **category** via API: http://127.0.0.1:8000/doctor?category=2
#### Filter by **language** via API: http://127.0.0.1:8000/doctor?language=1
```
the reponse is the same with get list doctor
```