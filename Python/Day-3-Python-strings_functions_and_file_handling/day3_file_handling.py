# 1. File Handling kya hai?
'''Python mein File Handling ka use files ko create, read, write aur update karne ke liye hota hai.
1. w = Write = File mein data likhna. Existing content overwrite ho sakta hai.
2. r = read = File ka existing content padhna.
3. a = append = Existing content ke end mein naya data add karna.
'''
# 1.1 Write(w)
# with open("study_data.txt", "w")as file:
#     file.write("Project VED Sttudy Tracker\n")
#     file.write("daily study hours: 4\n")
#     file.write("weekly study hours: 28\n")

# print("data saved successfully!")
'''
Important: w mode purani file ke content ko overwrite karta hai. Isliye existing file par use karte waqt careful rehna.
with open() kyun use karte hain?
- open() file kholta hai.
- "w" writing mode select karta hai.
- file.write() text save karta hai.
- with block complete hone par file automatically close ho jaati hai.
'''
# 1.2 Read(r)
# with open("study_data.txt", "r")as file:
#     data=file.read()
# print("==== Saved Study Data ====")
# print(data)
'''
Dono files ko same folder mein rakho, taaki Python study_data.txt ko easily locate kar sake. Agar file nahi milegi, toh FileNotFoundError aayega.'''

# 1.3 Append(a)
# with open("study_data.txt", "a")as file:
#     file.write("New study session: 2 hours\n")
# print("New record added!")
'''Har baar is code ko run karne par ek naya record add hoga.'''

