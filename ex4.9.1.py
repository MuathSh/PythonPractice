#keywords arguments
def employee(name, job, *skills, **details):
    profile = {
        "name": name,
        "job": job,
        "skills":list(skills),
    }
    profile.update(details)
    return profile


# 1. An employee without skills
emp1 = employee("carl", "guard")

# 2. An emplyee with 4 skills
emp2 = employee(
    "Ahmad",
    "C programmer",
    "Linux",
    "Git",
    "Makefiles",
    "GDB",
    City="Riyadh",
    Phone="0500000000",
    Office_no=402,
)

print("\033[1;31mCarl:\033[0m")
for key, value in emp1.items():
    print(f"\033[1;32m{key}\033[0m: \033[1;34m{value}\033[0m")

print("\033[1;31mAhmad's card:\033[0m")
for key, value in emp2.items():
    print(f"\033[1;32m{key}\033[0m: \033[1;34m{value}\033[0m")