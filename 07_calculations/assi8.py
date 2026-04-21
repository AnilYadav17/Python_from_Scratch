'''8. Weather Monitoring System

A weather monitoring system classifies the weather condition based on temperature:

* Below 0°C → Freezing
* 0°C to 20°C → Cold
* 21°C to 35°C → Warm
* Above 35°C → Hot

Write a Python program to classify the weather.

Input:
Enter temperature: 38

Output:
Weather Condition: Hot'''

temp = float(input("Enter temperature: "))

if temp>0:
    if temp>=20:
        if temp>20 and temp<=35:
            if temp>35:
                print("Weather Condition: Hot")
            else:
                print("Weather Condition: Warm")
        else:
            print("Weather Condition: Cold")
else:
     print("Weather Condition: Freezing")
