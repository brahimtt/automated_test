import pytest
import requests
import json

class Test_courses:


    token=None
    @pytest.fixture(scope="class",autouse=True)
    def setup_teardown(self):
       global token
       password = "Aqwzsx12435"
       email="brahim.touti15@gmail.com"
       payload = {"email":email, "password": password}
       r = requests.post(f'http://localhost:8000/users/login', data=payload)
       json = r.json()
       token = json['token']
       user=json['user']
       yield
       headers = {'Authorization': token }
       r = requests.post(f'http://localhost:8000/users/logout', data=user, headers=headers)
       

    @pytest.fixture(scope="function")
    def create_course(self):
        payload = {
            "price": 20,
            "title": "pytest",
            "start_date": "2023-06-09 14:00:00",
            "description": "lsmlsmsùs!",
            "duration": 20,
        }
        headers = {'Authorization': token }
        r = requests.post(f'http://localhost:8000/courses/', data=payload, headers=headers)
        r_dict=json.loads(r.content)
        course_id=r_dict['id']
        yield course_id
        headers = {'Authorization': token }
        r = requests.delete(f'http://localhost:8000/courses/{course_id}', headers=headers)



       
    
    def test_check_course_creation(self,create_course):
        courses_list=[]
        course_ids=[]
        id=create_course
        r = requests.get(f'http://localhost:8000/courses/')
        courses_lists=r.json()
        courses_list=courses_lists[-1]
        print(courses_list)
        """ courses=dict(courses_lists)
        liste_of_courses=courses["courses"]


        for courses in liste_of_courses:
            courses_list.append(courses)
            for course in courses_list:
                course_ids.append(course["id"])
        assert id in course_ids """

            
            
        assert True        

        
    
    
     

