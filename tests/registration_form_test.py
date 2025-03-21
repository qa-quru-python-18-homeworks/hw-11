import os

from pages.registration_form_page import RegistrationFormPage


def test_registration_form():
    form_page = RegistrationFormPage()

    form_page.fill_form(
        first_name='John',
        last_name='Doe',
        email='john.doe@example.com',
        gender='Male',
        mobile='1234567890',
        date_of_birth=(1, 0, 2000),
        subjects=['Physics', "Maths", "Computer Science"],
        hobbies=['Sports', 'Reading', 'Music'],
        picture=os.path.join(os.path.dirname(__file__), "resources", "image.png"),
        address='Some address',
        state='NCR',
        city='Delhi'
    ).should_have_submitted(
        student_name='John Doe',
        student_email='john.doe@example.com',
        gender='Male',
        mobile='1234567890',
        date_of_birth='01 January,2000',  # Именно так выводит demoqa
        subjects='Physics, Maths, Computer Science',
        hobbies='Sports, Reading, Music',
        picture='image.png',
        address='Some address',
        state_and_city='NCR Delhi'
    ).close_modal()
