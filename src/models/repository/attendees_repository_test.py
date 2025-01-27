import pytest
from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason='Novo registro banco de dados')
def test_insert_attendees():
    event_id='meu-uuid-e-nois'
    attendees_info={
        "uuid": "meu_uuid_attendee",
        "name": "attendee name3",
        "email": "email3@example.com",
        "event_id": event_id

    } 
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendees_info)
    print(response)
@pytest.mark.skip(reason='Teste de integração')
def test_get_attendee_badge_by_id():
    attendde_id = "meu_uuid_attendee"
    attendees_repository = AttendeesRepository()
    attendee = attendees_repository.get_attendee_badge_by_id(attendde_id)

    print(attendee)   
    print(attendee.title)

