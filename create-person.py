import credentials
import cognitive_face as cf


cf.BaseUrl.set(credentials.face_api_base_url)
cf.Key.set(credentials.face_api_key)


name = 'Manvendra Nath Thakur'
name_data = "TMH2KOR"
response = cf.person.create(credentials.face_api_person_group_id, name, name_data)
print (response)
name_id = response['personId']
print (name_id)

cf.person.add_face('/home/pi/images/test-person/mnt1.jpg', credentials.face_api_person_group_id, name_id)
#cf.person.add_face('/home/pi/images/test-person/mnt2.jpg', credentials.face_api_person_group_id, name_id)
#cf.person.add_face('/home/pi/images/test-person/mnt3.jpg', credentials.face_api_person_group_id, name_id)
cf.person.add_face('/home/pi/images/test-person/mnt4.jpg', credentials.face_api_person_group_id, name_id)
cf.person.add_face('/home/pi/images/test-person/mnt5.jpg', credentials.face_api_person_group_id, name_id)

name = 'Saksham Srivastava'
name_data = "ABQ8KOR"
response = cf.person.create(credentials.face_api_person_group_id, name, name_data)
print (response)
name_id = response['personId']
print (name_id)

cf.person.add_face('/home/pi/images/test-person/ss1.jpg', credentials.face_api_person_group_id, name_id)
#cf.person.add_face('/home/pi/images/test-person/ss2.jpg', credentials.face_api_person_group_id, name_id)
#cf.person.add_face('/home/pi/images/test-person/ss3.jpg', credentials.face_api_person_group_id, name_id)
cf.person.add_face('/home/pi/images/test-person/ss4.jpg', credentials.face_api_person_group_id, name_id)
cf.person.add_face('/home/pi/images/test-person/ss5.jpg', credentials.face_api_person_group_id, name_id)

name = 'Gunjan Maheshwari'
name_data = "GMJ1KOR"
response = cf.person.create(credentials.face_api_person_group_id, name, name_data)
print (response)
name_id = response['personId']
print (name_id)

cf.person.add_face('/home/pi/images/test-person/gm1.jpg', credentials.face_api_person_group_id, name_id)
#cf.person.add_face('/home/pi/images/test-person/gm2.jpg', credentials.face_api_person_group_id, name_id)
cf.person.add_face('/home/pi/images/test-person/gm3.jpg', credentials.face_api_person_group_id, name_id)
#cf.person.add_face('/home/pi/images/test-person/gm4.jpg', credentials.face_api_person_group_id, name_id)
cf.person.add_face('/home/pi/images/test-person/gm5.jpg', credentials.face_api_person_group_id, name_id)

name = 'Nikita Singh'
name_data = "ISI3KOR"
response = cf.person.create(credentials.face_api_person_group_id, name, name_data)
print (response)
name_id = response['personId']
print (name_id)

cf.person.add_face('/home/pi/images/test-person/ns1.jpg', credentials.face_api_person_group_id, name_id)
#cf.person.add_face('/home/pi/images/test-person/ns2.jpg', credentials.face_api_person_group_id, name_id)
#cf.person.add_face('/home/pi/images/test-person/ns3.jpg', credentials.face_api_person_group_id, name_id)
cf.person.add_face('/home/pi/images/test-person/ns4.jpg', credentials.face_api_person_group_id, name_id)
cf.person.add_face('/home/pi/images/test-person/ns5.jpg', credentials.face_api_person_group_id, name_id)

name = 'Saugat Modak'
name_data = "AOU2KOR"
response = cf.person.create(credentials.face_api_person_group_id, name, name_data)
print (response)
name_id = response['personId']
print (name_id)

cf.person.add_face('/home/pi/images/test-person/sm1.jpg', credentials.face_api_person_group_id, name_id)
#cf.person.add_face('/home/pi/images/test-person/sm2.jpg', credentials.face_api_person_group_id, name_id)
#cf.person.add_face('/home/pi/images/test-person/sm3.jpg', credentials.face_api_person_group_id, name_id)
cf.person.add_face('/home/pi/images/test-person/sm4.jpg', credentials.face_api_person_group_id, name_id)
cf.person.add_face('/home/pi/images/test-person/sm5.jpg', credentials.face_api_person_group_id, name_id)
