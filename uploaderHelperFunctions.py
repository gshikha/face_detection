import datetime
from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings
from azure.storage.common.retry import no_retry
import requests
import cognitive_face as cf
import credentials
import os


#connection function
def BlockStorageConnection(storage_account_name, storage_account_key):

    return BlockBlobService(storage_account_name, storage_account_key)


#Uploader function
def uploadfile(block_blob_service,
               storage_container_name,
               filename,
               local_file_name,
               file_content_type):

    print ("\n*****UPLOADING FILE*****")
    print (local_file_name)
    print ('\n')

    #uploading file
    block_blob_service.retry = no_retry

    block_blob_service.create_blob_from_path(storage_container_name,
                                filename,
                                local_file_name,
                                content_settings=ContentSettings(
                                        content_type=file_content_type),
                                if_none_match='*',
                                timeout='30'
                              )
    print ("\n*****FILE UPLOADED*****")
#uploader function end


def getTimeForFile():

    return datetime.datetime.now().strftime('%B %d, %Y %H:%M:%S.%f')


def checkNetwork():

    try:
        response = requests.get("http://www.google.com")
        print (("\nRESPONSE CODE: " + str(response.status_code)))
        return True
    except requests.ConnectionError:
        print ("\nCOULD NOT CONNECT. ERROR IN CHECKNETWORK()...")
        return False


def testImage(blob_service):

    cf.BaseUrl.set(credentials.face_api_base_url)

    cf.Key.set(credentials.face_api_key)

    generator = get_list_blobs(blob_service, credentials.storage_container_name)

    lst = list(generator)

    get_blob_from_storage(blob_service,
        credentials.storage_container_name,
        lst,
        credentials.face_api_downloaded_blob_loc)

    response = detect(credentials.face_api_downloaded_blob_loc, lst)

    face_ids = [d['faceId'] for d in response]

    identified_faces = identify(face_ids, credentials.face_api_person_group_id)

    if identified_faces is not None:
        person_lists = get_person_lists(credentials.face_api_person_group_id)

        identified_persons = []

        for face in identified_faces:
            temp_list = face['candidates']
            for content in temp_list:
                identified_persons.append(content['personId'])

        print ('\n\n')

        for person in person_lists:
            if person['personId'] in identified_persons:
                print ((person['name']))

    delete_file(credentials.face_api_downloaded_blob_loc + lst[-1].name)


def get_list_blobs(blob_service, storage_container_name):

    try:
        generator = blob_service.list_blobs(storage_container_name)
        return generator
    except:
        print ('\nERROR IN RETRIEVING LIST OF BLOBS...')


def identify(face_ids, face_api_person_group_id):

    try:
        identified_faces = cf.face.identify(face_ids, face_api_person_group_id)
        return identified_faces
    except:
        print ('\nNO ONE IDENTIFIED...')
        return None


def detect(downloaded_blob_loc, lst):

    try:
        response = cf.face.detect(downloaded_blob_loc + lst[-1].name)
        return response
    except:
        print ('\nERROR IN DETECTING IMAGE...(RESPONSE)...')


def get_person_lists(face_api_person_group_id):

    try:
        person_lists = cf.person.lists(face_api_person_group_id)
        return person_lists
    except:
        print ('\nERROR IN RETRIEVING PERSONS\' LISTS...')


def get_blob_from_storage(blob_service,
    storage_container_name,
    lst,
    downloaded_blob_loc):

    try:
        blob_service.get_blob_to_path(storage_container_name,
            lst[-1].name,
            downloaded_blob_loc + lst[-1].name)
    except:
        print ('\nERROR IN RETRIEVING BLOB FROM STORAGE...')


def delete_file(file_path):

    try:
        os.remove(file_path)
        print ('\nDELETED...')
    except:
        print ('\nERROR IN DELETING FILE...')