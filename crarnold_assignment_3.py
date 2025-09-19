#COMP 163 
#Assignment 3
#Have participants vote for the 'lie.'
#Engagement: Reveal the answer (C) and explain why AI can’t file PTO (yet!).
#Fun quip: 'Imagine AI filing your PTO… it might decide you need a vacation more than you think!'
#Have participants vote for the 'lie.'
#Engagement: Reveal the answer (C) and explain why AI can’t file PTO (yet!).
#Have participants vote for the 'lie.'
#Christopher Arnold
#crarnold
#
#
#PERSONAL INFORMATION (STRINGS)
full_name = "Lauren Arnold"
student_email = "larnold@ncat.edu"
hometown = "Washington, DC"
graduation_semester = "Spring 2029"
major = "Computer Science"

#ACADEMIC DATA ORGANIZATION (LIST VALUES)
current_courses_list = ["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
completed_courses_list =["Biology", "Chemistry", "Calculus", "Spanish II", "World History"]
credit_hours_list =[3, 3, 3, 3] #corresponding to current courses
gpa_history_list = [3.2, 3.6, 3.4, 3.7] #semester GPAs as floats

#CONTACT INFORMATION STORAGE (TUPLES)
emergency_contact = ("Mom", "Hannah Smith", "704-555-0199")
home_address = ("456 Oak Street", "Laurel", "MD", 28202)
instagram = ("Instagram", "@laureniam", 312)
twitter = ("Twitter", "@jordandev", 127)
birthday = ("Birthday", 5, 22, 1983)

#INTEREST TRACKING 
current_skills = {"Python basics", "HTML", "Problem solving", "Time management", "Photography"}
skills_to_learn = {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
career_interests = {"Software development", "Web development", "Data science", "Game development"}
hobbies_set = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertainment_set = {"One Piece", "Barry", "Life", "Incantation", "Memento"}

#ORGANIZATIONAL MAPPING (Dictionary)
Course_credits_dictionary =  {"COMP 163": 3, "MATH 150": 3, "ENG 101": 3, "HIS 105": 3}
Course_professors_dictionary =  {"COMP 163": "Prof. Rhodes", "MATH 150": "Dr. Lee","ENG 101": "Dr. Martinez", "HIS 105": "Dr. Brown"}
Course_rooms_dictionary =  {"COMP 163": "M-Eric 300", "MATH 150": "Marteena 201", "ENG 101": "Crosby 121", "HIS 105": "Crosby 210"}
Monthly_budget_dictionary =  {"Food": 450, "Entertainment": 200, "Books": 125, "Transportation": 100}
Study_hours_per_subject_dictionary =  {"Programming": 10, "Math": 8, "English": 4, "History": 3}
Contact_directory_dictionary = {"Mom": "704-555-0199", "Roommate": "336-555-7821", "Academic Advisor": "336-334-5000"}

#REQUIRED CALCULATIONS
total_current_credits = sum(credit_hours_list)
cumulative_gpa = ((gpa_history_list[0] * credit_hours_list[0])+(gpa_history_list[1] * credit_hours_list[1])+(gpa_history_list[2]*credit_hours_list[2])+(gpa_history_list[3]*credit_hours_list[3])) / total_current_credits
count_of_completed_courses = len(completed_courses_list)
total_weekly_study_hours = sum(Study_hours_per_subject_dictionary.values())
academic_load_credit_study_hours = sum(credit_hours_list) + total_weekly_study_hours
monthly_budget_total_all_cat = sum(Monthly_budget_dictionary.values())
daily_food_budget = round(Monthly_budget_dictionary["Food"] / 30, 2)
annual_budget_projection = sum(Monthly_budget_dictionary.values()) * 12 #monthly total * 12
study_cost_per_hour = round(Monthly_budget_dictionary["Books"] / total_weekly_study_hours) #books budget / total study hours, rounded to 2 decimals

#ANALYTICS CALCULATIONS
total_social_media_followers = twitter[2] + instagram[2]
curr_skills_count = len(current_skills)
skills_to_learn_count = len(skills_to_learn)
contact_directory_size = len(Contact_directory_dictionary.values())
entertainment_backlog_count = len(entertainment_set)
academic_workload_assessment = 0
 
#PRINTING
print (f"Daily food budget: {daily_food_budget}")
print (f"Total current credits from credit hours list: {total_current_credits}")
print (f"Cumulative GPA from GPA history list: {cumulative_gpa}")
print (f"Count of completed courses: {count_of_completed_courses}")
print (f"Total weekly study hours from study hours dictionary: {total_weekly_study_hours}")
print (f"Academic load (credits + study hours combined): {academic_load_credit_study_hours}")
print (f"Monthly budget total from all categories: {monthly_budget_total_all_cat}")
print (f"Daily food budget (food amount ÷ 30, rounded to 2 decimals: ")
print (f"Annual budget projection (montohly total × 12): ")
print (f"Study cost per hour (books budget ÷ total study hours, rounded to 2 decimals): ")
print (f"Analytics Calculations:/n/n")
print (f"Total social media followers from platform tuples: {total_social_media_followers}")
print (f"Skills count comparison (current vs. learning goals): {curr_skills_count} vs {skills_to_learn_count}")
print (f"Contact directory size analysis: {contact_directory_size}")
print (f"Entertainment backlog management count: {entertainment_backlog_count}")
print (f"Academic workload assessment: {academic_workload_assessment}")
