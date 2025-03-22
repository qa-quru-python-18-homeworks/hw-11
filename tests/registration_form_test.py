import os

from pages.registration_form_page import RegistrationFormPage


def test_registration_form():
    form_page = RegistrationFormPage()

    form_page \
    .open_page() \
    .set_first_name("John") \
    .set_last_name("Doe") \
    .set_email("john.doe@example.com") \
    .select_gender("Male") \
    .set_mobile_number("1234567890") \
    .set_birth_date(day=1, month=0, year=2000) \
    .add_subjects(["Physics", "Maths", "Computer Science"]) \
    .select_hobbies(["Sports", "Reading", "Music"]) \
    .upload_picture(os.path.join(os.path.dirname(__file__), "resources", "image.png")) \
    .set_current_address("Some address") \
    .set_state("NCR") \
    .set_city("Delhi") \
    .submit() \
    .should_have_submitted(
        student_name="John Doe",
        student_email="john.doe@example.com",
        gender="Male",
        mobile="1234567890",
        date_of_birth="01 January,2000",  # Именно так выводит demoqa
        subjects="Physics, Maths, Computer Science",
        hobbies="Sports, Reading, Music",
        picture="image.png",
        address="Some address",
        state_and_city="NCR Delhi",
    ) \
    .close_modal()
