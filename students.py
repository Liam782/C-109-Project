import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("StudentsPerformance.csv")

reading_score_list = df["reading score"].tolist()

mean = statistics.mean(reading_score_list)
median = statistics.median(reading_score_list)
mode = statistics.mode(reading_score_list)
std_deviation = statistics.stdev(reading_score_list)

print("Mean, Median and mode of the score dataset is {},{} and {}".format(mean, median, mode))     

first_std_deviation_start = mean - std_deviation
first_std_deviation_end = mean + std_deviation
list_of_data_within_1_std_deviation = [score for score in reading_score_list if score > first_std_deviation_start and score < first_std_deviation_end]
print("{}% of data that lies within first std deviation ".format(len(list_of_data_within_1_std_deviation)*100/len(reading_score_list)))

second_std_deviation_start = mean - (2* std_deviation)
second_std_deviation_end = mean + (2* std_deviation)
list_of_data_within_second_std_deviation = [score for score in reading_score_list if score > second_std_deviation_start and score < second_std_deviation_end]
print("{}% is the data that lies within the second standard deviation".format(len(list_of_data_within_second_std_deviation)*100/len(reading_score_list)))

third_std_deviation_start = mean - (3* std_deviation)
third_std_deviation_end = mean + (3* std_deviation)
list_of_data_within_third_std_deviation = [score for score in reading_score_list if score > third_std_deviation_start and score < third_std_deviation_end]
print("{}% is the data that lies within the third standard deviation".format(len(list_of_data_within_third_std_deviation)*100/len(reading_score_list)))