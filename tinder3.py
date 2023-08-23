class UserProfile:
    mprofiles = []
    fprofiles = []

    def __init__(self, name, age, gender, occupation, hobby):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.hobby = hobby

    def add_profile(self):
        if self.age < 18:
            print("You are not allowed to use this app!")
        elif self.gender == "F":
            UserProfile.fprofiles.append(self)
        else:
            UserProfile.mprofiles.append(self)

    @classmethod
    def get_profiles(cls, gender):
        if gender == "F":
            return cls.fprofiles
        else:
            return cls.mprofiles

name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
occupation = input("Enter your occupation: ")
hobby = input("Enter your hobby: ")

user_profile = UserProfile(name, age, gender, occupation, hobby)
user_profile.add_profile()

requested_gender = input("Enter the gender you're interested in (M/F): ")
requested_profiles = UserProfile.get_profiles(requested_gender)

print("Matching profiles:")
for profile in requested_profiles:
    print(f"Name: {profile.name}, Age: {profile.age}, Gender: {profile.gender}, Occupation: {profile.occupation}, Hobby: {profile.hobby}")
