from selene import have, be, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


class RegistrationFormPage:
    def fill_form(
            self,
            first_name,
            last_name,
            email,
            gender,
            mobile,
            date_of_birth,
            subjects,
            hobbies,
            picture,
            address,
            state,
            city
    ):
        self.__open_page() \
            .__set_first_name(first_name) \
            .__set_last_name(last_name) \
            .__set_email(email) \
            .__select_gender(gender) \
            .__set_mobile_number(mobile) \
            .__set_birth_date(*date_of_birth) \
            .__add_subjects(subjects) \
            .__select_hobbies(hobbies) \
            .__upload_picture(picture) \
            .__set_current_address(address) \
            .set_state(state) \
            .__set_city(city) \
            .__submit()
        return self

    def __open_page(self):
        browser.open('https://demoqa.com/automation-practice-form')
        return self

    def __set_first_name(self, value):
        s('#firstName').type(value)
        return self

    def __set_last_name(self, value):
        s('#lastName').type(value)
        return self

    def __set_email(self, value):
        s('#userEmail').type(value)
        return self

    def __select_gender(self, gender):
        gender_map = {
            'Male': 'label[for="gender-radio-1"]',
            'Female': 'label[for="gender-radio-2"]',
            'Other': 'label[for="gender-radio-3"]'
        }
        s(gender_map[gender]).click()
        return self

    def __set_mobile_number(self, value):
        s('#userNumber').type(value)
        return self

    def __set_birth_date(self, day: int, month: int, year: int):
        s('#dateOfBirthInput').click()
        s('.react-datepicker__month-select').element(f'option[value="{month}"]').click()
        s('.react-datepicker__year-select').element(f'option[value="{year}"]').click()
        day_str = f'{day:02d}'
        s(f'.react-datepicker__day--0{day_str}:not(.react-datepicker__day--outside-month)').click()
        return self

    def __add_subjects(self, subjects):
        for subject in subjects:
            s('#subjectsInput').type(subject).press_enter()
        return self

    def __select_hobbies(self, hobbies):
        hobby_map = {
            'Sports': 'label[for="hobbies-checkbox-1"]',
            'Reading': 'label[for="hobbies-checkbox-2"]',
            'Music': 'label[for="hobbies-checkbox-3"]'
        }
        for hobby in hobbies:
            s(hobby_map[hobby]).click()
        return self

    def __upload_picture(self, file_path):
        s('#uploadPicture').send_keys(file_path)
        return self

    def __set_current_address(self, value):
        s('#currentAddress').type(value)
        return self

    def set_state(self, state_name):
        s('#state').click()
        s('#react-select-3-input').type(state_name).press_enter()
        return self

    def __set_city(self, city_name):
        s('#city').click()
        s('#react-select-4-input').type(city_name).press_enter()
        return self

    def __submit(self):
        s('#submit').click()
        return self

    def should_have_submitted(
            self,
            student_name,
            student_email,
            gender,
            mobile,
            date_of_birth,
            subjects,
            hobbies,
            picture,
            address,
            state_and_city
    ):
        s('.modal-content').should(be.visible)
        s('table tbody tr:nth-of-type(1) td:nth-of-type(2)').should(have.text(student_name))
        s('table tbody tr:nth-of-type(2) td:nth-of-type(2)').should(have.text(student_email))
        s('table tbody tr:nth-of-type(3) td:nth-of-type(2)').should(have.text(gender))
        s('table tbody tr:nth-of-type(4) td:nth-of-type(2)').should(have.text(mobile))
        s('table tbody tr:nth-of-type(5) td:nth-of-type(2)').should(have.text(date_of_birth))
        s('table tbody tr:nth-of-type(6) td:nth-of-type(2)').should(have.text(subjects))
        s('table tbody tr:nth-of-type(7) td:nth-of-type(2)').should(have.text(hobbies))
        s('table tbody tr:nth-of-type(8) td:nth-of-type(2)').should(have.text(picture))
        s('table tbody tr:nth-of-type(9) td:nth-of-type(2)').should(have.text(address))
        s('table tbody tr:nth-of-type(10) td:nth-of-type(2)').should(have.text(state_and_city))
        return self

    def close_modal(self):
        s('#closeLargeModal').perform(command.js.click)
        return self
