import csv
from datetime import datetime

def collect_survey():
    print("🌱 Welcome to the Student Wellness Survey 🌱\n")

    name = input("What is your name? ")
    age = input("How old are you? ")
    mood = input("How are you feeling today? (Happy, Sad, Stressed, Neutral) ")
    sleep_hours = input("How many hours did you sleep last night? ")
    exercise = input("Did you exercise today? (Yes/No) ")
    study_hours = input("How many hours did you study today? ")
    additional_comments = input("Any additional comments about your wellness? ")

    survey_data = [
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        name,
        age,
        mood,
        sleep_hours,
        exercise,
        study_hours,
        additional_comments
    ]

    # Save to CSV
    with open('student_wellness_survey.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(survey_data)

    print("\n✅ Thank you for submitting your wellness survey!")


def main():
    print("📊 Student Wellness Survey System 📊\n")

    # Add CSV headers if file is empty
    try:
        with open('student_wellness_survey.csv', 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                "Timestamp", "Name", "Age", "Mood",
                "Sleep Hours", "Exercised Today",
                "Study Hours", "Additional Comments"
            ])
    except FileExistsError:
        pass  # File already exists

    collect_survey()


if __name__ == "__main__":
    main()